from flask import request, Blueprint
from utils import*

bp_diary = Blueprint('diary', __name__, url_prefix='/diaries')
# import config

@bp_diary.route('/<string:date>', methods=['GET', 'POST'])
def get_and_create_diary(date):
    if request.method=='GET':
        # 해당 날짜에 등록된 diary 의 {id, title, user_name} 을 반환
        connection = get_connection()
        cursor = connection.cursor()

        get_diary_query = '''
        SELECT d.title, d.id, d.user_id, u.name
        FROM diary d
        JOIN user u ON d.user_id = u.id
        WHERE d.diary_date = %s
        '''

        cursor.execute(get_diary_query, (date,))
        result = cursor.fetchall()

        diary_list = []
        for row in result:
            title, id, user_id, user_name = row
            diary_entry = {
                "diary_id" : id,
                "title" : title,
                "user_name" : user_name,
            }
            diary_list.append(diary_entry)


        cursor.close()
        connection.close()

        return {"diary datas" : diary_list};

    if request.method == 'POST':
        #new_diary 를 DB에 추가하고 새로 생성한 diary의 id를 반환
        data = request.get_json()

        connection = get_connection()
        cursor = connection.cursor()
        new_diary = (data["user_id"], date, data["title"], data["content"], )

        insert_query = '''
        INSERT INTO diary (user_id, diary_date, title, content ) 
        VALUES ( %s, %s, %s, %s );
        '''

        cursor.execute(insert_query, new_diary)
        connection.commit()
        cursor.execute('SELECT LAST_INSERT_ID()')
        new_diary_id = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return{
            "msg": "일기 등록 성공",
            "diary id": new_diary_id
        }

@bp_diary.route('/<date>/<int:user_id>', methods =[ 'PUT', 'DELETE'])
#TODO : 작성자 확인 로직 추가
def diary_manage(date, user_id):
    if request.method == 'PUT': # 특정 날짜에 특정 사용자가 작성한 diary 내요을 수정
        data = request.get_json()
        connection = get_connection()
        cursor = connection.cursor()

        update_query = '''
        UPDATE diary 
        SET content = %s 
        WHERE user_id = %s AND diary_date=%s
        '''
        values = (data["content"], user_id, date)
        cursor.execute(update_query, values)
        connection.commit()
        cursor.close()
        connection.close()

        return{
            "msg": "일기 수정 완료",
            }

    if request.method == 'DELETE': # 특정 날짜에 특정 사용자가 작성한 diary를 삭제
        values = (user_id, date)

        connection = get_connection()
        cursor = connection.cursor()
        delete_query = '''
        DELETE FROM diary 
        WHERE user_id=%s AND diary_date=%s
        '''
        cursor.execute(delete_query, values)
        connection.commit()

        cursor.close()
        connection.close()
        return {
            'msg': '일기 삭제 완료'
            }






