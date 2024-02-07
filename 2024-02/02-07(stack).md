# stack (중요)

## stack의 특성

- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조

- 스택에 저장된 자료는 선형 구조

    > 선형 구조: 자료 간의 관계가 1대 1의 관계

    > 비 선형 구조: 자료 간의 관계가 1대 N의 관계(예:트리)

- 후입선출 구조(LIFO)

## stack을 위해서 필요한 자료구조와 연산

- 자료 구조: 자료를 선형으로 저장할 저장소

    > 배열 사용 가능

    > 저장소 자체를 스택이라 부름

    > 스택에서 마지막 삽입 원소를 top

- 연산

    > 삽입: 저장소에 자료를 저장, append 사용(push)

    > 삭제: 저장소에서 자료를 꺼냄. 삽입의 역순인 후입선출(pop)

    > 스택이 공백 유무(isEmpty)

    > 스택의 top에 있는 원소 반환하는 연산(peek)

## stack의 구현

```
def push(n):
    global top
    top += 1
    if top == size:
        print('Overflow')
    else:
        stack[top] = n

top = -1
size = 10
stack = [0]*size

top += 1            # push(10)
stack[top] = 10

top += 1            # push(20)
stack[top] = 20

push(30)

while top >= 0:
    top -= 1
    print(stack[top+1])
```

---

# stack의 응용

## stack 구현의 고려 사항

> 1차원 배열은 구현은 용이하지만, 스택 크기 변경하기가 어려움

> 해결을 위한 방법으로 저장소를 동적으로 할당, 구현 복잡하지만, 메모리 효율적인 사용

## stack의 응용의 예시 : 괄호검사

## stack의 응용의 예시 : function call

### Function call

> 프로그램에서의 함수 호출과 복귀에 따른 수행 순서를 관리

> 후입선출을 이용하여 수행 순서 관리

> 함수 호출 발생 시, 필요한 지역변수, 매개변수 및 수행 후 복귀 주소등 스택 프레임에 저장하여 시스템 스택에 삽입

> 함수의 실행이 끝나면 top원소를 삭제하면서 복귀주소 확인 후 복귀

> 전체 프로그램 수행 종료시, 공백 스택 됨

---

# 재귀 호출

> 필요한 함수가 자신과 같은 경우 자신을 다시 호출하는 구조

> 재귀호출 방식을 사용하면 프로그램 크기를 줄이고 간단하게 작성

## 재귀 호출의 예시 : 피보나치

```
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
    
    
fibo(int(input()))
```

---

# Memoization

> 메모이제이션(Memoization)은 프로그램 실행할 때 이전에 계산 한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행 속도를 빠르게 하는 기술

> 동적 계획법의 핵심이 되는 기술

## 재귀 호출의 문제점

> 엄청난 중복 호출 존재

![중복호출](https://github.com/Demopeu/TLI/assets/156268475/59844585-3b30-48bf-b9d1-fbb4ad0902e5)

> 메모이제이션을 이용하면 실행시간을 O(n)으로 줄일 수 있음

```
def fibo(n):
    global memo
    if n>=2 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

n = int(input())
memo = [0]*(n+1)
memo[0] = 0
memo[1] = 1
print(fibo(n))
```