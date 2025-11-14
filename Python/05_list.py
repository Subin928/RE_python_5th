'''
리스트 (List)
- 여러 값들을 순서대로 저장할 수 있는 자료형
- 인덱스(index): 각 값에 부여된 순서 (0부터 시작)
# - 가변 자료형(mutable): 원소의 추가/수정/삭제 가능
# '''

# 리스트 만들기
list1 = [] # 빈 리스트
list2 = ["안녕하세요", "반갑습니다"] # ['안녕하세요', '반갑습니다']
list3 = [10, "good", 3.14, [1,2,3,4]] # [10, 'good', 3.14, [1, 2, 3, 4]]

print(list1, list2, list3)

list4 = list() # []
list5 = list("Codingon") # ['C', 'o', 'd', 'i', 'n', 'g', 'o', 'n']
print(list4, list5)

# ===================
# 인덱싱과 슬라이싱
my_list = [1,2,3,4,5]
print(my_list[1]) #2
print(my_list[-1]) #5
my_list[3] = -1
print(my_list) # [1, 2, 3, -1, 5]

number = input("네 자릿수 정수를 입력하세요: ")
천 = number[0]
백 = number[1]
십 = number[2]
일 = number[3]
print(천, 백, 십, 일)

# ------------------
# 슬라이싱
my_numbers = [10,20,30,40,50,60,70,80,90,100]
print(my_numbers[1:4]) # [20, 30, 40]
print(my_numbers[3:]) # [40, 50, 60, 70, 80, 90, 100]
print(my_numbers[:4]) # [10, 20, 30, 40]
print(my_numbers[::-1]) # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
my_numbers[2:4] = [300,400]
print(my_numbers)

# 실습 1. 인덱싱, 슬라이싱 복습문제

# 문제 1. 첫 번째 요소와 마지막 요소 출력하기
# 다음 리스트에서 첫 번째 요소와 마지막 요소를 출력하세요
# nums = [10,20,30,40,50]

nums = [10,20,30,40,50]
print(nums[0]) # 10
print(nums[-1]) # 50

# 문제 2. 가운데 세 개의 요소 추출하기
# 다음 리스트에서 가운데 3개의 요소만 슬라이싱하여 새 리스트로 만들어 출력하세요.
# nnums = [100,200,300,400,500,600,700]

nums = [100,200,300,400,500,600,700]
print(nums[2:5]) # [300, 400, 500]

# 문제 3. 리스트의 원소 두배 하기
# 다음 리스트의 모든 원소를 두 배로 만들어 보세요.
# nums = [1,2,3,4,5]

nums = [1,2,3,4,5]
nums[0] = nums[0]*2
nums[1] = nums[1]*2
nums[2] = nums[2]*2
nums[3] = nums[3]*2
nums[4] = nums[4]*2
print(nums) # [2, 4, 6, 8, 10]

# 문제 4. 리스트 뒤집어서 출력하기
# 다음 리스트를 역순으로 슬라이싱하여 출력하세요.
# items = ["a", "b", "c", "d", "e"]

items = ["a", "b", "c", "d", "e"]
print(items[::-1]) # ['e', 'd', 'c', 'b', 'a']

# 문제 5. 짝수 인덱스 요소만 출력하기
# 다음 리스트에서 짝수 인덱스(0,2,3,...)의 요소들만 출력하세요.
# data = ["zero", "one", "two", "three", "four", "five"]

data = ["zero", "one", "two", "three", "four", "five"]
print(data[::2]) # ['zero', 'two', 'four']

# 문제 6. 슬라이싱으로 리스트 수정하기
# 슬라이싱으로 "어벤져스", "라라랜드" -> "매트릭스", "타이타닉"으로 바꿔보세요.
# movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]

movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
movies[2:4] = ["매트릭스","타이타닉"]
print(movies) # ['인셉션', '인터스텔라', '매트릭스', '타이타닉', '기생충']

# 문제 7. 특정 규칙에 따라 요소 추출
# 다음 리스트에서 "물리", "생물", "지구과학"만 순서대로 추출하여 새 리스트로 만드세요.
# subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]

subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
print(subjects[3:8:2]) # ['물리', '생물', '지구과학']

# 문제 8. 리스트를 3개 구간으로 나누어 역순 병합
# 다음 리스트를 [1~3번째 요소] + [4~6번째 요소] + [7~9번째 요소] 순서로 세 구간으로 나눈 뒤,
# 각 구간을 역순으로 따로 출력하세요. 단, 출력 시 한 줄로 출력되게 출력해주세요.
# data = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

data = ["A", "B", "C", "D", "E", "F", "G", "H","I"]
new_list1 = data[0:3]
new_list2 = data[3:6]
new_list3 = data[6:9]
print(new_list1[::-1], new_list2[::-1], new_list3[::-1]) # ['C', 'B', 'A'] ['F', 'E', 'D'] ['I', 'H', 'G']

print(data[0:3][::-1], end=" ")
print(data[3:6][::-1], end=" ")
print(data[6:9][::-1], end=" ") # ['C', 'B', 'A'] ['F', 'E', 'D'] ['I', 'H', 'G']

# 인덱싱, 슬라이싱 주의 사항
# my_list = [1,2,3,4]
# my_list[5] # IndexError: list index out of range

my_list = [1,2,3,4,5]
print(my_list[4:1:2]) # []
print(my_list[1:3:-1]) # []

# =============================
# 리스트 연산 - del
my_list = [10,20,30,40,50]
del my_list[2] # 특정 요소 삭제
print(my_list) # [10, 20, 40, 50]
del my_list[1:3] # 슬라이스 범위 삭제
print(my_list) # [10, 50]
del my_list # 리스트 삭제
# print(my_list) # NameError: name 'my_list' is not defined

# 리스트 연결 - +
list1 = ["가", "나", "다"]
list2 = ["라", "마", "바"]
new_list = list1+ list2
print(list1, list2, new_list, sep= " / ") # ['가', '나', '다'] / ['라', '마', '바'] / ['가', '나', '다', '라', '마', '바']

# 리스트 반복 - *
medal = ["금", "은", "동"]
new_list = medal *3
print(medal, new_list, sep = " / ") # ['금', '은', '동'] / ['금', '은', '동', '금', '은', '동', '금', '은', '동']

# 포함 여부 (in, not in)
fruits = ["토마토", "사과", "포도", "수박", "바나나"]
print("포도" in fruits) # True
print("참외" not in fruits) # True

# 실습 2. 리스트 연산 복습문제(1)
# 문제 1. 부분 삭제 후 연결
# 다음 리스트에서 가운데 3개 요소 ("banana", "cherry", "grape")를 삭제한 뒤,
# 나머지 앞/뒤 리스트를 연결하여 새 리스트 result를 출력하세요.
# fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]

fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruits[1:4]
result = fruits[:1] + fruits[1:]
print(result) # ['apple', 'watermelon', 'strawberry']

# 실습 2. 리스트 연산 복습문제(2)
# 문제 2. 반복 리스트 내부 요소 삭제
# 다음 리스트를 3번 반복한 후, 전체 결과에서 중간에 있는 "A"만 삭제하세요.
# 최종 리스트를 출력하세요.
# letters=["A", "B"]

letters = ["A", "B"]
new_list = letters*3
del new_list[2]
print(new_list) # ['A', 'B', 'B', 'A', 'B']

# ==================
# 리스트 주요 메서드
# ==================

# 길이
numbers =  [1,2,3,4,5]
print("1. len()", len(numbers), len("codingon")) # 1. len() 5 8

# 삽입
numbers.append(6)
numbers.append(7)
numbers.append(8)
print("2. append()", numbers) # 2. append() [1, 2, 3, 4, 5, 6, 7, 8]

numbers.insert(2, 2.5)
numbers.insert(4, 3.5)
print("3. insert()", numbers) # 3. insert() [1, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8]

numbers.extend([9,10])
print("4. extend()", numbers) # 4. extend() [1, 2, 2.5, 3, 3.5, 4, 5, 6, 7, 8, 9, 10]

# 삭제
numbers.append(2.5)
numbers.remove(2.5)
print("5. remove()", numbers) # 5. remove() [1, 2, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 2.5]

a = numbers.pop(1)
print("6. pop() 삭제한 요소", a) # 6. pop() 삭제한 요소 2
print(numbers) # [1, 3, 3.5, 4, 5, 6, 7, 8, 9, 10, 2.5]
b = numbers.pop() 
print("6. pop() 삭제한 요소", b) # 6. pop() 삭제한 요소 2.5
print(numbers) # [1, 3, 3.5, 4, 5, 6, 7, 8, 9, 10]

# 정렬
numbers1 = [3,2,1,4]
numbers1.sort()
print("7-1. sort()",numbers1) # 7-1. sort() [1, 2, 3, 4]
numbers1.sort(reverse=True)
print("7-1. sort(reverse=True)",numbers1) # 7-1. sort(reverse=True) [4, 3, 2, 1]

numbers2 = [50,52,53,51]
new_numbers = sorted(numbers2)
new_numbers_desc = sorted(numbers2, reverse=True)
print("7-2. sorted()", numbers2, new_numbers, new_numbers_desc) # 7-2. sorted() [50, 52, 53, 51] [50, 51, 52, 53] [53, 52, 51, 50]

# 뒤집기
my_numbers = [100, 101, 104, 103, 102]
my_numbers.reverse()
print("8-1. reverse()", my_numbers) # 8-1. reverse() [102, 103, 104, 101, 100]

my_numbers2 = list(reversed(my_numbers))
print("8-2. reversed()", my_numbers2, my_numbers) # 8-2. reversed() [100, 101, 104, 103, 102] [102, 103, 104, 101, 100]

# count, min, max, sum
numbers = [1, 2, 2, 2, 2, 3, 4, 5, 6, 7]
print("9. count()", numbers.count(2)) # 9. count() 4
print("10. min/max", min(numbers), max(numbers)) # 10. min/max 1 7
print("11. sum", sum(numbers)) # 11. sum 34

# 실습 3. 리스트 주요 메서드 복습 문제(1)
# 문제 1. 기차 탑승 시뮬레이션
# 기차에 승객들이 순서대로 탑승하고 있습니다.
# 1. 처음엔 ["철수", "영희"]가 탑승했습니다.
# 2. 그 다음 역에서 ["민수","지훈"]이 함께 탑승했습니다.
# 3. 다음 역에서 "영희"는 내렸습니다.
# 4. "수진"이 1번 자리에 끼어 탑승했습니다.
# 5. 마지막 역에서 "민수"가 내렸고, 기차 안의 순서를 뒤집었습니다.
# 현재 기차 안에는 어떤 승객들이 어떤 순서로 앉아 있을까요?

train = []
train.append("철수")
train.append("영희")
train.extend(["민수", "지훈"])
train.remove("영희")
train.insert(1,"수진")
train.remove("민수")
train.reverse()
print(train) # ['지훈', '수진', '철수']

# 실습 3. 리스트 주요 메서드 복습 문제(2)
# 문제 2. 숫자 처리 게임
# 숫자 카드 게임에서 다음 리스트가 주어졌습니다 : [5,3,7]
# 1. 2장을 더 추가해서 [4,9]가 들어옵니다.
# 2. 가장 큰 수와 가장 작은 수를 각각 구해 출력하세요.
# 3. 총합을 출력하세요
# 4. 리스트를 정렬한 다음, 마지막 숫자를 제거하세요.
# 5. 최종 리스트를 출력하세요

nums = [5, 3, 7]
nums.extend([4, 9])
print(max(nums)) # 9
print(min(nums)) # 3
print(sum(nums)) # 28
nums.sort()
nums.pop()
print(nums) # [3, 4, 5, 7]