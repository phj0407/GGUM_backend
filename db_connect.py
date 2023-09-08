import mysql.connector

#MySQL 연결정보 설정
app.config['MYSQL_HOST'] = 'honggumdb.capnwelofgc3.ap-northeast-2.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'hongik45'
app.config['MYSQL_DB'] = 'honggumdb'

#MySQL 연결 생성
def get_connection():
	conncection = mysql.connector.connect(
		host=app.config['MYSQL_HOST'],
		user=app.config['MYSQL_USER'],
		password=app.config['MYSQL_PASSWORD'],
		database=app.config['MYSQL_DB'],
		)
	return connection