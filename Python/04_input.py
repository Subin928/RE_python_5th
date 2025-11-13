# 사용자 입력 (input)
# - input 함수 : 콘솔을 통해 사용자로부터 문자열 형태로 입력 받음


# input 함수 사용법
# # my_input = inpus("콘솔에 띄울 설명")
# name = input("이름을 입력하세요")
# print(name)

# # 숫자로 활용 시 '형 변환' 필요
# a = int(input())
# b = int(input())
# print(a+b)

# c = float(input())
# d = float(input())
# print(c+d)

# 여러 자료 입력하기
# # 문자열을 쪼개주는 함수 : split()
# # - 기본 구분자 : 공백
# 과일1, 과일2, 과일3 = input().split()
# # print(과일1, 과일2, 과일3)

# # 다른 구분자 사용
# apple, banana, grape = input().split("-")
# print(apple, banana, grape)

# name = input("이름을 입력하세요:")
# age = input("나이를 입력하세요:")
# print(f"안녕하세요, 저는 {name}이고, {age}살입니다.")

# width = int(input("가로 길이를 입력하세요: "))
# height = int(input("세로 길이를 입력하세요: "))

# area = width * height
# perimeter = 2 * (width+height)

# print(f"넓이 : {area}")
# print(f"둘레 : {perimeter}")

# a = int(input("네 자릿수 정수를 입력하세요: "))

# 천의자리 = a // 1000
# 백의자리 = (a//100) % 10
# 십의자리 = (a // 10) % 10
# 일의자리 = a % 10

# print("천의 자리: ", 천의자리)
# print("백의 자리: ", 백의자리)
# print("십의 자리: ", 십의자리)
# print("일의 자리: ", 일의자리)

# name1, name2, name3 = input("발표자 이름 3명을 입력하세요: ").split()
# topic1, topic2, topic3 = input("발표 주제 3개를 입력하세요: ").split()

# print("발표 순서 안내입니다.")

# print(f"1조 발표자: {name1} - 주제: {topic1}")
# print(f"2조 발표자: {name2} - 주제: {topic2}")
# print(f"3조 발표자: {name3} - 주제: {topic3}")

# year, month, day = input("년, 월, 일을 입력해주세요: ").split()
# hour, minute, second = input("시, 분, 초를 입력해주세요: ").split()

# print(f"""RE3의 개강일은 {year}년 {month}월 {day}일
# 시작 시간은 {hour}시 {minute}분 {second}초입니다.""")

# num = int(input("네 자리 정수를 입력하세요: "))

# 천의자리 = input()
# 백의자리 = input()
# 십의자리 = input()
# 일의자리 = input()

# print(f"""천의 자리: {천의자리}
# 백의 자리: {백의자리}
# 십의 자리: {십의자리}
# 일의 자리: {일의자리}""")

# number1 = input('천의 자리: ')
# number2 = input('백의 자리: ')
# number3 = input('십의 자리: ')
# number4 = input('일의 자리: ')
# print(number, number1, number2, number3, number4)