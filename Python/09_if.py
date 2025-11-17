'''
조건문
- 조건에 따라 프로그램의 실행 흐름을 분기시키는 제어문
- 조건 : 참/거짓을 구분할 수 있는 문장
'''
'''
# 조건문의 기초 문법
# if + 조건 -> 조건이 참이면 실행

a = int(input())
if a >10:
    print("a는 10보다 커요")
print("조건문 종료") # 5               12
                    # 조건문 종료      a는 10보다 커요
                                    # 조건문 종료

# 들여쓰기 에러 예시
if a > 10:
  print("조건문 종료") # 띄어쓰기 두 칸 가능/동일하게 맞춰줌(일관성있게), tab 키를 이용하는게 보편적
# print("a는 10보다 커요") # IndentationError

# 조건문에 실행할 코드를 작성하지 않았을 때
# pass로 해당 조건문을 넘어갈 수 있음
# if a > 100: # IndentationError
#    pass # 비워둘 경우 pass로 써야 에러가 없이 실행됨

# 실습 1. 날씨에 따른 준비물 안내
# 오늘의 날씨에 따라 필요한 준비물이 달라집니다.
# 사용자에게 오늘의 날씨를 입력받고, 그에 따라 적절한 메시지를 출력하는 프로그램을 만들어 보세요.
# 조건
# 입력값은 "비" 또는 "맑음" 중 하나입니다.
# "비"라고 입력하면 "우산을 챙기세요!"를 출력하세요.
# "맑음"이라고 입력하면 "선크림을 바르세요!"를 출력하세요.

weather = input("오늘 날씨를 입력하세요 (비/맑음): ")

if weather == "비":
   print("우산을 챙기세요!")

if weather == "맑음":
   print("선크림을 바르세요!")
   
'''

# if - else 문
# 조건이 참일 때는 if문을, 조건이 거짓일 때는 else문을 실행
# else -> ~아니라면 의 의미 -> 조건이 필요x, if문과 반드시 같이 나와야 함.
a = int(input())
if a > 10:
    print("a는 10보다 커요")
else:
    print("a는 10보다 작아요")

# 실습 2. 짝수 홀수 판별하기
# 정수를 입력 받아 짝수/홀수 여부를 판단하는 프로그램을 만들어 봅시다.
# "정수를 입력해 주세요." 라는 입력 설명문을 띄워주세요

num = int(input("정수를 입력해주세요: "))
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")


# if - elif - else 구문
# elif : else if의 약자
# elif에서 조건을 반드시 기록
# if 가 있어야만 사용 가능

score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 실습 3. 나이에 따른 영화 관람 가능 여부
# 영화관에서는 연령에 따라 관람할 수 있는 영화가 정해져 있습니다.
# 아래의 기준에 따라 사용자의 나이를 입력 받아 관람 가능한 등급을 출력하는 프로그램을 만들어보세요.

age = int(input("나이를 입력해주세요: "))

if age >= 19:
    print("청소년 관람불가 가능")
elif age >= 16:
    print("15세 이상 관람가")
elif age >= 13:
    print("12세 이상 관람가")
else:
    print("전체 관람가")

# 실습 4. 시, 분, 초 구하기
# 조건문을 이용해서 초를 입력하면 시, 분, 초로 나누어 알려주는 프로그램을 만들어 봅시다.
# 변수를 만들고 정수를 입력 받아 주세요.
# 입력 받은 변수의 값을 사용해서 변수 hour와 minute, second에 알맞은 값을 저장해 주세요.
# 조건에 따라 시, 분, 초를 적절히 출력해 주세요.

# time = int(input("초를 입력하세요: "))

# if time >= 3600:
#     hour = time // 3600
#     minute = (time % 3600) // 60
#     second = time % 60
#     print(f"{hour}시간 {minute}분 {second}초")

# elif time >= 60:
#     minute = time // 60
#     second = time % 60
#     print(f"{minute}분 {second}초")

# else:
#     print(f"{time}초")

# 해설

hour, minute, second = 0, 0, 0
input_second = int(input())

# 60s = 1m, 60m = 1h

minute = input_second // 60
second = input_second % 60
hour = minute // 60
minute %= 60 

if hour > 0:
    print(f"{hour}시간 {minute}분 {second}초")
elif minute > 0:
    print(f"{minute}분 {second}초")
else:
    print(f"{second}초")

# 중첩 조건문
# 하나의 if문 안에 또 다른 if문을 사용하는 것

username = input("관리자 아이디를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

if username == "admin":
    if password == "abcd":
        print("로그인 성공")
    else:
        print("비밀번호가 잘못됐습니다")
else:
    print("잘못된 사용자입니다")

# 실습 5. 편의점 도시락 구매하기
# 당신은 편의점에 들러 간단한 식사를 사려고 합니다.
# 아래의 가격표를 참고하여 금액을 입력하고, 원하는 식품을 선택하면 해당 식품을 구매할 수 있는지 판단하여 출력하는 프로그램을 만들어보세요.
# 김밥 : 2500원
# 삼각김밥 : 1500원
# 도시락 : 4000원
# 프로그램 조건
# 먼저 금액을 입력 받습니다.
# 그 다음, 식품명을 입력 받습니다. (입력값: "김밥", "삼각김밥", "도시락")
# 입력한 금액이 선택한 식품의 가격 이상이면 구매에 성공한 메시지를 출력합니다.
# 금액이 부족할 경우 "금액이 부족합니다."를 출력합니다.

money = int(input("금액을 입력하세요"))
food = input("식품을 선택하세요 (김밥/삼각김밥/도시락): ")

if food == "김밥":
    price = 2500
elif food == "삼각김밥":
    price = 1500
elif food == "도시락":
    price = 4000

if money >= price:
    print("구매 성공!")
else:
    print("금액이 부족합니다.")