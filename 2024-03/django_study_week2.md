# 장고 복습 시트 5일차

## QuerySet Api

> orm에서 데이터를 만질때 사용하는 도구

> 구조

>> Model class.Manage.QuersetAPI(Article.objects.all())

### Query

> DB에 특정한 데이터를 보여달라는 요청

> 파이썬으로 작성된걸 보내면 QuerySet라는 자료형태로 나한테 전달

### QuerySet

> 데이터 모음

> 반환시 Class의 인스턴스로 반환

### 장고 shell

> 장고 환경 안에서 실행되는 파이썬 쉘(번역기 및 해석기)

> 실행시 ``python manage.py shell_plus``

### QuerySet API 조회 메서드

> all()

> filter()

>> Modelclass.Manage.filter(열이름:'특정값')

```
Field lookups

# content 칼럼에 'dja'가 포함된 모든 데이터 조회
Article.objects.filter(content__contains) = 'dja')
```

>>> 빈값 or 찾아줌

> get()

### 데이터 객체를 만드는 3가지 방법

1. 특정 테이블에 새로운 행을 추가하여 데이터 추가

```
article = Article() # Article(class)로부터 article(instance) 생성

# save를 하지 않으면 아직 DB에 값이 저장되지 않음
    # article = Article()
    # <Article: Article object (None)>
    # Article.objects.all()
    # <QuerySet[]>

article.title = 'first'
article.content = 'django!'
```

2. 두 줄로 쓰기

``article = Article(title='second',content='django!')``

> 이후 저장

3. 한 줄 쓰기

``Article.object.create(title='third',content='django!')``

### 데이터 수정

1. 수정할 인스턴스 조회(pk)

``행이름 = 모델클래스.Manage.get(pk=1) ``

2. 인스턴스 변수를 변경

``행이름.열이름 = '변경할 거'``

3. 저장

``행이름.save()``

### 데이터 삭제

1. 수정할 인스턴스 조회(pk)

``행이름 = 모델클래스.Manage.get(pk=1) ``

2. 인스턴스 변수를 변경

``행이름.delete()'``

---

# 장고 복습 시트 6일차

> 지금까지 연습한 것을 view함수에서 사용하자

## HTTP

> 네트워크 상에서 데이터를 주고 받기 위한 약속

> HTTP request methods(GET,POST)

> GET

>> 데이터 전달 시 Query String 형식

> POST

>> 변경(생성,수정,삭제)을 요구하는 요청, 데이터 전달 시 HTTP Body에 담김

### HTTP response status code

- 403 Forbidden

    > 권한 거절

    > CSRF(사이트 간 요청 위조) - > {% csrf_token %}

    > Django가 직접 제공한 페이지에서 요청 보낸 것인지 인증 토큰 발행

- redirect()

    > 사용자가 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수

    > 데이터 저장 후 페이지를 주는 것이 아닌 다른 페이지로 사용자를 보내야함

    > 사용자 -> create -> 서버가 redirect -> 사용자가 다시 다른 곳으로 요청 -> 서버가 그곳을 보넴

    > 따라서 사용자는 create 이후 다른 곳으로 바로 이동하는 느낌을 받는 것


- Delete

```
articles/urls.py

path('<int:pk>/delete/', views.delete,name ='delete')

views.py

def delete(requset,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article:index')

detail.html
<form action ="{%url 'articles:delete' article.pk %}" method ='POST'>
{%csrf_token%}
<input type='submit' value='delete'>
</form>
```

- update

    > urls.py는 다 같음
    
    ``path('<int:pk>/update/', views.update,name ='update')``

    > views.py return 에서 article.pk 보내줌

    ```
    article = Article.objects.get(pk=pk)
    return redirect('articles:detail',article.pk)
    ```

    ---

    # 장고 복습 7일차

    ## 장고 폼

   > as_div,as_table,as_p,as_ul 지원 

   ## 위젯

   > input의 표현을 담당

   > form.py에서 디자인을 담당

   ## 장고 모델 폼

   > Form(DB에 저장하지 않을 때) vs ModelForm(DB에 저장)

   ```
   class 이름(form.ModelForm):
    class Meta:
        model = 'model이름'
        fields = '__all__'
        # fields = ('title','content') #그 모델에서 어떤 필드를출력할 껀지
        # exclude = ('title') 이런식으로 전체에서 지워주는 형식도 가능
   ```

   > 두가지 함수 합치기

    ```
   def new(request):
    form = ArticleForm()
    context = {
        'form':form,
    }
    return render(request, 'articles/new.html',context)

    def create(request):
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    
    context =  {
        'form':form,
    }
    return render(request,'articles/new.html',context)

    >>> 하나로 합치기

    def create(request):
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail',article.pk)
        else:
            form = ArticleForm()
        context = {
            'form':form,
        }
        return render(request,'articles/create.html',context)
    ```


