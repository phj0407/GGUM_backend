from flask import request, Blueprint
from utils import*

bp_user = Blueprint('users', __name__, url_prefix='/users')


# 회원정보 ------------------------------------------------------------------
@bp_user.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    connection = get_connection()
    cursor = connection.cursor()

    input_password = data["password"]
    student_number = data["student_number"]

    query = '''
             SELECT password, id  FROM user WHERE student_number = %s
             '''
    cursor.execute(query, (student_number,))
    result = cursor.fetchone()

    if check_password(input_password, student_number, result[0]):
        return {
            "msg": "로그인 성공",
            "id" : result[1]
        }
    else:

        return {
            "msg": "사용자 조회 실패",
        }


@bp_user.route('/register', methods=['POST'])
def sign_in():
    data = request.get_json()
    connection = get_connection()
    cursor = connection.cursor()

    query = '''
            INSERT INTO user ( name, student_number, cohort, password )
            VALUES (%s, %s, %s, %s)
            '''
    hashed_password = hash_password(data["password"],data["student_number"])
    values = (data["name"], data["student_number"], data["cohort"], hashed_password)

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return {
        "msg": "사용자 등록 성공",
    }

