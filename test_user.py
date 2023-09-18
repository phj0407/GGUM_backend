from flask import Flask, request, jsonify
from utils import*

# import config
app = Flask(__name__)

@app.route('/')
def main():
	return 'home_page'

# 회원정보 ------------------------------------------------------------------
@app.route('/users/login')
def login():
		 data = request.get_json()
		 connection = get_connection()
		 cursor = connection.cursor()

		 query = '''
			 SELECT password  FROM user WHERE student_id = %s
			 '''
		 try:
			 cursor.execute(query, record)		# 쿼리 실행, record에 쿼리에서 사용하는 변수를 바인딩
			 password = cursor.fetchone()		# 쿼리 실행 결과 가져오기
		 except:
			return{
				"msg" : "cursor execute failed"
				}

		 hashed_password = hash_password(data["password"])			#비밀번호 암호화 & 검사
		 check = check_password(data["password"], hashed_password)

		 if check:
			 return {
						"msg" : "로그인 성공",
						"result" : 1
					}
		 else:
			 return {
				 "msg" : "사용자 조회 실패",
				 "result" : 0
				 }

@app.route('/users/register', mehotds=['POST'])
def sign_in():
			data = request.get_json()
			connection = get_connection()
			cursor = connection.cursor()

			query = '''
			INSERT INTO user (user_id, student_id, name, cohort)
			VALUES (%d, %s, %s, %d)
			'''
			values = (new_user_id, data["student_id"],  data["name"], data["cohort"])
			try:
				cursor.execute(query, values)
				connection.commit()
			except:
				return {
					"msg" : "query execute failed"
					}

			cursor.close()
			connection.close()

			return {
				"result" : "user register sccuess",
				}
from flask import Flask, request, jsonify
from utils import*

# import config
app = Flask(__name__)

@app.route('/')
def main():
	return 'home_page'

# 회원정보 ------------------------------------------------------------------
@app.route('/users/login')
def login():
		 data = request.get_json()
		 connection = get_connection()
		 cursor = connection.cursor()

		 query = '''
			 SELECT password  FROM user WHERE student_id = %s
			 '''
		 try:
			 cursor.execute(query, record)		# 쿼리 실행, record에 쿼리에서 사용하는 변수를 바인딩
			 password = cursor.fetchone()		# 쿼리 실행 결과 가져오기
		 except:
			return{
				"msg" : "cursor execute failed"
				}

		 hashed_password = hash_password(data["password"])			#비밀번호 암호화 & 검사
		 check = check_password(data["password"], hashed_password)

		 if check:
			 return {
						"msg" : "로그인 성공",
						"result" : 1
					}
		 else:
			 return {
				 "msg" : "사용자 조회 실패",
				 "result" : 0
				 }

@app.route('/users/register', mehotds=['POST'])
def sign_in():
			data = request.get_json()
			connection = get_connection()
			cursor = connection.cursor()

			query = '''
			INSERT INTO user (user_id, student_id, name, cohort)
			VALUES (%d, %s, %s, %d)
			'''
			values = (new_user_id, data["student_id"],  data["name"], data["cohort"])
			try:
				cursor.execute(query, values)
				connection.commit()
			except:
				return {
					"msg" : "query execute failed"
					}

			cursor.close()
			connection.close()

			return {
				"result" : "user register sccuess",
				}
from flask import Flask, request, jsonify
from utils import*

# import config
app = Flask(__name__)

@app.route('/')
def main():
	return 'home_page'

# 회원정보 ------------------------------------------------------------------
@app.route('/users/login')
def login():
		 data = request.get_json()
		 connection = get_connection()
		 cursor = connection.cursor()

		 query = '''
			 SELECT password  FROM user WHERE student_id = %s
			 '''
		 try:
			 cursor.execute(query, record)		# 쿼리 실행, record에 쿼리에서 사용하는 변수를 바인딩
			 password = cursor.fetchone()		# 쿼리 실행 결과 가져오기
		 except:
			return{
				"msg" : "cursor execute failed"
				}

		 hashed_password = hash_password(data["password"])			#비밀번호 암호화 & 검사
		 check = check_password(data["password"], hashed_password)

		 if check:
			 return {
						"msg" : "로그인 성공",
						"result" : 1
					}
		 else:
			 return {
				 "msg" : "사용자 조회 실패",
				 "result" : 0
				 }

@app.route('/users/register', mehotds=['POST'])
def sign_in():
			data = request.get_json()
			connection = get_connection()
			cursor = connection.cursor()

			query = '''
			INSERT INTO user (user_id, student_id, name, cohort)
			VALUES (%d, %s, %s, %d)
			'''
			values = (new_user_id, data["student_id"],  data["name"], data["cohort"])
			try:
				cursor.execute(query, values)
				connection.commit()
			except:
				return {
					"msg" : "query execute failed"
					}

			cursor.close()
			connection.close()

			return {
				"result" : "user register sccuess",
				}
from flask import Flask, request, jsonify
from utils import*

# import config
app = Flask(__name__)

@app.route('/')
def main():
	return 'home_page'

# 회원정보 ------------------------------------------------------------------
@app.route('/users/login')
def login():
		 data = request.get_json()
		 connection = get_connection()
		 cursor = connection.cursor()

		 query = '''
			 SELECT password  FROM user WHERE student_id = %s
			 '''
		 try:
			 cursor.execute(query, record)		# 쿼리 실행, record에 쿼리에서 사용하는 변수를 바인딩
			 password = cursor.fetchone()		# 쿼리 실행 결과 가져오기
		 except:
			return{
				"msg" : "cursor execute failed"
				}

		 hashed_password = hash_password(data["password"])			#비밀번호 암호화 & 검사
		 check = check_password(data["password"], hashed_password)

		 if check:
			 return {
						"msg" : "로그인 성공",
						"result" : 1
					}
		 else:
			 return {
				 "msg" : "사용자 조회 실패",
				 "result" : 0
				 }

@app.route('/users/register', mehotds=['POST'])
def sign_in():
			data = request.get_json()
			connection = get_connection()
			cursor = connection.cursor()

			query = '''
			INSERT INTO user (user_id, student_id, name, cohort)
			VALUES (%d, %s, %s, %d)
			'''
			values = (new_user_id, data["student_id"],  data["name"], data["cohort"])
			try:
				cursor.execute(query, values)
				connection.commit()
			except:
				return {
					"msg" : "query execute failed"
					}

			cursor.close()
			connection.close()

			return {
				"result" : "user register sccuess",
				}
