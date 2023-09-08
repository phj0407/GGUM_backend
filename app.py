from flask import Flask, request, jsonify
import config
from db_connect import get_connection
# import mysql.connector

app = Flask(__name__)

@app.route('/')
def main():
    return 'home_page'

# 회원정보 ------------------------------------------------------------------
# user table : 어떤 속성 사용할지 : ex) user_id, student_id, user_name, generation
@app.route('/users/login')
def login():
		 data = request.get_json()
		 record=(data["student_id"]) 
		 connection=get_connection() #커넥션 생성
		 query='''
			 SELECT user_id  FROM user WHERE student_id = %s
			 '''
		 cursor = connection.cursor()		# 커서 생성

		 try:
			 cursor.execute(query, record)		# 쿼리 실행, record에 쿼리에서 사용하는 변수를 바인딩
			 result = cursor.fetchone()		# 쿼리 실행 결과 가져오기

			 if result:
				 user_id = result[0]
			 else: 
				return {
					"message" : "존재하지 않는 사용자입니다.",
					"uesr_id" : -1
					}

			 cursor.close()								# 쿼리 & 커넥션 닫기
			 connection.close()

			 return {
					"message" : "사용자 조회 성공",
					"user_id" : user_id
				}

@app.route('/users/register')
def sign_in():
			data = request.get_json()
			'''
			{
			"name" : "박혜진"
			"student_id" : "C111075" 
			"generation" : "45"
			}
			'''
			#유효 형식 확인 프론트에서 구현함
			connection = get_connection()
			cursor = connection.cursor()
			new_user_id = cursor.last_row_id +1
			query ='''
			INSERT INTO user (user_id, student_id, name, generation)
			VALUES (%d, %s, %s, %d)
			'''
			values = (new_user_id, data["student_id"],  data["name"], data["generation"] )
			try:
				cursor.execute(query, values)
				connection.commit()

			cursor.close()
			connection.close()

			return {
				"result" : "user register sccuess",
				"user_id" : new_user_id
				}


# 일지 관련----------------------------------------------------------------
# diary table : 어떤 속성 사용할지 : ex) diary_id, user_id, date, content
@app.route('/users/<int:user_id>/diaries')
def get_diary(user_id):
    # all_diary = user_id 에 맞는 diary 모두 가져오기
	data = request.get_json()
	connection=get_connection() 
	cursor = connection.cursor( )
	query = '''
	SELECT date, content FROM diary WHERE user_id = %s
	'''
	try:
		cursor.execute( query, user_id)
		result = cursor.fetchall()

	diary_list=[ ]

	for row in result:
		date, content = row
		diary_entry = {
			"date" : date,
			"content" : content
			}
		diary_list.append(diary_entry)

	cursor.close()
	connection.close()
	return diary_list



@app.route('/users/<int:user_id>/diaries')
def create_diary(user_id):

    #new_diary 를 DB에 추가
    #new_diary_id = 최신 diary_id +1
	data = request.get_json( )

	connection = get_connection( )
	cursor = connection.cursor( )
	new_diary_id = cursor.last_row_id +1
	new_diary = ( user_id, new_diary_id, data["date"], data["content"] )

	insert_query = '''
	INSERT INTO diaries (user_id, diary_id, date, content ) VALUES ( %d, %d, %s, %s)
	'''
	cursor.execute(insert_query, new_diary)
	connection.commit()

	cursor.close()
	connection.close()

	return{
		"message" : "diary created successfullly",
		"diary_id" : new_diary_id
		}

@app.route('/users/<int:user_id>/diaries')
def update_diary(user_id):
	data = request.get_json()
	connection = get_connection()
	cursor = connection.cursor()

	update_query = '''
	UPDATE diaries SET content = %s WHERE user_id = %s AND date=%s
	'''
	values = (data["content"] , user_id, data["date"] )
	cursor.execute(update_query, values)

	cursor.close()
	connection.close()

	return{
		"message" : "update successfully",
		}

@app.route('/users/<int:user_id>/diaries')
def get_diary_by_date(user_id):
	date=request.args.get('date')
    # diary = user_id 중 date 에 맞는 diary 가져오기
	connection = get_connection()
	cursor = connection.cursor()
	select_query = '''
	SELECT content FROM diaries WHERE user_id = %d AND date=%s
	'''
	values = ( user_id, date)
	cursor.execute(select_query, values)
	result = cursor.fetchone( )
	cursor.close()
	connection.close()

	return {
		'content' : result,
		'date' : date
		}

	

@app.route('/users/<int:user_Id>/diaries')
def delete_diary( user_id) :
    # diary = user_id 중 date 에 맞는 diary 삭제
    date = request.args.get('date')
    connection = get_connection()
    cursor = connection.cursor
    delete_query = '''
	DELETE FROM diaries WHERE user_id=%d AND date=%s
	'''
    diary_id = cursor.last_row_id
    return {
		'lastest_diary_id ' : diary_id
		}

  

# 3. 공지사항----------------------------------------------------------------------
# notice table : 어떤 속성 사용할지 : ex) notice_id, user_id, date, content, tag
'''
@app.route('/notice')
def get_notice():
    # 모든 공지사항 가져오기

@app.route('/')
def post_notice():
    # 공지사항 올리기

@app.route('/')
def update_notice():
    # 공지사항 수정 

@app.route('/')
def delete_notice():
    #공지사항 삭제
'''

if __name__ == '__main__':
    app.run(debug=True)
    
