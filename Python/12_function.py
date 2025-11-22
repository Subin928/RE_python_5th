'''
함수 (function)
- 특정 작업을 수행하는 코드들의 모음
- 복잡한 코드를 작은 단위로 나눌 수 있게 도와줌
- 특정한 코드들을 재사용 할 수 있게 함
'''

# 사용자 정의 함수 기본 문법
# 함수의 정의 : define의 약자로 def 사용
def 함수이름 (매개변수):
    # 실행할 코드
    print(매개변수)
    return "반환값"

# 함수의 실행(호출 call)
함수이름("인자") # 인자 -> 왜 인자냐면 값을 매개변수로 넣어주고 매개변수가 print된것이기 때문

result = 함수이름("인자")
print(result) # 반환값

# 매개 변수 (Parameter) : 매개 + 변수
# 매개 : 둘 사이를 연결해줌
# 함수가 실행될 때 인자로부터 입력되는 값을 함수의 코드블록으로 전달하는 역할


# 함수의 필요성 예제
a = 10
b = 20

if a > b:
    print(a - b)

else:
    print(a + b)

c = 30
d = 40

if c > d:
    print(c - d)

else:
    print(c + d)

# ......

# a와 b, c와 d 경우가 같아 보임 -> 기능은 똑같지만 안의 내용(숫자)만 바뀜 -> 함수

def my_func(a,b):
    if a > b:
        return a - b
    else:
        return a + b
    
print(my_func(10,20)) # 30
print(my_func(30,40)) # 70

# 실습 1. 사칙연산 계산기 함수 만들기

# 문제 1. 사칙연산 계산기 함수 만들기
# 두 개의 숫자와 연산자를 인자로 받아, 해당 연산 결과를 반환하는 함수를 작성하세요.
# 요구사항
# 함수 이름은 calculate로 합니다.
# 매개변수는 a, b, operator 세 개입니다.
# operator는 문자열이며, 다음 중 하나입니다:"+","-","*","/"
# 나눗셈은 결과를 실수(float)로 반환합니다.
# 올바르지 않은 연산자가 들어오면 "지원하지 않는 연산입니다"라는 문자열을 반환하세요.

def calculate(a, b, operator):
    if operator == "+":
        return a + b
    
    elif operator == "-":
        return a - b
    
    elif operator == "*":
        return a * b
    
    elif operator == "/":
        return float(a / b)
    
    else:
        return "지원하지 않는 연산입니다"
    
print(calculate(20,30,"+")) # 50
print(calculate(20,30,"-")) # -10
print(calculate(20,30,"*")) # 600
print(calculate(20,30,"/")) # 0.66666..
print(calculate(20,30,"&")) # 지원하지 않는 연산입니다
    

# 키워드 인자
# 예시 1.
print("안녕하세요", "반갑습니다!", sep = "-", end = " / ") # 안녕하세요-반갑습니다! /

# 예시 2.
def my_func(a, b, c=None, operator=None):
    if operator == "+":
        return a + b
    else:
        return c

# operator는 따로 명시해서 넣어야 함
print(my_func(10, 20, c=999, operator="+"))  # 30
print(my_func(10, 20, c=999, operator="-"))  # 999

# 기본값 인자
# 단, 기본값 매개변수는 뒤쪽에 위치해야함
def greet(name, message="안녕하세요~!"):
    print(f"{name}님, {message}")

# 호출 시 인자 생략 -> 기본값 사용
greet("Luna") # Luna님, 안녕하세요~!
greet("ff", "반갑습니다!") # ff님, 반갑습니다!

# 위치 가변 인자
# 여러개의 값을 유동적으로 받을 수 있음
# 값이 튜플 형태로 받아짐

def add_all(*args):
    return sum(args)

print(add_all(1,2,3,4,5)) # 15

# 키워드 가변 인자
# 여러 키워드 인자를 유동적으로 받을 수 있다
# 딕셔너리 형태로 값이 입력됨

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_info(name = "luna", age=15, city= "seoul") # name : luna
                                                 # age : 15
                                                 # city : seoul

# 실습 2. 가변인자 연습하기
# *args 사용 연습

# 문제 1. 숫자 여러 개의 평균 구하기
# 숫자를 몇 개든 받을 수 있는 average() 함수를 만들어보세요.

def average(*args):
    # 예외처리
    if len(args) == 0:
        return "입력값이 없습니다"
    return sum(args) / len(args)

print(average(1,2,3,4,5)) # 3.0

# 문제 2. 가장 긴 문자열 찾기(max 함수에 대해 찾아보고 풀기)
# 여러 개의 문자열을 받아, 가장 긴 문자열을 반환하는 함수를 만들어보세요.

def long_word(*args):
    return max(args, key=len)
print(long_word("apple","banana","kiwi","strawberry")) # strawberry


# 정답

# 1)
def longgest(*args):
    answer = ""
    for s in args:
        if len(s) > len(answer):
            answer = s
    return answer
print(longgest("apple","banana","kiwi","strawberry")) # strawberry

# 2) - max 이용하기

def longgest2(*args):
    # 예외처리
    if len(args) == 0:
        return "입력값이 없습니다"
    return max(args, key=len)

print(longgest2("apple","banana","kiwi","strawberry")) # strawberry



# **kwargs 사용 연습

# 문제 3. 사용자 정보 출력 함수
# 사용자의 이름, 나이, 이메일 등의 정보를 받아 출력하는 함수를 **kwargs로 구현하세요.
# 정보가 몇 개가 들어오든 모두 출력해야 합니다.

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name = "bin", age =20, email="bin@naver.com")
# name: bin
# age: 20
# email: bin@naver.com

# 문제 4. 할인 계산기
# 상품 가격 목록을 **kwargs로 받아, 각각 10%씩 할인된 가격을 출력하는 함수를 작성하세요.

def discount_prices(**kwargs):
    for key, value in kwargs.items():
        discounted = value * 0.9
        print(f"{key}: 할인가 {discounted} (원가 {value})")

discount_prices(apple=3000, banana=2000, strawberry=4000)

# apple: 할인가 2700.0 (원가 3000)
# banana: 할인가 1800.0 (원가 2000)
# strawberry: 할인가 3600.0 (원가 4000)



# 전역 변수 : 함수 밖에 선언된 변수
# 지역 변수 : 함수 안에 선언된 변수

# 전역변수
x = 200

# 예제
def my_func():
    # 지역변수
    x = 10
    print(x) # 10

my_func()
print("함수 밖", x) # 200


# 예제 2 (UnboundLocalError 에러)
x = 10

def my_func2():
    # x = 20 -> 주석처리하니까 UnboundLocalError나타남
    x += 5
    print("지역변수",x) # 지역변수 25

my_func2()

print("전역변수", x) # 전역변수 10

# 예제 3 (global 사용 예제)
x = 10

def my_func3():
    global x # 전역변수 사용 선언
    x += 5
    print("지역", x) # 지역 15

my_func3()

print("전역", x) # 전역 15



# 권장되는 패턴
# 부수효과(side effect)를 발생시키지 않는 함수를 위주로 프로그래밍

x = 10

def my_func4(x):
    x += 5
    return x

x = my_func4(x)

print("전역", x) # 전역 15

# 실습 3. 전역 변수 연습하기

# 로그인/로그아웃 전역 상태 관리
# 전역 변수로 로그인한 사용자 저장 및 로그아웃 기능을 구현해 봅시다.
# 요구사항
# 전역 변수 current_user는 로그인한 사용자의 이름을 저장합니다.
# login(name) 함수는 사용자를 로그인시키고, logout() 함수는 로그아웃 상태로 만듭니다.
# 이미 로그인된 상태에서 다시 로그인하면 "이미 로그인되어 있습니다"를 출력합니다.
# 로그아웃하지 않고 로그인을 여러 번 시도할 수 없도록 합니다.

current_user = None

def login(name):
    global current_user
    if current_user is not None:
        print("이미 로그인되어 있습니다")

def logout():
    global current_user
    if current_user is None:
        print("로그아웃되었습니다")

    else:
        print("로그아웃되었습니다")
        current_user = None

# 정답

current_user = None
login_count = 0

def login(name):
    global current_user
    global login_count

    if current_user == None:
        current_user = name
        print(f"{name}님 로그인 성공!")
    else:
        print("이미 로그인되어 있습니다.")
        login_count += 1
        if login_count > 4:
            print("더 이상 로그인 시도를 할 수 없습니다.")

def logout():
    global current_user
    global login_count

    if current_user == None:
        print("로그인 상태가 아닙니다.")
    else:
        print("로그아웃 되었습니다!")
        current_user = None
        login_count = 0

login("Ian")
login("CodingOwl")
logout()
login("CodingOwl")
print(current_user)





# 재귀함수
# 1. 자기 자신을 호출하는 함수
# 2. 반드시 기본 조건 (종료 조건)이 있어야 함
# - 큰 문제를 작은 문제로 나누었을 때 일정한 패턴이 있어야 함

import time

def recursive_func(n):
    # 기본 조건
    if n == 0:
        return 
    
    recursive_func(n-1)
    print("재귀 호출", n)
    time.sleep(1)

recursive_func(5) # 재귀 호출 1
                  # 재귀 호출 2
                  # 재귀 호출 3
                  # 재귀 호출 4
                  # 재귀 호출 5

# 실습 4. 거듭 제곱
# 자연수 a와 b가 주어졌을 때, a와 b 제곱을 계산하는 재귀 함수를 만들어 봅시다.
# 거듭 제곱은 다음과 같이 정의됩니다.
# a^b = a * a^(b-1)

def power(a, b):
    if b == 0:
        return 1
    
    return a * power(a, b-1)

print(power(2,4)) # 16 (2*2*2*2*1)=>b=4에서 b=0이 되는 순간까지 포함 총 5개 곱

# 실습 5. 팩토리얼(Factorial)
# 1. 먼저 반복문을 활용해서 팩토리얼을 구현합니다.
# 2. 1번을 바탕으로 작동 원리를 파악하고, 재귀함수를 이용해서 팩토리얼을 구현합니다.
# 3. 디버거를 이용해 재귀함수의 작동을 확인합니다.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5)) # 120

# 정답

# 1) 반목문으로 구현
def factorial_for(n):
    # 예외처리
    if n < 0:
        return "음수의 팩토리얼은 정의되지 않습니다."
    
    result = 1

    for i in range(1,n+1):
        result


# 2) 재귀함수

def factorial_rec(n):
    # 예외처리
    if n < 0:
        return "음수의 팩토리얼은 정의되지 않습니다."
    
    # 기본조건
    if n == 0 or n == 1:
        return 1
    
    return n * factorial_rec(n-1)

print(factorial_rec(5)) # 120


# 실습 6. 피보나치 수열
# 1. 먼저 반복문을 활용해서 피보나치 수열을 구현합니다.
# 2. 1번을 바탕으로 작동 원리를 파악하고, 재귀함수를 이용해서 피보나치 수열을 구현합니다.
# 0 이하의 수가 입력될 시 0을 리턴

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

# 정답

# 1) 반복문

def fibonacci_for(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a,b = 0,1
    for _ in range(n-1):  # _는 반복만 하고 반복 변수를 안 쓸 때
        a,b = b,a+b
        # 0 1 = 1 1
        # 1 1 = 1 2
        # 1 2 = 2 3

    return b

print(fibonacci_for(6)) # 8

# 2) 재귀함수

def fibonacci_rec(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

print(fibonacci_rec(6)) # 8



### 람다 (lambda) 함수
# 익명 함수
# 간단한 함수를 한줄로 표현할 때 사용

# 람다 함수의 기본 문법
# # lambda 매개변수: 표현식
# - 표현식 : 값이 반환되는 식

# 일반 함수
def add(x, y):
    return x + y

# 람다 함수
add_func = lambda x, y: x + y
print(add_func(3, 5)) # 8

# 람다로 값을 반환하고 사용을 끝내는 경우
(lambda x: x ** 2)(10)
print((lambda x: x ** 2)(10)) # 100


# 람다 함수의 활용
# 1. map에서 활용
my_list = [1,2,3,4]

# 일반 함수를 사용
def square_func(x):
    return x ** 2

# 함수를 인자로 받는 함수
map(square_func, my_list)
print(map(square_func, my_list)) # <map object at 0x0000029085F1BC10>
print(list(map(square_func, my_list))) # [1, 4, 9, 16]

# 람다함수를 사용
print(list(map(lambda x: x ** 2, my_list))) # [1, 4, 9, 16]



# 2. filter에서 활용
my_list2 = [1,2,3,4,5,6,7,8,9,10]

# 일반 함수 사용
def is_even(x):
    return x %2 == 0

print(list(filter(is_even, my_list2))) # [2, 4, 6, 8, 10]

# 람다함수를 사용
print(list(filter(lambda x: x % 2 == 0, my_list2))) # [2, 4, 6, 8, 10]

# 3. sorted에서 활용
my_list3 = ["apple", "banana", "watermelon", "grape"]
sorted(my_list3, key=lambda word: len(word))
print(sorted(my_list3, key=lambda word: len(word))) # ['apple', 'grape', 'banana', 'watermelon']

# 실습 7. 람다 함수 연습 문제(1)

# 문제 1. 특정 조건 만족하는 튜플만 추출
# 아래 학생 튜플 리스트에서 평균 점수가 70점 이상인 학생만 추출하세요
# students = [("Alice", [80,90]),("Bob",[60,65]),("Charlie",[70,70])]

students = [
    ("Alice", [80,90]),
    ("Bob",[60,65]),
    ("Charlie",[70,70])
]

score = list(filter(lambda x: sum(x[1])/len(x[1]) >= 70, students))
print(score) # [('Alice', [80, 90]), ('Charlie', [70, 70])]


# 문제 2. 키워드 추출 리스트 만들기
# 아래와 같은 문자열 리스트가 있을 때, 각 문장에서 맨 앞 단어만 추출한 리스트를 만들어보세요.
# sentences = ["Python is fun","Lambda functions are powerful","Coding is creative"]

sentences = ["Python is fun",
             "Lambda functions are powerful",
             "Coding is creative"]

first_word = list(map(lambda s: s.split()[0], sentences))
print(first_word) # ['Python', 'Lambda', 'Coding']

# 문제 3. 튜플 리스트 정렬하기
# 이름과 나이로 구성된 튜플 리스트를 나이를 기준으로 오름차순 정렬하세요.
# people = [("Alice",30),("Bob",25),("Charlie",35)]

people = [
    ("Alice", 30),
    ("Bob", 25),
    ("Charlie", 35)
]

sorted_people = sorted(people, key=lambda person: person[1])
print(sorted_people) # [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
