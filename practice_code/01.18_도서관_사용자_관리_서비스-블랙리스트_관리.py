black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]
def censorship(censored_userlist):
    New = list(censored_userlist.items())
    x,y = New[0][0],New[0][1][0]
    if x in black_list:
        print(f'{x}소속의 {y}은/는 등록할 수 없습니다.')
        return(False)
    else:
        print('이상 없습니다.')
        return(True)

def create_user(parsed_data):
    censored_userlist ={}
    censored_userlist[parsed_data['company']['name']] = [parsed_data['name']]
    TF = censorship(censored_userlist)
    if TF:
        return censored_userlist

import requests

Lst = []
# 무작위 유저 정보 요청 경로
for i in range(1,11):
    A ='https://jsonplaceholder.typicode.com/users/'+str(i)
    API_URL = A
# API 요청
    response = requests.get(API_URL)
# JSON -> dict 데이터 변환
    parsed_data = response.json()
    censored_user_list = create_user(parsed_data)
    if censored_user_list:
        Lst.append(censored_user_list)
for  i in Lst:
    print(i,end='')

    
