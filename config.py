aws_db = {
    "user": "admin",
    "password": "hongik45",
    "host": "honggumdb.capnwelofgc3.ap-northeast-2.rds.amazonaws.com",
    "port": "3306"
    "database": "honggumdb",
}

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{aws_db['user']}:{aws_db['password']}@{aws_db['host']}:{aws_db['port']}/{aws_db['database']}?charset=utf8"
