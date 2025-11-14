'''
set (집합)
- 원소의 중복을 허용하지 않는 여러 데이터의 모음
- 순서가 없는 컬렉션 자료형
'''

# set 만들기
s1 = {1,2,3}
print(s1, type(s1)) # {1, 2, 3} <class 'set'>

s2 = {1,1,1,1,2,2,2,3,3,3,4,4,4,}
print(s2) # {1, 2, 3, 4}

# 빈 set 만들기
# - 중괄호에 원소를 넣지 않고 만들면 빈 dict로 인식됨
s3 = {}
print(type(s3)) # <class 'dict'>

# set 함수로 생성
s4 = set()
print(s4, type(s4)) # set() <class 'set'>

# set 함수의 활용 : 원소의 중복 제거
my_list = [1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4]
s5 = set(my_list)
print(s5) # {1, 2, 3, 4}

# 인덱싱 X
# s1[1] # TypeError: 'set' object is not subscriptable

# 자료형 제한
# - 가변 자료형은 원소로 사용할 수 없다
# s1 = {1,2,3, [1,2,3]} # TypeError: unhashable type: 'list'

# set 연산
# 집합의 연산 : 합집합, 교집합, 차집합, 대칭차집합
a = {1,2,3}
b = {3,4,5}

# 합집합 (|, .union)
s_union1 = a | b
s_union2 = a.union(b)
print("합집합1", s_union1) # 합집합1 {1, 2, 3, 4, 5}
print("합집합2", s_union2) # 합집합1 {1, 2, 3, 4, 5}

# 교집합(&, .intersection)
s_inter1 = a & b
s_inter2 = a.intersection(b)
print("교집합1", s_inter1) # 교집합1 {3}
print("교집합2", s_inter2) # 교집합1 {3}

# 차집합 (-, difference)
s_diff1 = a - b
s_diff2 = a.difference(b)
print("차집합", s_diff1) # 차집합 {1, 2}
print("차집합", s_diff2) # 차집합 {1, 2}
print(b-a) # {4, 5}

# 대칭차집합 (^, symmetric_difference)
s_symm1 = a ^ b
s_symm2 = a.symmetric_difference(b)
print("대칭차집합", s_symm1) # 대칭차집합 {1, 2, 4, 5}
print("대칭차집합", s_symm2) # 대칭차집합 {1, 2, 4, 5}

# 실습1. set 종합 연습(1)

# 문제 1. 중복 제거 및 개수 세기
# 중복을 제거한 후, 총 몇 명이 제출했는지 출력하는 프로그램 작성
# submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']

submissions = ['kim', 'lee', 'kim', 'park', 'choi', 'lee', 'lee']
unique_students = set(submissions)

print("제출한 학생 수:", len(unique_students)) # 제출한 학생 수: 4
print("제출자 명단:", unique_students) # 제출자 명단: {'park', 'choi', 'kim', 'lee'}

# 실습1. set 종합 연습(2)

# 문제 2. 공통 관심사 찾기
# 두 명의 사용자가 각자 좋아하는 영화 장르를 아래와 같이 입력했습니다.
# 두 사용자의 공통 관심 장르, 서로 다른 장르, 모든 장르 목록을 출력하세요.
# user1 = {'SF', 'Action', 'Drama'}
# user2 = {'Drama', 'Romance', 'Action'}

user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}

print("공통 관심 장르:", user1 & user2) # 공통 관심 장르: {'Drama', 'Action'}
print("서로 다른 장르:", user1 ^ user2) # 서로 다른 장르: {'SF', 'Romance'}
print("전체 장르:",user1 | user2) # 전체 장르: {'SF', 'Drama', 'Romance', 'Action'}

# set 메서드
s1 = {1,2,3}

# 원소 추가
s1.add(4)
print("원소 추가", s1) # 원소 추가 {1, 2, 3, 4}

# 여러 원소 추가
s1.update((5,6,7))
print("여러 원소 추가", s1) # 여러 원소 추가 {1, 2, 3, 4, 5, 6, 7}

# 원소 제거
s1.remove(4)
print("원소 제거1", s1) # 원소 제거1 {1, 2, 3, 5, 6, 7}
# s1. remove(100) # KeyError: 100 - 존재하지 않는 원소 삭제 시도 시 에러

s1.discard(100)
s1.discard(6)
print("원소 제거2", s1) # 원소 제거2 {1, 2, 3, 5, 7} - 에러가 나지 않음

deleted = s1.pop() # 임의의 값 하나 제거
print("원소 제거3", s1, deleted) # 원소 제거3 {2, 3, 5, 7} 1

# 부분 집합 (subset) 관련 메서드
a = {10,20,30,40,50} # 상위집합
b = {20,30,40} # 부분집합
c = {10,200,300,400,500}

# 부분집합 여부 판단
print(b.issubset(a)) # True
print(a.issubset(b)) # False

# 상위집합 여부 판단
print(a.issuperset(b)) # True
print(b.issuperset(a)) # False

# 공통 원소가 없는지 확인
print(a.isdisjoint(b)) # False
print(a.isdisjoint(c)) # False
print(b.isdisjoint(c)) # True

# 실습 1. set 종합 연습(3)

# 문제 3. 부분집합 관계 판단
# 어떤 유저가 가지고 있는 자격증 목록과 특정 직무에 필요한 자격증 목록이 주어집니다.
# 이 사용자가 지원 자격을 갖추었는지 확인하세요.
# my_certificates = {'SQL', 'Python', 'Linux'}
# job_required = {'SQL', 'Python'}

my_certificates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}

is_qualified = job_required.issubset(my_certificates)
print("지원 자격 충족 여부: ", is_qualified)