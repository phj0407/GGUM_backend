from flask import request, Blueprint
from utils import*

bp_notice = Blueprint('notice', __name__, url_prefix='/notices')

app = Flask(__name__)


def check_notice_publisher(cursor, notice_id, user_id):
    get_query = '''
        SELECT user_id 
        FROM notice 
        WHERE id = %s
        '''
    cursor.execute(get_query, (notice_id,))

    db_user_id = cursor.fetchone()[0]
    return db_user_id == user_id


@bp_notice.route('/')
def get_notice(): #최근 n개 공지를 반환, , http://127.0.0.1:5000/notice?count=n 꼴로 요청
    count = request.args.get('count', default=5, type=int)
    connection = get_connection()
    cursor = connection.cursor()

    get_query = '''
    SELECT * FROM notice 
    order by id desc 
    limit %s
    '''
    cursor.execute(get_query, (count,))
    result_list = cursor.fetchall()
    notice_id_list = []
    for row in result_list:
        notice_id_list.append(row[0])
    return {
        'notice ids': notice_id_list
    }


@bp_notice.route('/', methods=['POST'])
def post_notice(): #공지 게시
    connection = get_connection()
    cursor = connection.cursor()
    data = request.get_json()

    insert_query = ''' 
        INSERT INTO notice (user_id, title, content) 
        VALUES (%s, %s, %s)
        '''

    values = (data["user_id"], data["title"], data["content"])
    cursor.execute(insert_query, values)
    notice_id = cursor.lastrowid

    connection.commit()
    cursor.close()
    connection.close()

    return {
        "notice id": notice_id
    }


@bp_notice.route("/<int:notice_id>", methods=['PUT'])
def update_notice(notice_id):
    connection = get_connection()
    cursor = connection.cursor()

    data = request.get_json()

    update_query = '''
        UPDATE notice 
        SET content = %s 
        WHERE id = %s
        '''

    if check_notice_publisher(cursor, notice_id, data['user_id']):
        values = (data["content"], notice_id)
        cursor.execute(update_query, values)
        connection.commit()
        msg = "공지 수정 완료"

    else:
        msg = "작성자와 일치하지 않습니다"

    return {
        'msg': msg
    }


@bp_notice.route("/<int:notice_id>", methods=['DELETE'])
def delete_notice(notice_id):
    connection = get_connection()
    cursor = connection.cursor()

    data = request.get_json()
    delete_query = '''
    DELETE FROM notice WHERE id = %s
    '''

    if check_notice_publisher(cursor, notice_id, data['user_id']):
        cursor.execute(delete_query, (notice_id,))
        connection.commit()
        msg = "공지 삭제 완료"
    else:
        msg = "작성자와 일치하지 않습니다"

    return {
        'msg': msg
    }


if __name__ == '__main__':
    app.run(debug=True)
