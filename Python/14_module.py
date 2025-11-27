# 모듈 (module)
# - 여러 기능(함수)의 묶음
# - 하나의 py파일로 여러 기능을 모아놓은 것


# 모듈 불러오기(1)
# import hello

# 모듈 불러오기(2)
from hello import greeting
# 모듈 불러오기(3)
from hello import *
# 모듈 불러오기(4)
import hello as h

# hello.greeting("lee")
greeting("kim") # Hello, kim!
introduce("sin", 20) # 제 이름은 sin이고, 나이는 20입니다
h.greeting("kim") # Hello, kim!



# 실습 1. 계산기 모듈 만들어보기

# 문제 설명
# calc.py라는 파일을 생성하여 사칙연산 함수(덧셈, 뺄셈, 곱셈, 나눗셈)를 각각 구현하세요.
# 함수명: add(a, b), subtract(a, b), multiply(a, b), divide(a, b)
# 같은 폴더에 main.py파일을 생성하고, calc 모듈을 import해서 각 함수의 결과를 출력하세요.

# 요구 사항
# 나눗셈 함수에서는 0으로 나누는 경우 "0으로 나눌 수 없습니다."를 출력하고 None을 반환할 것

# calc.py파일에서

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("0으로 나눌 수 없습니다.")
        return None
    return a / b

# 지금 현재 14_module.py

import calc as c

print(c.add(20, 5))         # 25
print(c.subtract(20, 5))    # 15
print(c.multiply(20, 5))    # 100
print(c.divide(20, 5))      # 4.0
print(c.divide(20, 0))      # 0으로 나눌 수 없습니다. None




# 패키지
# 모듈의 묶음
# 모듈을 폴더 단위로 묶어놓은 것

# 패키지에서 모듈 불러오기(1)
from my_package import calc as c
c.add(10,20)

# 패키지에서 모듈 불러오기(2)
from my_package.calc import add
add(10,20)



# 파이썬 표준 라이브러리

# math 모듈 : 수학적 연산에 사용되는 모듈
import math as m


# 1. 올림/내림
# ceil : 올림, 소수점 지정 X
print(m.ceil(3.14))

# floor : 내림, 소수점 지정 X
print(m.floor(3.14))

# round : 반올림 - 내장 함수
print(round(3.141592, 2))


# 2. 제곱, 제곱근
# pow(x, y) : 제곱 - x^2y
m.pow(2,3)

# sqrt(x) : 제곱근 반환
m.sqrt(16)



# 3. 상수
# pi : 원주율
print(m.pi)


# 4. 수학 계산 편의 기능
print(m.factorial(3))

# 최대 공약수
print(m.gcd(12, 20))
# 최소 공배수
print(m.lcm(12,20))


# 실습 2. math 모듈 사용해보기

# 문제 1. 실제 거리 계산: 좌표 두 점 사이 거리 구하기

# 문제 설명
# 두 점 (x1, y1),(x2, y2)의 좌표를 입력받아 두 점 사이의 실제 거리를 소수 둘째 자리까지 출력하세요.

# 힌트:
# 피타고라스 정리: 거리 = sqrt((x2-x1)^2 + (y2-y1)^2)
# math.sqrt(), math.pow() 함수 활용

import math

x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f"두 점 사이 거리 {distance:.2f}")


# 문제 1. 정답 

import math as m

x1, y1 = map(int, input("x1,y1을 입력해주세요.").split(","))
# x1, y1 = int(x1), int(y1)
x2, y2 = map(int, input("x2,y2을 입력해주세요.").split(","))

dist = round(m.sqrt(m.pow((x2-x1),2) + m.pow((y2-y1),2)),2)

print(f"두 점 사이의 거리는: {dist}")
# x1,y1을 입력해주세요.0,0
# x2,y2을 입력해주세요.3,4
# 두 점 사이의 거리는: 5.0


# 문제 2. 상품 나누기: 최소 공배수와 최대 공약수

# 문제 설명
# 어떤 학급에 학생이 18명, 선생님이 24명 있습니다.
# 두 집단이 모두 공평하게 나눠 가질 수 있는 최대의 간식 개수(최대공약수)와
# 포장 단위별로 동시에 맞게 나누어 떨어지는 최소 간식 개수(최소 공배수)를 구하는 코드를 작성하세요.

# 힌트
# math.gcd(), math.lcm()  

import math as m

s = 18
t = 24

gcd = m.gcd(s, t)
lcm = m.lcm(s, t)

print(f"최대 간식 개수: {gcd}")
print(f"최소 간식 개수: {lcm}")



# random 모듈 : 랜덤 값(난수) 생성 시 사용
import random


# 1. 난수 생성

# random() : 0 이상 1 미만의 float 난수 반환
print(random.random()) # 0.38202563056267214

# uniform(a, b) : a 이상 b 이하의 실수 난수 반환
print(random.uniform(1,10)) # 9.459176913477434

# randint(a,b) : a 이상 b 이하의 정수 난수 반환
print(random.randint(1, 100)) # 25

# randrange(start, stop, step) : 범위 안의 정수 난수 반환, 간격 지정 가능
print(random.randrange(0, 100, 5)) # 80



# 2. 랜덤 선택
fruits = ["apple", "banana", "watermelon", "grape", "orange"]

# choice(seq) : 시퀀스에서 임의의 요소 1개 반환
print(random.choice(fruits)) # grape

# choices(seq, k) : 시퀀스에서 "중복 허용" k개 요소 리스트를 반환
print(random.choices(fruits, k = 2)) # ['banana', 'orange']

# 섞기
# sample(seq, k) : 시퀀스에서 "중복 없이" k개 요소 리슽트를 반환
print(random.sample(fruits, k = 2)) # ['grape', 'apple']

# shuffle(seq) : 시퀀스의 요소를 무작위로 섞음 -> 원본 시퀀스를 변경
numbers = [1,2,3,4,5]
print(random.shuffle(numbers)) # None
print(numbers) # [5, 2, 1, 3, 4]


# 실습 3. 로또 번호 뽑기

# 문제 설명
# 1. 1~45까지의 수 중에서 랜덤으로 6개의 숫자를 뽑는다
# 2. 6개의 숫자 중 중복되는 숫자가 없도록 한다
# 3. 오름차순으로 정렬한 결과를 출력한다

import random

numbers = list(range(1, 46))
random.shuffle(numbers)
lotto = sorted(numbers[:6])
print(lotto) # [1, 11, 12, 22, 37, 40]

# 정답

# 1)
result = sorted(random.sample(range(1,46), k = 6))
print(result) # [5, 21, 24, 36, 40, 44]

# 2)
lotto = []
while len(lotto) < 6:
    number = random.randint(1, 45)
    if number in lotto:
        continue

    lotto.append(number)

lotto.sort()
print(lotto) # [17, 25, 29, 30, 38, 44]

# 실습 4. 가위 바위 보 게임 만들기

# 문제 설명
# 1. 컴퓨터는 '가위', '바위', '보' 중 하나를 무작위로 선택합니다.
# 2. 사용자는 키보드로 '가위', '바위', '보' 중 하나를 직접 입력합니다.
# 3. 둘의 결과를 비교해 승, 무, 패를 판단하여 출력하세요

# 요구 사항
# 1. random 모듈의 함수를 사용할 것
# 2. 사용자 입력은 input()으로 받을 것
# 3. 승패 판정(비교) 로직은 if/elif/else로 직접 구현할것

import random

choices = ["가위", "바위", "보"]
computer = random.choice(choices)

user = input("가위, 바위, 보 중 하나를 입력하세요: ")

print("컴퓨터:", computer)

if computer == user:
    print("무승부")
elif (user == "가위" and computer =="보") or (user == "바위" and computer == "가위") or (user == "보" and computer == "바위"):
    print("승")
else:
    print("패")

# 가위, 바위, 보 중 하나를 입력하세요: 가위
# 컴퓨터: 바위
# 패

# 정답

RPS = ["가위", "바위", "보"]
win_count = 0

while win_count < 3:
    com_choice = random.choice(RPS)
    user_choice = input("가위, 바위, 보 중에 골라주세요!: ")

    print(f"유저의 선택: {user_choice}")
    print(f"컴퓨터의 선택: {com_choice}")

    if user_choice == com_choice:
        print("비겼습니다")

    elif(
        (user_choice == "가위" and com_choice == "보") or
        (user_choice == "바위" and com_choice =="가위") or
        (user_choice == "보" and com_choice == "바위")):
        print("이겼습니다")
        win_count += 1
    elif user_choice in RPS:
        print("졌습니다")
    else:
        print("잘못된 입력이에요")

# 가위, 바위, 보 중에 골라주세요!: 가위
# 유저의 선택: 가위
# 컴퓨터의 선택: 보
# 이겼습니다
# 가위, 바위, 보 중에 골라주세요!: 바위
# 유저의 선택: 바위
# 컴퓨터의 선택: 가위
# 이겼습니다
# 가위, 바위, 보 중에 골라주세요!: 보
# 유저의 선택: 보
# 컴퓨터의 선택: 바위
# 이겼습니다



# datetime 모듈
# 날짜와 시간의 생성, 조작, 현실 변환과 같은 시간 관련 기능을 제공
import datetime

# 1. 날짜/시간 구하기
# 현재 날짜와 시간 구하기
now = datetime.datetime.now()
print(now) # 2025-11-26 10:20:32.165596

# 오늘 날짜만 구하기
today = datetime.date.today()
print(today) # 2025-11-26

# 2. 날짜/시간 형식 변환
formatted = now.strftime("%Y/%m/%d %H:%M:%S")
print(formatted) # 2025/11/26 10:24:18

parsed = datetime.datetime.strptime(formatted, "%Y/%m/%d %H:%M:%S")
print(parsed) # 2025-11-26 10:26:33



# 3. 날짜/시간 연산
dt = datetime.date(2025, 7, 7)
passed_time = today - dt
print(f"{passed_time.days}일이 지났습니다") # 142일이 지났습니다



# 4. 요일 반환 : weekday
# 0 : 월요일 ~ 7 : 일요일
days = ["월", "화", "수", "목", "금", "토", "일"]
day_num = today.weekday()
days[day_num]
print(days[day_num]) # 수


# datetime 또는 date 객체에는 년/월/일 시간 등이 속성으로 들어있음
print(datetime.datetime.now().year) # 2025



# 실습 5. 다음 생일까지 남은 날짜 계산하기

# 문제 설명
# 1. 사용자로부터 생일(월-일, 예: 07-25)을 입력 받으세요.
# 2. 오늘 날짜를 기준으로 올해 또는 내년의 생일까지 남은 날짜(일 수)를 계산해서 출력하세요.
# 올해 생일이 지났으면 내년까지 남은 일수로, 아직 안 지났으면 올해 생일까지 남은 일수로 계산

# 요구 사항
# 날짜 연산에는 반드시 datetime 모듈을 사용할것

import datetime

birthday_input = input("생일을 월-일 형식으로 입력하세요: ")

month, day = map(int, birthday_input.split("-"))

today = datetime.date.today()

birthday_this_year = datetime.date(today.year, month, day)

if birthday_this_year < today:
    birthday_next = datetime.date(today.year + 1, month, day)
else:
    birthday_next = birthday_this_year

days_left = (birthday_next - today).days

print(f"다음 생일까지 {days_left}일 남았습니다!")

# 생일을 월-일 형식으로 입력하세요: 09-28
# 다음 생일까지 306일 남았습니다!


# 정답

birth_month, birth_day = map(int, input("생일을 입력하세요.(예 03-14):").split("-"))

# 오늘 날짜 구하기
today = datetime.date.today()

# 올해 생일을 date 객체로 변환
birthday_this_year = datetime.date(today.year, birth_month, birth_day)

# 오늘 날짜와 올해 생일을 비교
if today > birthday_this_year:
    # 올해 생일이 지났으면 내년으로 설정
    birthday_next = datetime.date(today.year + 1, birth_month, birth_day)

else:
    # 올해로 설정
    birthday_next = birthday_this_year

# 남은 일수 계산
days_left = (birthday_next - today).days

print(f"다음 생일까지 {days_left}일이 남았어요!")



# calendar 모듈
# 날짜와 달력 관련 기능을 제공

import calendar

# 1. 달력 조회
calendar.prmonth(2025,11)
calendar.prcal(2025)

# 텍스트로 값을 반환
print(calendar.month(2025, 11))

# 요일 반환
print(calendar.weekday(2025, 11, 26)) # 2



# time 모듈
# 시간의 측정, 지연, 변환과 같은 시간 관련 기능 제공

import time

# 1. 시간 반환
# time()
# Unix 타임스탬프로 반환 (1970.1.1부터 경과 초)
print(time.time()) # 1764128042.4286494

# ctime() : 현재 시간을 문자열로 반환
print(time.ctime()) # Wed Nov 26 12:34:02 2025
print(time.ctime(0)) # 기준시로 반환(1970.1.1) -> Thu Jan  1 09:00:00 1970


# strftime() : 원하는 포맷의 문자열로 시간 객체 변환
lt = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
print(formatted) # 2025-37-26 12:37:36

# strptime() : 문자열을 struct_time 객체로 변환
parsed = time.strptime(formatted, "%Y-%m-%d %H:%M:%S")
print(parsed) # time.struct_time(tm_year=2025, tm_mon=11, tm_mday=26, tm_hour=12, tm_min=41, tm_sec=24, tm_wday=2, tm_yday=330, tm_isdst=-1)
 


# 2. 시간 지연
# sleep(seconds) : 지정한 초만큼 프로그램이 일시 정지
time.sleep(1)
print("time sleep")



# 시간 측정하기
start = time.time()

for i in range(5):
    print(i)
    time.sleep(1)

end = time.time()
print(f"수행시간 : {end - start: .2f}초")

# 0
# 1
# 2
# 3
# 4
# 수행시간 :  5.00초



# 실습 6. 타자 연습 게임 만들기

# 문제 설명
# 1. 영단어 리스트 중 무작위로 단어가 제시됩니다.
# 2. 사용자는 해당 단어를 정확히 입력해야 다음 문제로 넘어갈 수 있습니다.
# 3. 10문제를 모두 맞히면, 게임이 종료되고 총 소요 시간이 출력됩니다.
# 4. 틀린 경우에는 "오타! 다시 도전!" 메시지를 출력하고, 같은 문제를 다시 도전하게 합니다.
# 5. 게임이 시작되기 전, 엔터키를 누르면 시작합니다.

# 요구 사항
# 1. 단어는 미리 주어진 리스트에서 random.choice()로 무작위 선택
# 2. input()으로 사용자 입력
# 3. time.time()으로 시작~종료 시간 측정, 소요 시간 계산
# 4. 문제마다 번호가 함께 출력
# 5. 통과/오타 메시지, 총 타자 시간까지 출력

import random
import time

words = [
    "apple", "banana", "orange", "grape", "lemon",
    "peach", "melon", "cherry", "plum", "pear",
    "school", "friend", "family", "flower", "garden",
    "window", "bottle", "pencil", "summer", "winter",
    "happy", "future", "travel", "animal", "market",
    "doctor", "planet", "energy", "nature", "memory"
]

input("[타자 게임] 준비되면 엔터를 누르세요!")

start_time = time.time()
print()

for i in range(1,11):
    word = random.choice(words)

    print(f"문제 {i}")
    print(word)

    while True:
        user_input = input()

        if user_input == word:
            print("통과!!\n")
            break
        else:
            print("오타! 다시 도전!")

end_time = time.time()

total_time = end_time - start_time

print(f"타자 시간: {total_time: .2f}초")




# 실습 6. 타자연습게임

import time
import random

words = [
    "apple", "banana", "orange", "grape", "lemon",
    "peach", "melon", "cherry", "plum", "pear",
    "school", "friend", "family", "flower", "garden",
    "window", "bottle", "pencil", "summer", "winter",
    "happy", "future", "travel", "animal", "market",
    "doctor", "planet", "energy", "nature", "memory"
]

n = 1

input("[타자 게임] 준비되면 엔터!")
start = time.time()

while n < 11:
    print(f"{n}번 문제")
    question = random.choice(words)
    print(question)

    while True:
        user_answer = input()

        if question == user_answer:
            print("통과!!")
            break

        else:
            print("오타! 다시 도전!")

end = time.time()
play_time = end - start
print(f"총 소요시간 : {play_time: .2f}초")



# sys 모듈
# 파이썬 인터프리터와 관련된 다양한 기능 제공

import sys

# 파이썬 버전 정보
print(sys.version) # 3.13.7

# 운영체제
print(sys.platform) # win32

# 프로그램 종료
print("프로그램 시작")
sys.exit() # 강제 종료
print("실행되지 않는 코드") # 프로그램 시작



# os 모듈
# 운영체제와 상호작용 할 수 있도록 도와주는 기능 제공
import os

# getcwd() : 현재 작업 디렉토리 반환
print(os.getcwd()) # C:\Users\luzsb\Documents\RE_5th\Python

# listdir() : 현재 폴더 내 파일, 디렉토리 목록 반환
print(os.listdir())


# 폴더 생성
folder_name = "sample_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
else:
    print(f"{folder_name} 폴더가 이미 존재합니다.")


print(os.listdir())
