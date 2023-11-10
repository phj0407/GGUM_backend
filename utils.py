from flask import Flask
import mysql.connector
from passlib.hash import pbkdf2_sha256


# 암호화 알고리즘. 256을 제일 많이 사용한다.

# 원문 비밀번호를, 암호화 하는 함수

def hash_password(original_password, salt):
    password = original_password + salt
    password = pbkdf2_sha256.hash(password)
    return password


def check_password(original_password, salt, hashed_password):

    # 입력 비밀번호에 동일한 솔트 값을 추가하여 해싱
    print(original_password, salt)
    check = pbkdf2_sha256.verify(original_password, hashed_password)

    # 해시된 입력 비밀번호와 저장된 해시된 비밀번호 비교
    return check
def get_connection():
    connection = mysql.connector.connect(
        host="honggumdb.capnwelofgc3.ap-northeast-2.rds.amazonaws.com",
        user="admin",
        port="3306",
        password="hongik45",
        database="honggumDB"
    )
    return connection
