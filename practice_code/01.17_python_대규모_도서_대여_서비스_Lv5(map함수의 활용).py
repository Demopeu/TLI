def create_user(name,age,address):
    print(name+"님 환영합니다 !")
    user_info = {}
    user_info['name'] = name ; user_info['age'] = age ; user_info['address'] = address ; 
    return user_info
    
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user,name,age,address))

info = list(map(lambda x:(x['name'],x['age']),many_user))

def rental_book(info):
    for i in range(len(info)):
        name = info[i][0]
        number = info[i][1]
        number //= 10
        decrease_book(number)
        print(f"{name}님이 {number}권의 책을 대여하였습니다.")

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print('남은 책의 수 :',number_of_book)
    

number_of_book = 100

rental_book(info)