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

print(f"최대 간식 개수: {gcd}0")
print(f"최소 간식 개수: {lcm}")

