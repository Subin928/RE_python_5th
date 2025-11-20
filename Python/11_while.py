'''
while문
- 조건이 True인 동안 코드를 반복하는 반복문
- 조건이 False가 되면 반복을 멈춤
- 반복횟수가 정해지지 않았을 때 사용
'''

# while문 기본 문법
# 조건 : 참/거짓을 구분할 수 있는 문장
# while 조건:
    # 반복할 코드


# 무한루프
# 사용시 주의. 반드시 종료 조건이 있어야 함
# while True:
#     print("반복중") # 반복중이 계속 나옴


# 예제1
light = "green"

while light == "green":
    print("계속 가세요!")
    light = input("신호등의 신호를 입력하세요(green/yellow/red): ") 

print("중지!!") # 계속 가세요!
                # 신호등의 신호를 입력하세요(green/yellow/red): green
                # 계속 가세요!

                # 계속 가세요!
                # 신호등의 신호를 입력하세요(green/yellow/red): red
                # 중지!!

# 예제 2. 별도의 반복 변수를 정의

i = 0

while i < 5:
    print(i, "반복")
    i += 1
print("반복 종료") # 0 반복
                   # 1 반복
                   # 2 반복
                   # 3 반복
                   # 4 반복
                   # 반복 종료

# 실습 1. while문 연습문제

# 문제 1. 비밀 코드 맞추기 (1)

# 비밀 모임에 입장하려면 올바른 비밀 코드를 입력해야 합니다. 아래의 요구사항에 만족하는 코드를 작성하세요.
# 조건
# 변수 secret_code에는 "codingonre5"라는 문자열이 저장되어 있습니다.
# 사용자에게 "비밀 코드를 입력하세요." 라고 안내 문구를 출력합니다.
# 사용자가 입력한 코드가 secret_code와 다를 경우, 계속해서 다시 입력 받습니다.
# 코드가 맞으면 "입장이 허용되었습니다!"를 출력하고 프로그램을 종료합니다.

secret_code = "codingonre5"

while True:
    user_input = input("비밀 코드를 입력하세요: ")

    if user_input == secret_code:
        print("입장이 허용되었습니다!")
        break
    else:
        print("코드가 틀렸습니다. 다시 입력하세요.")

# 정답

secret_code = "codingonre5"
user_input = ""

# 비밀코드와 사용자 입력이 같지 않을때 반복
while user_input != secret_code:
    user_input = input("비밀 코드를 입력하세요: ")

print("입장이 허용되었습니다!")


# 문제 2. 업다운 게임

# 컴퓨터가 1부터 100 사이의 무작위 정수 하나를 미리 정해 놓았습니다. 사용자는 이 수를 맞힐 때까지 계속해서 숫자를 입력해야 합니다.
# 조건
# 입력한 숫자가 정답보다 크면: "입력한 숫자보다는 작아요."
# 입력한 숫자가 정답보다 작으면: "입력한 숫자보다는 커요."
# 숫자를 맞히면: "{입력 횟수}"번 만에 정답을 맞췄습니다."라고 출력합니다.

answer = 50
count = 0

while True:
    guess = int(input("숫자를 입력하세요: "))
    count += 1

    if guess > answer:
        print("입력한 숫자보다는 작아요.")
    elif guess < answer:
        print("입력한 숫자보다는 커요.")
    else:
        print(f"{count}번 만에 정답을 맞췄습니다!")
        break

# 정답

# answer = 99
import random
answer = random.randint(1,100)
print(answer)
num = 0 # 사용자 입력 받을 변수
time = 0 # 실행 횟수를 저정할 수 있는 변수

while num != answer:
    num = int(input("1~100 사이의 수를 입력해주세요: "))
    time += 1

    if num > answer:
        print(f"정답이 {num}보다는 작아요")
    elif num < answer:
        print(f"정답이 {num}보다 커요")

print(f"{time}번 만에 정답을 맞췄습니다")

# 루프 제어문
# running = True
# while running:
#     if 조건1:
#         running = False
    
#     if 조건2:
#         running = False

# # break문
# while True:
#     if 조건:
#         break

# 예제 1

i = 0

while True:
    print(i, "실행")
    my_select = input("메뉴를 골라주세요: ")

    if my_select == "종료":
        break

    i += 1

print("반복문 종료") # 0 실행
                    # 메뉴를 골라주세요: 삼겹살
                    # 1 실행
                    # 메뉴를 골라주세요: 종료
                    # 반복문 종료

# continue

i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
print("반복 종료") # 1
                   # 3
                   # 5
                   # 반복 종료

# 실습 2. while문 연습문제 (2)

# 문제 1. 비밀 코드 맞추기 (2)

# 비밀 모임에 입장하려면 올바른 비밀 코드를 입력해야 합니다. 정답을 입력할 때까지 무한히 반복되며, 정확한 코드를 입력하면 루프를 탈출합니다.
# 조건
# 변수 secret_code에는 "codingonre5"라는 문자열이 저장되어 있습니다.
# 사용자에게 "비밀 코드를 입력하세요." 라고 안내 문구를 출력합니다.
# 정답이 맞을 때까지 계속 입력을 받습니다.
# 사용자가 입력이 정답과 일치하면 "입장 완료! 환영합니다."를 출력하고 break로 루프를 종료하세요.
# 정답이 틀렸다면 "비밀 코드가 틀렸습니다. 다시 시도하세요."를 출력한 후 루프를 계속 진행합니다.

secret_code = "codingonre5"
user_input = ""

while True:
    user_input = input("비밀 코드를 입력하세요: ")

    if user_input == secret_code:
        print("입장 완료! 환영합니다.")
        break

    else:
        print("비밀 코드가 틀렸습니다. 다시 시도하세요.")

# 문제 2. 유효한 나이만 평균 내기
# 사용자에게 총 5명의 나이를 입력 받아야 합니다. 유효한 나이들만 평균을 내어 출력하세요.
# 조건
# 변수 times는 유효한 입력의 개수를 셉니다.
# 변수 sum_age는 나이의 합계를 저장합니다.
# 나이는 정수로 입력 받습니다.
# 나이가 0 이하이거나 120보다 크면 무시하고 반복을 건너뜁니다.
# 5개의 유효한 나이를 입력 받으면 루프를 종료하고, 총합과 평균을 출력합니다.
# 결과값 총 나이 합계는  , 평균은  입니다

times = 0
sum_age = 0

while times < 5:
    age = int(input("나이를 입력하세요: "))

    if age < 0 or age > 120:
        print("유효하지 않은 나이입니다. 다시 입력하세요.")
        continue

    sum_age += age
    times += 1
    average = sum_age / times

print(f"총 나이 합계는 {sum_age}, 평균은 {average}입니다.")

# 정답

times = 0
sum_age = 0

while times < 5:
    age = int(input("나이를 입력하세요: "))

    # 나이가 0 이하 또는 120 초과이면 건너 뜀
    if age <= 0 or age > 120:
        continue

    times += 1
    sum_age += age

print(f"총 나이 합계는 {sum_age}, 평균은 {int(sum_age/times)}")



# 중첩 while문

# while 바깥 조건식:
#     # 바깥 루프의 실행 코드
#     while 안쪽 조건식:
#         # 안쪽 루프의 실행 코드

# 예제

dan = 2  # 2단부터 시작

while dan <= 9:  # 9단까지
    print(f"[{dan}단]")

    num = 1  # 1부터 9까지 곱할 숫자
    while num <= 9:
        print(f"{dan} X {num} = {dan * num}")
        num += 1  # num 증가

    print()   # 단 끝나고 줄바꿈
    dan += 1  # 다음 단으로 이동


dan = 2
while dan <= 9:
    num = 1
    print(f"[{dan}단]")

    while num <= 9:
        num += 1
        if num % 2 != 0:
            continue
        else:
            print(f"{dan} X {num} = {dan * num}")
            num += 1

        num += 1

    print()
    dan += 1

dan = 2  # 2단부터 시작
while dan <= 9:  # 9단까지 반복
    print(f"[{dan}단]")

    num = 1  # 곱해질 숫자 1부터 시작

    while num <= 9:  # num이 1~9까지 반복
        if num % 2 == 0:      # num이 짝수라면
            print(f"{dan} X {num} = {dan * num}")  # 짝수 곱셈만 출력
        num += 1  # num을 1씩 증가 (증가 위치는 딱 한 곳!)
    
    print()  # 단 사이에 한 줄 띄우기
    dan += 1  # 다음 단으로 이동

dan = 2
while dan <= 9:
    num = 1
    print(f"[{dan}단]")

    while num <= 9:
        num += 1
        if num % 2 != 0:
            break
        else:
            print(f"{dan} X {num} = {dan * num}")
            num += 1

        num += 1

    print()
    dan += 1

# 실습 3. 중첩 while문 연습문제

# 문제 1. 로그인 시스템 구현
# 로그인 시스템을 만들고 있습니다. 순서대로 ID와 비밀번호를 입력 받고, ID와 비밀번호 모두 맞으면 로그인 성공 메시지를 출력하세요.

# 조건
# 임의의 ID와 비밀번호를 세팅합니다.
# 잘못된 ID일 경우 "ID가 존재하지 않습니다."를 출력하고 다시 ID를 입력 받습니다.
# ID가 맞으면 비밀번호를 입력 받고, 비밀번호가 틀리면 "비밀번호가 틀렸습니다."를 출력하고 다시 입력 받습니다.
# 둘 다 맞으면 "로그인 성공!"을 출력하고 프로그램을 종료합니다.


true_ID = "subin"
true_PW = "1234"

while True:
    user_ID = input("아이디를 입력하세요: ")

    if user_ID != true_ID:
        print("ID가 존재하지 않습니다.")
    
    else:
        while True:
            user_PW = input("비밀번호를 입력하세요: ")

            if user_PW != true_PW:
                print("비밀번호가 틀렸습니다.")
            
            else:
                print("로그인 성공!")
                break
    break


# 정답
# 아이디와 비밀번호를 저장할 변수

user_id = "codingon"
user_pw = "abc123"

# ID 먼저 검사

while True:
    id_input = input("ID를 입력하세요: ")

    if id_input != user_id:
        print("ID가 일치하지 않습니다.")
        continue

    while True:
        pw_input = input("비밀번호를 입력하세요: ")

        if pw_input != user_pw:
            print("비밀번호가 일치하지 않습니다.")
            continue

        print("로그인 성공!")
        break

# 추가 문제. 로그인 시스템 구현

# 조건
# 임의의 ID와 비밀번호를 세팅합니다.
# 중첩 while문 사용
# break,continue 사용할 것
# 실행 화면과 같은 모습으로 만들어주세요

my_id = "codingon"
my_pw = "abc123"

while True:
    print("=== 로그인 화면 ===")
    print("1. 로그인")
    print("2. 종료")

    choice = input("선택: ")

    if choice == "2":
        print("프로그램을 종료합니다.")
        break

    elif choice == "1":
        user_id = input("ID: ")
        user_pw = input("PW: ")

        if user_id == my_id and user_pw == my_pw:
            print("로그인 성공!")

            
            while True:
                print("==== 메뉴 ====")
                print("1. 정보 보기")
                print("2. 설정")
                print("3. 로그아웃")
                print("================")

                menu = input("메뉴 선택: ")

                if menu == "1":
                    print("회원 정보입니다.")
                
                elif menu == "2":
                    print("설정 메뉴입니다.")
                
                elif menu == "3":
                    print("로그아웃합니다.")
                    break
            
        else:
            print("로그인 실패! 다시 시도해주세요.")

# 정답

# ID, PW 동시에 받는 경우

user_id = "codingon"
user_pw = "abc123"

while True:         # 전체 프로그램 반복
    print("=== 로그인 화면 ===")
    print("1. 로그인")
    print("2. 종료")
    main_sel = input("선택: ")

    if main_sel == "2":
        print("프로그램을 종료합니다.")
        break

    elif main_sel != "1":
        print("잘못 선택하셨습니다.|n")
        continue

    # 로그인

    id_input = input("ID: ")
    pw_input = input("PW: ")

    if id_input != user_id or pw_input != user_pw:
        print("로그인 실패! 다시 시도해주세요.|n")
        continue

    print("로그인 성공!|n")

    # 로그인 후 메뉴 화면
    
    while True:
        print("=== 메뉴 ===")
        print("1. 정보 보기")
        print("2. 설정")
        print("3. 로그아웃")
        print("==============")

        sel = input("메뉴 선택: ")

        if sel == "1":
            print("회원 정보입니다.|n")
            continue
        
        elif sel == "2":
            print("설정 메뉴입니다.|n")
            continue

        elif sel == "3":
            print("로그아웃합니다. |n")
            break # 안쪽 while만 끊고 로그인 화면으로

        else:
            print("잘못 입력하셨습니다. |n")
            continue

# 해석

# [바깥 while 시작]
#     로그인 화면 출력
#     1 → 로그인 절차
#     2 → break로 프로그램 종료
#     나머지 → continue (다시 로그인 화면)

#     [ID/PW 입력]
#     틀림 → continue (로그인 화면)
#     맞음 → 안쪽 while 진입

#         [안쪽 while 시작]
#             메뉴 선택
#             1/2 → continue (다시 메뉴)
#             3 → break (안쪽 while 종료 → 로그인 화면으로)
#             나머지 → continue (다시 메뉴)

# [바깥 while 반복]