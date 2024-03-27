# 장고 복습 시트

- CRUD

    >소프트웨어가 가지는 기본적인 데이터 처리 기능

    > 저장,조회,갱신,삭제

- 프로젝트 생성 루틴

    > python -m venv venv

    > source venv/Scripts/activate

    > pip install -r requirements.txt

    >(pip freeze > requirements.txt)

    > touch .gitignore

- 생성

    > django-admin startproject 이름 .

    >> .이 없으면 manage.py가 안으로 드감

    > python manage.py startapp 이름

- 실행

    > python manage.py runserver

- 앱 사용 순서

    1. 앱 생성

        > python manage.py startapp 이름(이름은 복수형 권장)

    2. 앱 등록

        > 프로젝트 setting.py 들어가서 INSTALLED_APPS 에 등록

- 요청과 응답

    1. URLs

        1. project의 urls.py

            > from app의 이름 import views

            > path('index/', views.index),

            >> http://127.0.0.1:8000/index/ 형식으로 드감

            >> views.index는 경로

            >> 'index/<int:num>'/ or 'index/<str:name>' 같은 형식으로 여러 페이지 만들기 가능

            >>> 단, view,py def index(request,num)로 변수를 받아야함

        2. app의 urls.py

            > 다른 app에서 같은 이름의 index가 나오면 혼동

            > 따라서 url을 각자 app에서 관리

            > project urls.py

            ```
            from django.urls import path,include
            # include 설치

            path('articles/',include('articles,urls')),
            # path('index/','articles.views.index')를 변형하여 articles붙은건 articles.urls에서 하도록 변경
            ```

            > app urls.py

            ```
            from . import views
            path('index/',views.index),

            ```

            **이럴 경우 주소가 변경되어 모든 위치를 찾아가 변경해야함**
            **따라서 밑의 방법을 이용**

        3. app의 urls.py(URL이름 버전)

        > app urls.py

         ```
            from . import views
            
            app_name = 'articles'
            path('index/',views.index,name="index"),
        ```

        > app_name과 name을 설정(성과 이름이라고 생각하면 편함)

        > index.html

        ```
        {% url "articles:dinner" %}
        #이런식으로 가르켜주면 됨
        {% url "articles:dinner" 변수명1 %}
        # 추가 인수가 필요한 경우
        ```





    2. views

        1. app의 view

            > 특정 경로에 있는 template와 request 객체를 결합해 함수 정의

            ```
            def index(request):     # 매개변수는 왠만하면 request
                return render(request,'articles/index.html')
                # (변수,주소)
                # 주소는 template 밑에 articles 밑에 index.html를 읽어라
            ```

**데이터 흐름에 따라 코드를 작성하라(URLs -> Views -> Template)**

- HTML의 콘텐츠를 변수 값에 따라 바꾸기

    1. views의 함수를 수정
    
    ```
    def index(request):
        context = {
            'name' : 'Alice'
        }
        return render(request,'articles/index.html',context)
        # context 안에 함수를 html에서 사용 가능
        # 이후 html에서 {{name}}으로 사용
        # 딕셔너리 형태로 데이터를 사용
    ```

    2. html 수정

    ```
    {{name}} 이런 식으로 사용
    {{name|length}} 같이 파이썬 처럼 사용 가능

    for 함수
    {% for 변수 in 리스트 %}{% endfor %}

    if 함수
    {% if  %}
    {% else %}
    {% endif %}
    ```

- 템플릿 상속

    ```
    1.부모
        {% block content %}
        {% endblock content %}
        ! 이후 body에 그냥 저렇게 적음 content는 걍 이름

    2.자식
        {% extends "부모의 주소 ex base.html" %}
        {% block content %}
            여기에 html 적음
        {% endblock content %}
    ```

- 요청과 응답

    > form

    ```
    <form action="#" method="GET">
        <input type="text" name = "message" id = "message">
        <input type="submit" value = "submit">
    </form>

    # text부분에 적을 수 있는 네모 상자가 나옴
    # submit에 제출 버튼이 나옴
    ```

    > name속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근할 수 있음

    >> name 사용시 http://127.0.0.1:8000/search/?message=input값 으로 나타남

    > action은 어디로 보낼지(URL), method는 어떻게 보낼 지(GET or POST)

    > input type 속성 값에 따라 다양한 유형의 입력 데이터 받음

    > id는 input이 여러개일 경우, 판별해주는 꼬리표(CSS에서 사용)

- Query string parameters

> 기존 url + ? + 다음에 오는 것들이 쿼리 스트링

> ? 기존과 쿼리 스트링 구분은 ?로 구분

> key=value 형태(ex.order=seq)

> 여러개 보내고 싶으면 & 사용(ex.order=seq&skill=python)

- 장고 Model

> 테이블 구조를 설계하는 청사진

```
class 클래스이름(models.Model):
    열의 이름 = models.타입종류(제약조건)
```

> CharField(max_length=) 길이제한 문자열

> TextField() 글자수 많은 문자열

> DateTimeField() 날짜와 시간

>> auto_now 데이터 저장마다 저장

>> auto_now_add 데이터가 처음 생성될 때만 저장

- Migrations

> model 클래스의 변경사항을 DB에 최종 반영하는 방법

> model class(설계도 초안) -> (makemigrations) -> migration 파일(최종 설계도) -> (migrate) -> db

```
python manage.py makemigrations
python manage.py migrate
```

> 최종 테이블 이름은 앱이름_모델클래스이름으로 합성해서 만듬

> 기타 명령어(showmigrations,sqlmigrate 파일 이름)

- 이미 생성된 테이블에 필드 추가

> 1번 기본값 입력 ,2번 대화 나간 후 기본값 설정

> 그 후, 엔터 -> 장고가 제안하는 기본 값

> 이 후, migrations에 설계도가 쌓임

- Admin site

> 슈퍼관리자 계정 만들기

1. 계정 생성

``python manage.py createsuperuser``

2. 권한 주기

    - app admin.py

    ```
    from .models import 클래스모델명

    admin.site.register(모델명)
    # admin site에 모델파일의 클래스를 등록한다
    ```