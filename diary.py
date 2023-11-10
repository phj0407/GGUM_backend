from flask import Flask, request, jsonify
from utils import*

# import config
app = Flask(__name__)

@app.route('/diary/<string:date>', methods=['GET', 'POST'])
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

        return diary_list

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
            "message": "diary created successfully",
            "diary_id": new_diary_id
        }

@app.route('/diary/<date>/<int:user_id>', methods =[ 'PUT', 'DELETE'])
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
            "message": "update successfully",
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
            'msg': 'data deleted successfully'
            }

if __name__ == '__main__':
    app.run(debug=True)







