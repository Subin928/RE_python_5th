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


<<<<<<< HEAD
# 문제 1 정답

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def change_password(self, old_pw, new_pw):
        if old_pw == self.__password:
            self.__password = new_pw
            print("비밀번호가 변경되었습니다.")

        else:
            print("기존 비밀번호가 일치하지 않습니다.")

    def check_password(self, password):
        return self.__password == password
    
    user = UserAccount("user1", "pass123")
    print(user.username)
    print(user.__password)

    print(user.check_password("pass123"))
    user.change_password("wrongpass", "newpass")


=======
>>>>>>> 4510d2e7e3d1c10940c85e2d43b536d31477f9ef
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

<<<<<<< HEAD
s.score = -10  # ValueError


# 문제 2. 정답

class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property # getter
    def score(self):
        return self.__score
    
    @score.setter # setter
    def score(self, value):
        if 0 <= value <= 100:
            self.__score = value
        else:
            raise ValueError("성적은 0에서 100 사이여야 합니다.")
        
s1 = Student("Alice" , 85)
print(s1.name)
print(s1.score) # 85

s1.score = 105
print(s1.score)



# 상속
# 부모 클래스의 속성과 메서드를 물려받아 새로운 자녀 클래스를 만드는 것

# 상속 기본 문법
# 부모 클래스
class Animal:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("동물이 울음소리를 냅니다.")
    
# 자식 클래스
class Dog(Animal):
    pass

dog = Dog("구름이")
dog.bark()
print(dog.name) # 구름이



# super() 사용

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("동물이 울음소리를 냅니다.")
    
# 자식 클래스
class Dog(Animal):
    def __init__(self, name, age, species):
        # super는 부모를 가리킴
        super().__init__(name, age)
        self.species = species

        # 오버라이딩
        def bark(self):
            super().bark
            print("멍멍")


dog = Dog("구름이", 12, "포메라니안")
dog.bark()
print(dog.name) # 구름이
print(dog.species) # 포메라니안


# 실습 4. 상속과 오버라이딩 연습

# 문제 1. Shape 클래스 오버라이딩

# [Shape 클래스 조건]
# 생성자를 통해 다음 두 값을 초기화하세요:
# 변의 개수 (sides)
# 밑변의 길이 (base)
# printinfo() 메서드를 정의하여 다음과 같이 출력:
# 변의 개수: 4
# 밑변의 길이: 10
# area() 메서드를 정의하여 "넓이 계산이 정의되지 않았습니다."라는 메시지를 출력
# -> 자식 클래스에서 이 메서드를 오버라이딩해야 합니다.

# 부모 클래스
class Shape:
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printinfo(self):
        print(f"변의 개수: {self.sides}")
        print(f"밑변의 길이: {self.base}")
    def area(self):
        print("넓이 계산이 정의되지 않았습니다.")


# [Rectangle 클래스 조건]
# Shape를 상속받습니다.
# 생성자에서 sides, base, height를 모두 초기화합니다.
# area() 메서드를 오버라이딩하여 base * height 값을 출력합니다.

# 자식 클래스 : Rectangle

class Rectangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        area = self.base * self.height
        print(f"{self.sides}각형의 넓이: {area}")


# [Triangle 클래스 조건]
# Shape를 상속받습니다.
# 생성자에서 sides, base, height를 모두 초기화합니다.
# area() 메서드를 오버라이딩하여 (base*height) / 2 값을 출력합니다.

# 자식 클래스 : Triangle

class Triangle(Shape):
    def __init__(self, sides, base, height):
        super().__init__(sides, base)
        self.height = height

    def area(self):
        area = int((self.base * self.height)/2)
        print(f"{self.sides}각형의 넓이: {area}")

# [실행]
# Rectangle과 Triangle 객체를 생성합니다.
# 각 객체에 대해 printinfo()와 area() 메서드를 차례로 호출하세요.

r = Rectangle(4, 10, 5)
r.printinfo()
r.area()

# 변의 개수: 4
# 밑변의 길이: 10
# 4각형의 넓이: 50

print()
t = Triangle(3, 8, 6)
t.printinfo()
t.area()

# 변의 개수: 3
# 밑변의 길이: 8
# 3각형의 넓이: 24



# 추상 클래스 (Abstract Class)
# 클래스의 구조를 정의하는 클래스

from abc import ABC, abstractmethod

class Animal(ABC):
    # 추상 메서드
    @abstractmethod
    def bark(self):
        pass

class Dog(Animal):
    def bark(self):
        print("멍멍")

a = Animal()
a = Dog()
a.bark()



# 실습 5. 추상 클래스 연습 문제

# 문제. 추상 클래스 Payment 구현

# 아래 조건을 만족하는 클래스를 구현하세요.
# 추상 클래스 Payment를 정의하고, pay(amount)를 추상 메서드로 선언하세요. (abc 모듈 사용)
# CardPayment 클래스와 CashPayment 클래스는 Payment를 상속받아 pay() 메서드를 오버라이딩하세요.
# CardPayment: 카드로 {amount}원을 결제합니다. 출력
# CashPayment: 현금으로 {amount}원을 결제합니다. 출력

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def __init__(self):
        # pass
        super().__init__()

    def pay(self, amount):
        print(f"카드로 {amount}원을 결제합니다.")

class CashPayment(Payment):
    def pay(self, amount):
        print(f"현금으로 {amount}원을 결제합니다.")

card = CardPayment()
cash = CashPayment()

card.pay(2000) # 카드로 2000원을 결제합니다.
cash.pay(10000) # 현금으로 10000원을 결제합니다.

