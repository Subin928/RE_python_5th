# 사용자 입력 (input)
# - input 함수 : 콘솔을 통해 사용자로부터 문자열 형태로 입력 받음


# input 함수 사용법
# my_input = inpus("콘솔에 띄울 설명")
name = input("이름을 입력하세요")
print(name) # 이름을 입력하세요

# # 숫자로 활용 시 '형 변환' 필요
# a = int(input())
# b = int(input())
# print(a+b)

# c = float(input())
# d = float(input())
# print(c+d)

# 여러 자료 입력하기
# 문자열을 쪼개주는 함수 : split()
# - 기본 구분자 : 공백
과일1, 과일2, 과일3 = input().split()
print(과일1, 과일2, 과일3)

# 다른 구분자 사용
apple, banana, grape = input().split("-")
print(apple, banana, grape)

# 실습 3. input 연습하기
# 사용자로부터 이름과 나이를 입력 받아, 다음 형식으로 출력하세요.
# 안녕하세요. 저는 [이름]이고, [나이]살입니다.

name = input("이름을 입력하세요:")
age = input("나이를 입력하세요:")
print(f"안녕하세요, 저는 {name}이고, {age}살입니다.")

# 실습 4. 입력과 연산 연습하기
# 1. 사용자로부터 가로와 세로를 입력 받아 넓이와 둘레를 계산하세요.

width = int(input("가로 길이를 입력하세요: "))
height = int(input("세로 길이를 입력하세요: "))

area = width * height
perimeter = 2 * (width+height)

print(f"넓이 : {area}")
print(f"둘레 : {perimeter}")

# 2. 네 자릿수 정수를 입력 받고, 각 자릿수를 분리하여 출력하세요.

num = int(input("네 자리 정수를 입력하세요: "))

천의자리 = input()
백의자리 = input()
십의자리 = input()
일의자리 = input()

print(f"""천의 자리: {천의자리}
백의 자리: {백의자리}
십의 자리: {십의자리}
일의 자리: {일의자리}""")

number1 = input('천의 자리: ')
number2 = input('백의 자리: ')
number3 = input('십의 자리: ')
number4 = input('일의 자리: ')
print(number, number1, number2, number3, number4)

# 실습 5. 발표 순서와 발표 주제 정하기
# 한 조에서 팀 프로젝트 발표 순서와 발표 주제를 정했습니다
# 발표자 이름 3명과 주제 3개를 한 번에 입력 받고, 아래와 같이 출력해보세요.

name1, name2, name3 = input("발표자 이름 3명을 입력하세요: ").split()
topic1, topic2, topic3 = input("발표 주제 3개를 입력하세요: ").split()

print("발표 순서 안내입니다.")

print(f"1조 발표자: {name1} - 주제: {topic1}")
print(f"2조 발표자: {name2} - 주제: {topic2}")
print(f"3조 발표자: {name3} - 주제: {topic3}")

# 실습 6. 날짜와 시간
# 년, 월, 일과 시, 분, 초를 한번에 입력 받아서 아래와 같이 출력해보세요.

year, month, day = input("년, 월, 일을 입력해주세요: ").split()
hour, minute, second = input("시, 분, 초를 입력해주세요: ").split()

print(f"""RE3의 개강일은 {year}년 {month}월 {day}일
시작 시간은 {hour}시 {minute}분 {second}초입니다.""")
