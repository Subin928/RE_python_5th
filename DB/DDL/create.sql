-- 인코딩 지정
CREATE DATABASE test_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE test_db;

CREATE TABLE user (
	user_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(10) NOT NULL,
    address VARCHAR(45),
    join_date DATE
);

SHOW TABLES;
DESC user;

CREATE DATABASE my_shop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE my_shop;

CREATE TABLE customer (
	cust_id CHAR(10) NOT NULL PRIMARY KEY,
    cust_name VARCHAR(10) NOT NULL,
    address CHAR(10) NOT NULL,
    phone CHAR(11),
    birth DATE
);

SHOW TABLES;
DESC customer;

CREATE TABLE orders (
	order_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    cust_id CHAR(10) NOT NULL,
    prod_name CHAR(6) NOT NULL,
    price INT NOT NULL,
    amount smallint NOT NULL,
    
    FOREIGN KEY (cust_id) REFERENCES my_shop.customer(cust_id)
);

SHOW TABLES;
DESC orders;

-- ALTER
-- 1. 속성 추가
ALTER TABLE user ADD age INT;
-- 2. 컬럼 자료형 수정
ALTER TABLE user MODIFY address VARCHAR(40);
-- 3. 컬럼 이름 수정
ALTER TABLE user RENAME COLUMN address TO user_address;
-- 4. 컬럼 삭제
ALTER TABLE user DROP age;

-- DDL 실습

-- 1. 실습용 데이터베이스 university_db 생성
CREATE DATABASE university_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- 2. students 테이블
CREATE TABLE students (
  student_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  major VARCHAR(30),
  advisor_id INT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 3. professors 테이블
CREATE TABLE professors (
  professor_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE,
  department VARCHAR(30),
  mentee_id INT,
  joined_at DATE
);

-- 4. 다음 관계가 만족되어야 함
-- 4.1. students.advisor_id는 professors.professor_id 참조 (교수 정보가 삭제되면 해당 학생의 advisor_id)는 NULL로 설정
ALTER TABLE students
ADD CONSTRAINT fk_students_advisor
FOREIGN KEY (advisor_id)
REFERENCES professors(professor_id)
ON DELETE SET NULL;

-- 4.2 professors.mentee_id는 students.student_id를 참조 (학생 정보가 삭제되면 해당 교수의 mentee_id도 NUll로 설정)
ALTER TABLE professors
ADD CONSTRAINT fk_professors_mentee
FOREIGN KEY (mentee_id)
REFERENCES students(student_id)
ON DELETE SET NULL;

DESC students;
DESC professors