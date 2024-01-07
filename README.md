# user
### '/users'
```
[GET] login() 
{
	student_number : 
	password:
}
```
```
 [POST] sign_in()
{
	name:
	student_number : 
	cohort:
	password:
}
  
```
# diary
### '/diaries/ { string : date }'
```
[GET]  해당 날짜에 등록된 diary 의 {id, title, user_name} 을 반환
return {
                "diary_id" : id,
                "title" : title,
                "user_name" : user_name,
            }
```
```
[POST] new_diary 를 DB에 추가하고 새로 생성한 diary의 id를 반환

request {
	user_id :
	title:
	content:
}
return {
            "message": "diary created successfully",
            "diary_id": new_diary_id
        }
```
  
### '/diaries/ { string : date }/{ int : user_id }'
```
[PUT] 특정 날짜에 특정 사용자가 작성한 diary 내용을 수정
request {
	id: #수정할 diary 선택
	user_id: #작성자만 수졍 가능하도록
	title:
	content:
}
return{
            "message": "update successfully",
            }
```
```
[DELETE]  특정 날짜에 특정 사용자가 작성한 diary를 삭제
return {
            'msg': 'data deleted successfully'
            }
```
  
# notice
### '/notices'
[GET] 최근 n개 공지를 반환, , http://127.0.0.1:5000/notice?count=n 꼴로 요청
```
[POST]
request {
	user_id: 
	title :
	content :
}
return {
        "notice_id": notice_id
    }
```
  
### '/notices/{ int : notice_id }'
```
[PUT]
request {
	user_id : # 작성자만 수정 가능하도록 확인 위함 
	title : 
	content :
}
	#last_edit_at 업데이트 필요

return{
	'msg' : '사용자가 일치하지 않습니다 / 수정 성공'
}
```
```
[DELETE]
request {
	user_id: #작성자만 삭제 가능하도록 확인
}
return{
	'msg' : '사용자가 일치하지 않습니다 / 삭제 성공'
}
```
  
# survey
### '/surveys'
```
[POST]
request {
        'survey_date':
        'user_id':
        'title': 
        'description'
}
return {
        'msg': msg,
        'id': new_id
    }
```
```
[GET] 활성화중인 survey를 로드
return {
        'id' 리스트
}
```

### '/surveys/ { int : survey_id }'
```
[GET] 해당 survey의 정보를 로드
return {
        'survey date': date,
        'title': title,
        'desc': desc,
    }
```

```
[PUT] 투표 게시글 수정
request{
        'survey_date':
        'user_id':
        'title': 
        'description'
        'isactive'
중 수정 원하는 항목
}
```

```
[DELETE] 투표 게시글 삭제
request {
        'user_id':
}
```
  

### '/surveys/ { int : survey_id } /participant'
```
[POST] survey에 attendee 등록
request { 'attendee_id' }
return { 'msg' } 

[GET ] 해당 survey에 참석한 attendee를 로드
{ id 리스트}

[DELETE] 투표취소
request { 'attendee_id' }
return { 'msg' } 
```
