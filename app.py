from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return 'home_page'

# 회원정보 ------------------------------------------------------------------
# user table : 어떤 속성 사용할지 : ex) user_id, student_id, user_name, generation
@app.route('/login')
def login():

    #     user_id = DB에서 회원조회


@app.route('/sign_in', methods=['POST'])
def sign_in():

 #   DB에 정보 등록 (이름, 학번, 기수)
 #     new_user_id = 제일 최신 user_id 가져와 +1


# 일지 관련----------------------------------------------------------------
# diary table : 어떤 속성 사용할지 : ex) diary_id, user_id, date, content
@app.route('/')
def get_diary():

    # all_diary = user_id 에 맞는 diary 모두 가져오기
  

@app.route('/')
def post_diary():

    #new_diary 를 DB에 추가
    #new_diary_id = 최신 diary_id +1


@app.route('/')
def get_diary_by_date():
    # diary = user_id 중 date 에 맞는 diary 가져오기
  

@app.route('/')
def delete_diary( );
    # diary = user_id 중 date 에 맞는 diary 삭제
  

# 3. 공지사항----------------------------------------------------------------------
# notice table : 어떤 속성 사용할지 : ex) notice_id, user_id, date, content, tag
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
    #공지사항 삭ㅈ[

if __name__ == '__main__':
    app.run(debug=True)
    
