from flask import Flask, request, jsonify
from utils import*

# import config
app = Flask(__name__)

# 일지 관련----------------------------------------------------------------
# diary table : 어떤 속성 사용할지 : ex) diary_id, user_id, date, content
@app.route('/users/<user_id>/diaries', )
def get_diary(user_id):
    # all_diary = user_id 에 맞는 diary 모두 가져오기
	data = request.get_json()
	connection = get_connection() 
	cursor = connection.cursor()
	query = '''
	SELECT date, content FROM diary WHERE user_id = %s
	'''
	try:
		cursor.execute(query, user_id)
		result = cursor.fetchall()

	diary_list = []

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
	data = request.get_json()

	connection = get_connection()
	cursor = connection.cursor()
	new_diary_id = cursor.last_row_id + 1
	new_diary = (user_id, new_diary_id, data["date"], data["content"])

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
	values = (data["content"] , user_id, data["date"])
	cursor.execute(update_query, values)

	cursor.close()
	connection.close()

	return{
		"message" : "update successfully",
		}

@app.route('/users/<int:user_id>/diaries')
def get_diary_by_date(user_id):
	date = request.args.get('date')
    # diary = user_id 중 date 에 맞는 diary 가져오기
	connection = get_connection()
	cursor = connection.cursor()
	select_query = '''
	SELECT content FROM diaries WHERE user_id = %s AND date=%s
	'''
	values = (user_id, date)
	cursor.execute(select_query, values)
	result = cursor.fetchone()

	cursor.close()
	connection.close()

	return {
		'content' : result,
		'date' : date
		}

	

@app.route('/users/<int:user_Id>/diaries')
def delete_diary(user_id) :
    # diary = user_id 중 date 에 맞는 diary 삭제
    date = request.args.get('date')
    values = (user_id, date)
    connection = get_connection()
    cursor = connection.cursor
    delete_query = '''
	DELETE FROM diaries WHERE user_id=%s AND date=%s
	'''
    cursor.execute(delete_query, values)
    diary_id = cursor.last_row_id
    cursor.close()
    connection.close()
    return {
		'lastest_diary_id ' : diary_id
		}

  




