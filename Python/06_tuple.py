'''
튜플
- 순서가 존재하는 여러 데이터의 모음
- 불변 (immutable) 자료형
'''


# ------- 튜플 생성 --------
my_tuple = (1, 2, 3, 4)
print(my_tuple)
print(type(my_tuple)) #<class 'tuple'>

my_tuple2 = 5, 6, 7, 8
print(type(my_tuple2)) # <class 'tuple'>

# 원소가 하나인 튜플 생성
single_el_tuple = (100,)

# 튜플 생성 함수로 생성
my_tuple2 = tuple()
print(my_tuple2) # ()

my_tuple3 = tuple("codingon")
print(my_tuple3) # ('c', 'o', 'd', 'i', 'n', 'g', 'o', 'n')

# ----- 언패킹 ------
# 시퀀스에 저장된 여러 값을 여러 변수에 나눠 저장하는 것
# 튜플, 리스트, 문자열...
apple, banana, kiwi = ("apple", "banana", "kiwi")
print(apple, banana, kiwi) # apple banana kiwi

# --------------

# 불변성 (immutable)
# - 객체가 생성된 이후 내부 데이터를 변경할 수 없는 것
# my_tuple[0] = 100 # TypeError: 'tuple' object does not support item assignment
# 삭제
# del my_tuple[1] # TypeError: 'tuple' object doesn't support item deletion
# # 튜플 자체는 삭제 가능 but 원소 삭제는 불가
# del my_tuple
# print(my_tuple) # NameError

# ---- 튜플 수정 ---
my_tuple4 = (10, 20, 30)
new_tuple = (100,) + my_tuple4[1:]
print("원본 튜플", my_tuple4) # 원본 튜플 (10, 20, 30)
print("새로운 튜플", new_tuple) # 새로운 튜플 (100, 20, 30)

# 실습1. 튜플 종합 연습
# 회원 정보 해킹 사고!? 고객 데이터 복구 작전
# 당신은 한 스타트업의 데이터 엔지니어입니다. 고객 정보 서버가 해킹을 당해 일부 정보가 손상되었습니다.
# 다행히 튜플 형태로 백업된 데이터가 남아 있으며, 이를 기반으로 정확한 정보를 복원하고 분석해야 합니다.
# 튜블의 불편성과 언패킹, 탐색 기능을 적절히 활용하여 문제를 해결해보세요.

# step 1. 손상된 고객 정보 복원하기
# 해커가 고객 이름을 "unknown"으로 바꿔버렸습니다.
# 하지만 다행히 백업 파일에는 나이와 지역 정보가 그대로 남아 있습니다.
# 아래 고객의 이름을 'eunji'로 바꿔주세요
# user = ("minji", 25, "Seoul")
# 수정한 결과를 restored_user에 저장하고 출력하세요.

user = ("minji", 25, "Seoul")
restored_user = ("eunji",)+user[1:]
name, age, city = restored_user
print(restored_user) # ('eunji', 25, 'Seoul')

# step 2. 고객 정보 언패킹하여 변수에 저장
# 복원된 튜플을 통해 이름, 나이, 도시 정보를 각각 처리할 수 있도록 변수로 나누려 합니다.
# 튜플 restored_user를 언패킹하여 name, age, city 변수에 저장하세요.

name, age, city = restored_user
print(name, age, city) # eunji 25 Seoul

# step4. 고객 데이터 통계 분석
# 현재 고객 DB는 다음과 같습니다.
# users = ("minji", "eunji", "soojin", "minji", "minji")
# "minji"라는 이름이 몇 번 등장하는지 출력하세요.
# "soojin"이 처음 등장하는 위치(인덱스)를 출력하세요.

users = ("minji", "eunji", "soojin", "minji", "minji")
print(users.count("minji")) # 3
print(users.index("soojin")) # 2

# step5. 고객 이름 정렬
# 보고서 출력용으로 고객 이름을 가나다순으로 정렬해야 합니다.
# 단, 튜플은 변경 불가이므로 원본은 유지되어야 하며, 정렬 결과는 리스트 형태로 출력하세요.
# users 튜플을 정렬한 결과를 sorted_users에 저장하고 출력하세요.

sorted_users = tuple(sorted(users))
print(sorted_users) # ('eunji', 'minji', 'minji', 'minji', 'soojin')