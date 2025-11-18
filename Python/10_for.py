# for문
# - 이터러블(순회 가능한) 요소를 하나씩 꺼내서 실행 블록에 전달하는 반복문

# 리스트 반복
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"I like {fruit}") # I like apple
                             # I like banana
                             # I like cherry

# 문자열 반복
my_str = "Apple" # A
                 # p
                 # p
                 # l
                 # e

for char in my_str:
    print(char)

# 튜플 반복
coords = [(1,2),(10,15),(-6,8)]
# 언패킹 (구조분해 가능)
for x,y in coords:
    print(f"x좌표; {x}, y좌표: {y}") # x좌표; 1, y좌표: 2
                                    # x좌표; 10, y좌표: 15
                                    # x좌표; -6, y좌표: 8

# 딕셔너리 반복
person = {
    "name" : "kim",
    "age" : 15,
    "address" : "seoul"
}

# 기본
for key in person:
    print(f"key: {key}, value: {person[key]}") # key: name, value: kim
                                               # key: age, value: 15
                                               # key: address, value: seoul

# value 만 가져오기
for value in person.values():
    print(f"value: {value}") # value: 15
                             # value: seoul

# item 가져오기
for key, value in person.items():
    print(f"key: {key}, value: {value}") # key: name, value: kim
                                         # key: age, value: 15
                                         # key: address, value: seoul

# set 반복
my_set = {1,2,3,4}

for s in my_set:
    print(s) # 1
             # 2
             # 3
             # 4

# 실습 1. for문 기본 문법 문제
# 문제 1. 리스트의 값을 두 배로 변환하기
# for문을 사용하여, 아래 리스트의 각 값의 두 배를 계산한 결과를 새로운 리스트에 저장한 뒤 출력해보세요.
# 주어진 리스트 : numbers = [3, 6, 1, 8, 4]

numbers = [3, 6, 1, 8, 4]
result = [num*2 for num in numbers]
print(result) # [6, 12, 2, 16, 8]

# 정답
numbers = [3, 6, 1, 8, 4]
doubled = []

for number in numbers:
    doubled.append(number*2)
print(doubled) # [6, 12, 2, 16, 8]

# 문제 2. 문자열의 길이 구해서 새 리스트 만들기
# 아래 리스트의 단어의 길이 (len)를 구해서, 길이만 담긴 새로운 리스트를 생성해 출력하세요.
# 주어진 리스트 : words = ["apple", "banana", "kiwi", "grape"]

words = ["apple", "banana", "kiwi", "grape"]
lengths = [len(word) for word in words]
print(lengths) # [5, 6, 4, 5]

# 정답
words = ["apple", "banana", "kiwi", "grape"]
lengths = []

for word  in words:
    lengths.append(len(word))

print(lengths) # [5, 6, 4, 5]

# 문제 3. 좌표 튜플에서 x,y 좌표 나누기
# 아래와 같은 (x,y) 형태의 좌표 튜플 리스트에서 for문 튜플 언패킹(구조 분해)을 활용하여,
# 각 좌표의 x 값만을 x_values 리스트에, y 값만을 y_values 리스트에 저장하고 각각 출력하세요.
# 주어진 리스트 : coordinates = [(1,2), (3,4), (5,6), (7,8)]

coordinates = [(1,2), (3,4), (5,6), (7,8)]
for x_values, y_values in coordinates:
    print(f"x좌표: {x_values}, y좌표: {y_values}")

# 정답
coordinates = [(1,2), (3,4), (5,6), (7,8)]
x_values = []
y_values = []

for x, y in coordinates:
    x_values.append(x)
    y_values.append(y)

print(f"x좌표: {x_values}")
print(f"y좌포: {y_values}") # x좌표: [1, 3, 5, 7]
                            # y좌포: [2, 4, 6, 8]






# for문과 range()
# range 함수 : 지정된 범위의 정수 시퀀스 생성

# 기본 문법
# range(start, end, step)
# - start : 생략 가능, 기본값 0
# - end : end-1까지 생성
# - step : 생략 가능, 기본값 = 1

range(1,5)

for i in range(1,5):
    print(i) # 1
             # 2
             # 3
             # 4

for i in [1,2,3,4]:
    print(i) # 1
             # 2
             # 3
             # 4

# start 생략
for i in range(5):
    print(i) # 0
             # 1
             # 2
             # 3
             # 4

# 간격 (step) 지정
for i in range(0,11,2):
    print(i) # 0
             # 2
             # 4
             # 6
             # 8
             # 10

for i in range(11,0,-2):
    print(i) # 11
             # 9
             # 7
             # 5
             # 3
             # 1

# 실습 2. for문과 range
# 문제 1. 입력 받은 수의 합 구하기
# for 문과 range()를 사용하여 1부터 사용자가 입력한 수까지의 합을 구해보세요.

number = int(input("숫자를 입력하세요: "))
total = 0
for n in range(1, number+1):
    total += n
print(total)

# 정답
num = int(input("숫자를 입력하세요ㅣ "))
sum = 0

for i in range(num+1):
    sum += i

print(sum)

# 문제 2. 구구단 만들기(1)
# 사용자로부터 정수 하나를 입력 받아, 해당 숫자의 구구단을 아래와 같이 출력하는 프로그램을 작성하세요.

number = int(input("숫자를 입력하세요: "))
for i in range(1,10):
    print(f"{number} X {i} = {number * i}")

# 정답

dan = int(input("생성할 단을 입력해주세요 "))

for i in range(1,10):
    print(f"{dan} X {i} = {dan * i}")

# 문제 3. 3의 배수의 합 구하기
# for문과 range()를 사용하여 1부터 100까지의 수 중 3의 배수만 골라 합을 구해 출력하세요.

total = 0
for i in range(1,101):
    if i % 3 == 0:
        total += i
print(total)

# 정답
result = 0
# 1)
for i in range(3,101, 3):
    result += i

print("3의 배수의 합: ",result)

# 2)
for i in range(1,101):
    if i % 3 ==0:
        result += i

print("3의 배수의 합: ",result)

# 문제 4. 짝수이면서 5의 배수인 수 출력하기
# 사용자로부터 숫자 n을 입력 받아,
# 1부터 n까지 수 중에서 짝수이면서 5의 배수인 수만 출력하세요.

number = int(input("숫자를 입력하세요: "))
for i in range(1, number+1):
    if i % 2 == 0 and i % 5 ==0:
        print(i)
    
# 정답

n = int(input("숫자를 입력하세요: "))
for i in range(1, n+1):
    if i % 2 == 0 and i % 5 == 0:
        print(i)






# 루프 제어문
# - 특정 조건 하에서만 작동하도록 구현

# break : 반복을 즉시 중단
for i in range(10):
    if i == 5:
        break

    print(i)
print("반복 종료") # 0
                  # 1
                  # 2
                  # 3
                  # 4
                  # 반복 종료

# continue : 현재 반복을 넘어감

for i in range(5):
    if i == 2:
        print("continue = 건너뜀")
        continue
    
    print(i)

print("반복 종료") # 0
                  # 1
                  # continue = 건너뜀
                  # 3
                  # 4
                  # 반복 종료

# pass
for i in range(10):
    pass

# for - else 구문
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("반복종료") # 0
                      # 1 -> 반복종료라는 문구가 안 나옴(break로 종료시 else 구문 실행 x)


# 중첩 for문
# - 하나의 for문 안에 다른 for문이 들어있는 구조


# 이중 for문
for i in range(5):
    for j in range(5):
        print("i,j", i, j)
    print()


# 실습 3. 중첩 for문 연습 문제
# 문제 1. 구구단 만들기(2)
# for 문을 중첩하여 2단부터 9단까지의 구구단 전체를 아래와 같은 형태로 출력해보세요

for i in range(2,10):
    print(f"[ {i}단 ]")
    for j in range(1,10):
        print(f"{i} X {j} = {i * j}")
    print()

# 문제 2. 중첩 for문 별찍기
# 사용자로부터 정수 n을 입력받아, 별(*) 문자를 n줄에 걸쳐 출력하는 프로그램을 작성하세요.
# 아래와 같이 3가지 정렬 방식(왼쪽 정렬, 가운데 정렬, 오른쪽 정렬)으로 각각 구현해보세요.

# 정답

# 왼쪽 정렬
n = int(input("몇 줄? "))

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

# 오른쪽 정렬
n = int(input("몇 줄? "))

for i in range(1,n+1):
    # 공백 출력
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("*", end ="")
    print()

# 가운데 정렬
n = int(input("몇 줄? "))

for i in range(1,n+1):
    # 공백 출력
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()