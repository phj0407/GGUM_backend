from flask import Flask, request, jsonify
from utils import *

# import config
app = Flask(__name__)


@app.route('/')
def main():
    return 'home_page'


# 회원정보 ------------------------------------------------------------------
@app.route('/users')
def login():
    data = request.get_json()
    connection = get_connection()
    cursor = connection.cursor()
    input_password = data["password"]

    query = '''
             SELECT password, id  FROM user WHERE school_id = %s
             '''
    cursor.execute(query, (data["school_id"],))
    result = cursor.fetchall()

    if pbkdf2_sha256.verify(input_password, result[0]):
        return {
            "msg": "로그인 성공",
            "user_id" : result[1]
        }
    else:

        return {
            "msg": "사용자 조회 실패",
            "result": 0,
            "saved_password" : result[1],
            "original_password+hash" : data["password"]+data["school_id"],
        }


@app.route('/users', methods=['POST'])
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
        "result": "user register success",
        "pss" : hashed_password
    }


if __name__ == '__main__':
    app.run(debug=True)
