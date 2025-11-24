# 클래스 (class)
# - 데이터와 기능을 하나로 묶는 구조
# - 개념적(기능적)으로 유사한 관계에 있는 것들을 묶어줌

# 클래스 기본 문법
# 클래스의 정의

class ClassName:
    # 생성자(constructor) : 인스턴스(객체)가 생성될 때 호출
    # 인스턴스 변수를 초기화, 기본 상태 설정
    # 하나의 클래스에서 하나만 정의 가능
    def __init__(self, name):
        # self : 인스턴스 자기 자신을 가리킴
        self.name = name
        self.age = 0

    # (인스턴스) 메서드
    def method_name(self):
        print(f"이 인스턴스의 이름은 {self.name}입니다.")

# 인스턴스 생성
my_instance = ClassName("I1")
print(my_instance.name) # I1
my_instance.method_name() # 이 인스턴스의 이름은 I1입니다.

another_instance = ClassName("I2")
another_instance.method_name() # 이 인스턴스의 이름은 I2입니다.

# 실습 1. class 기본 문법 연습

# 문제 1. 책 클래스 만들기

# Book 클래스를 정의하세요.
# 인스턴스 변수로 title, author, total_pages, current_page를 가집니다.
# 메서드
# read_page(pages) : 현재 페이지를 읽음. 총 페이지 수를 넘지 않도록 처리.
# progress() : 전체에서 얼마나 읽었는지를 퍼센트(%)로 소수점 1자리까지 출력

class Book:
    def __init__(self, title, author, total_pages):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = 0

    def read_page(self, pages):
        self.current_page += pages
        if self.current_page > self.total_pages:
            self.current_page = self.total_pages

    def progress(self):
        percent = self.current_page/self.total_pages * 100
        print(f"{percent:.1f}%")

b = Book("파이썬","코딩온",100)
b.read_page(20)
b.progress()

# 20.0%

# 정답

class Book:
    def __init__(self, title, author, total_pages, current_page):
        self.title = title
        self.author = author
        self.total_pages = total_pages
        self.current_page = current_page

    def read_page(self, pages):
        self.current_page += pages

        if self.current_page > self.total_pages:
            self.current_page = self.total_pages
            print("책을 끝까지 다 읽었어요.")

    def progress(self):
        percent = (self.current_page / self.total_pages) * 100
        print(f"현재 읽은 분량: {percent: .1f}%")

book1 = Book("넥서스", "유발 하라리", 500, 1)
book1.read_page(50)
book1.progress()  # 현재 읽은 분량:  10.2%

book1.read_page(500)
book1.progress() # 책을 끝까지 다 읽었어요.
                 # 현재 읽은 분량:  100.0%

# 문제 2. Rectangle 클래스 구현

# 다음 조건에 맞는 Rectangle 클래스를 작성해 보세요.
# 인스턴스 변수 : width, height
# 메서드: 
# area() : 사각형의 넓이 반환
# 사용자 입력:
# 프로그램 실행 시 사용자로부터 가로(width)와 세로(height) 값을 입력 받아 객체를 생성하고 are() 메서드를 호출하여 넒이를 출력

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
w = int(input("가로 길이: "))
h = int(input("세로 길이: "))

rect = Rectangle(w, h)
print("사각형의 넓이: ", rect.area())

# 가로 길이: 4
# 세로 길이: 5
# 사각형의 넓이:  20


# 클래스 변수
# - 클래스가 가지고 있는 변수
# - 모든 인스턴스가 공유할 수 있음
class Dog:
    # 클래스 변수
    kind = "강아지"

    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

dog1 = Dog("포메라니안", "리치", 12)
dog2 = Dog("비숑", "구름", 10)

print("인1", dog1.kind) # 인1 강아지
print("인2", dog2.kind) # 인2 강아지
print("클래스", Dog.kind) # 클래스 강아지



# 클래스 메서드
# 클래스 자체를 대상으로 동작하는 메서드
# 클래스 데이터를 조작하는데 사용

class Book2:
    book_count = 0

    def __init__(self, title, author):
        Book2.book_count += 1
        self.title = title
        self.author = author

    # 클래스 메서드
    @classmethod  # 데코레이터
    def get_count(cls):
        print(f"현재 {cls.book_count}권의 책을 가지고 있다.")

book1 = Book2("B1", "author1")
book2 = Book2("B2", "author2")
Book2.get_count() # 현재 2권의 책을 가지고 있다.



# 정적 메서드
# - 클래스나 인스턴스의 데이터를 조작하지 않는 클래스 함수
# - 클래스나 인스턴스의 상태에 의존하지 않는 일반 함수
# - 개념적으로는 클래스와 연관이 있으나, 클래스나 인스턴스의 데이터를 조작하지 않음

class OperationTool:

    @staticmethod # 데코레이터
    def add(a, b):
        return a + b
    
OperationTool.add(10, 20)
print(OperationTool.add(10, 20)) # 30


# 실습 2. 클래스 변수, 메서드 연습

# 문제 1. User 클래스 구현

# User 클래스를 정의하세요.
# 인스턴스 변수 : username, points (초기값은 0)
# 클래스 변수 : total_users (생성된 유저 수 저장)
# 메서드
# add_points(amount) : 포인트 추가
# get_level() : 포인트 기준으로 레벨 변환 (0~99 : Bronze, 100~499 : Silver, 500이상 : Gold)
# 클래스 메서드 : get_total_users() -> 총 유저 수 출력

class User:
    total_users = 0

    def __init__(self, username, points):
        self.username = username
        self.points = points
        User.total_users += 1

    def add_points(self, amount):
        self.points += amount

    def get_level(self):
        if self.points >= 500:
            return "Gold"
        elif self.points >= 100:
            return "Silver"
        else:
            return "Bronze"
        
    @classmethod
    def get_total_users(cls):
        print(f"총 유저 수 : {cls.total_users}")


u1 = User("Bin", 70)
u2 = User("Jenny", 300)
print(u1.get_level()) # Bronze
print(u2.get_level()) # Silver

User.get_total_users() # 총 유저 수 : 2



# 접근 제어와 정보 은닉
# 데이터 무결성을 보호하기 위함
# 코드 안정성을 향상시키기 위함

class Person2:
    def __init__(self, name, age):
        # public
        self.name = name
        # private : 언더바(__) 두 개를 변수 앞에 붙여서 정의
        self.__age = age


p1 = Person2("lee", 15)
print(p1.name) # lee
print(p1.__age) # AttributeError: 'Person2' object has no attribute '__age'


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # getter
    def get_age(self):
        return self.__age
    
    # setter
    def set_age(self, value):
        if value > 120 or value < 0:
            print("유효하지 않은 나이입니다.")
        else:
            self.__age = value


p1 = Person2("lee", 15)
print(p1.name)         # lee
print(p1.get_age())    # 15
p1.set_age(-10)        # 유효하지 않은 나이입니다.



# @property 데코레이터
# - 메서드를 속성처럼 보이게 만들어주는 데코레이터

class Ex:
    def __init__(self):
        self.__value = 0

    # getter
    @property
    def value(self):
        return self.__value
    
    # setter
    @value.setter
    def value(self,val):
        if val < 0:
            print("유효하지 않은 값입니다.")
        else:
            self.__value = val
        
ex1 = Ex()
print(ex1.value) # 0
ex1.value = 100
print(ex1.value) # 100
ex1.value = -100 # 유효하지 않은 값입니다.

# 실습 3. 접근 제어와 정보은닉 연습

# 문제 1. UserAccount 클래스 : 비밀번호 보호
# UserAccount 클래스를 정의하세요.
# 인스턴스 변수:
# username : 사용자 이름
# __password : private 변수로, 비밀번호 저장
# 생성자에서 사용자 이름과 비밀번호를 초기화하세요
# 다음 메서드를 정의하세요
# change_password(old_pw, new_pw): 현재 비밀번호가 old_pw와 같을 때만 변경 허용, 틀리면 "비밀번호 불일치" 출력
# check_password(password): 비밀번호 일치 여부를 반환 (True/False)

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_pw, new_pw):
        if self.__password == old_pw:
            self.__password = new_pw
        else:
            print("비밀번호 불일치")

user = UserAccount("lee", "1234")

print(user.check_password("1234")) # True
print(user.check_password("0000")) # False

user.change_password("1234","abcd")
user.change_password("9999","new") # 비밀번호 불일치

print(user.check_password("abcd")) # True


# 문제 2. Student 클래스 : 성적 검증(@property 사용)
# Student 클래스를 정의하세요.
# 인스턴스 변수 __score는 private으로 선언합니다.
# score에 대한 getter/setter를 @property를 사용하여 정의하세요.
# 점수는 0 이상 100 이하만 허용되며, 범위를 벗어나면 ValueError를 발생시킵니다.(raise ValueError 사용)

class Student:
    def __init__(self, score):
        self.__score = score

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError
        
s = Student(90)
print(s.score) # 90

s.score = 100
print(s.score) # 100

s.score = -10  # ValueError