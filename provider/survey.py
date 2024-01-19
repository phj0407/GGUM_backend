from flask import request, Blueprint
from utils import*


bp_survey = Blueprint('survey', __name__, url_prefix='/surveys')


def check_survey_publisher(cursor, survey_id, user_id):
    get_query = '''
    SELECT publisher_id
    FROM survey
    WHERE id= %s'''
    cursor.execute(get_query, (survey_id,))
    db_user_id = cursor.fetchone()

    return {
        'survey ids' : db_user_id[0] == int(user_id)
    }


@bp_survey.route('/<int:survey_id>') #해당 survey의 정보를 로드
def get_survey_data(survey_id):
    connection = get_connection()
    cursor = connection.cursor()

    get_query = '''
    SELECT survey_date, title, description
    FROM survey
    WHERE id = %s
    '''
    cursor.execute(get_query, (survey_id,))
    data = cursor.fetchall()
    date, title, desc = data[0]

    return {
        'title': title,
        'desc': desc,
        'survey date': date,

       # 'end_date': end_date
    }


@bp_survey.route('/<int:survey_id>/participant') #해당 survey에 참석한 attendee를 로드
def get_attendee(survey_id):
    connection = get_connection()
    cursor = connection.cursor()

    get_query = '''
    SELECT attendee_id
    FROM user_survey
    WHERE survey_id = %s
    '''

    cursor.execute(get_query, (survey_id,))
    data = cursor.fetchall()

    attendee_ids = [row[0] for row in data]

    return {"attendee ids" : attendee_ids}


@bp_survey.route('/') #활성화중인 survey를 로드
def get_active_survey():
    connection = get_connection()
    cursor = connection.cursor()

    get_query = '''
    SELECT id
    FROM survey
    WHERE is_active = true
    '''
    cursor.execute(get_query)
    data = cursor.fetchall()

    survey_ids = [row[0] for row in data]

    return {"survey ids" : survey_ids}


@bp_survey.route('/', methods=['POST'])
def post_survey():  # survey 게시
    connection = get_connection()
    cursor = connection.cursor()

    data = request.get_json()

    values = (data['user_id'], data['survey_date'], data['title'], data['description'])
    insert_query = '''
        INSERT INTO survey(publisher_id, survey_date, title, description)
        VALUES (%s, %s, %s, %s)
        '''
    msg = '투표 등록 완료'

    cursor.execute(insert_query, values)
    new_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()

    return {
        'msg': msg,
        'posted survey id': new_id
    }


@bp_survey.route('/<int:survey_id>', methods=['POST'])
def participate_survey(survey_id): #survey에 attendee 등록
    connection = get_connection()
    cursor = connection.cursor()

    data = request.get_json()

    values = (data['attendee_id'], survey_id)
    insert_query = '''
            INSERT INTO user_survey(attendee_id, survey_id)
            VALUES (%s, %s)
            '''
    msg = '투표 참석 완료'
    cursor.execute(insert_query, values)
    new_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()

    return {
        'msg': msg,
    }


@bp_survey.route('/<int:survey_id>', methods=['PUT'])
def update_survey(survey_id): #투표 게시글 수정
    connection = get_connection()
    cursor = connection.cursor()
    data = request.get_json()
    msg = ""
    if check_survey_publisher(cursor, survey_id, data['user_id']):
        update_query = '''
        UPDATE survey
        SET 
        '''
        values = []
        if "survey_date" in data:
            update_query += "survey_date = %s, "
            values.append(data["survey_date"])

        if "title" in data:
            update_query += "title = %s, "
            values.append(data["title"])

        if "description" in data:
            update_query += "description = %s, "
            values.append(data["description"])

        if "is_active" in data:
            update_query += "is_active = %s, "
            values.append(data["is_active"])

        update_query = update_query[:-2]
        update_query += '''WHERE id= %s'''
        values.append(survey_id)

        cursor.execute(update_query, values)
        connection.commit()
        msg = "투표 수정 완료"

    else:
        msg = "작성자와 일치하지 않습니다"

    cursor.close()
    connection.close()

    {"msg" : msg}

@bp_survey.route('/<int:survey_id>/participant', methods=['DELETE'])
def cancel_survey(survey_id): #투표 취소
    connection = get_connection()
    cursor = connection.cursor()
    data = request.get_json()

    delete_query='''
    DELETE FROM user_survey
    WHERE survey_id=%s AND attendee_id=%s
    '''
    values = (survey_id, data['attendee_id'])
    cursor.execute(delete_query, values)
    connection.commit()

    cursor.close()
    connection.close()
    return {
        "msg": "투표 삭제 완료"
    }


@bp_survey.route('/<int:survey_id>', methods=['DELETE'])
def delete_survey(survey_id): #게시한 투표 삭제
    connection = get_connection()
    cursor = connection.cursor()
    data = request.get_json()

    if check_survey_publisher(cursor, survey_id, data['user_id']):
        delete_query = '''
        DELETE FROM survey
        WHERE id= %s
        '''
        cursor.execute(delete_query, (survey_id,) )
        msg = '삭제 완료'

        connection.commit()
    else:
        msg = '작성자와 일치하지 않습니다'

    cursor.close()
    connection.close()

    return {"msg" : msg}
