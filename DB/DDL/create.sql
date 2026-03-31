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
    
    FOREIGN KEY (cust_id) REFERENCES customer(cust_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
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
USE university_db;

-- 2. students 테이블
CREATE TABLE students (
	student_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    major VARCHAR(30),
    advisor_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 3. professors 테이블
CREATE TABLE professors (
	professor_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department VARCHAR(30),
    mentee_id INT,
    joined_at DATE
);

-- 4. 다음 관계가 만족되어야 함
-- 4.1. students.advisor_id는 professors.professor_id 참조 (교수 정보가 삭제되면 해당 학생의 advisor_id)는 NULL로 설정
ALTER TABLE students
ADD
CONSTRAINT fk_advisor
FOREIGN KEY (advisor_id)
REFERENCES professors(professor_id)
ON DELETE SET NULL;

-- 4.2 professors.mentee_id는 students.student_id를 참조 (학생 정보가 삭제되면 해당 교수의 mentee_id도 NUll로 설정)
ALTER TABLE professors
ADD
CONSTRAINT fk_mentee
FOREIGN KEY (mentee_id)
REFERENCES students(student_id)
ON DELETE SET NULL;
-- on delete, update의 기본값 : restrict
-- on update restrict

DESC students;
DESC professors;



-- INSERT
insert into customer (cust_id, cust_name, address, phone, birth) 
values ('C001', '김민수', '서울시', '01012345678', '1990-05-14');
insert into customer values ('C002', '이영희', '부산시', '01023456789', '1985-08-22');

INSERT INTO customer (cust_id, cust_name, address, phone, birth) VALUES
('C003', '박철수', '대전시', '01034567890', '1992-11-02'),
('C004', '정유진', '광주시', '01045678901', '1998-01-19'),
('C005', '한지민', '수원시', '01056789012', '1996-06-30'),
('C006', '최우성', '서울시', '01067890123', '1989-03-15'),
('C007', '장윤아', '대구시', '01078901234', '1994-10-05'),
('C008', '오태식', '인천시', '01089012345', '1987-02-25'),
('C009', '류수정', '서울시', '01090123456', '1995-07-08'),
('C010', '배진영', '부산시', '01001234567', '1993-12-12');

INSERT INTO orders (cust_id, prod_name, price, amount) VALUES
('C001', '커피머신', 120000, 1),
('C003', '노트북', 950000, 1),
('C002', '헤드폰', 85000, 2),
('C001', '모니터', 250000, 1),
('C005', '의자', 130000, 1),
('C004', '키보드', 45000, 2),
('C007', '마우스', 32000, 3),
('C009', '조명등', 28000, 1),
('C008', '휴대폰', 990000, 1),
('C010', '게임기', 480000, 1);

select * from customer;
select * from orders;

select address as ads from customer;
select c.address from customer as c;


-- 실습 DDL 종합연습 및 INSERT

DROP DATABASE IF EXISTS codingon_db;
CREATE DATABASE codingon_db
DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE codingon_db;

CREATE TABLE class (
	class_id CHAR(5) PRIMARY KEY NOT NULL,
	class_name VARCHAR(30) NOT NULL,
    category VARCHAR(20),
    room CHAR(5) NOT NULL,
    start_date DATE
);

CREATE TABLE student (
	student_id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(20) NOT NULL,
    age INT,
    gender ENUM('남', '여'),
    class_id CHAR(5) NOT NULL,
    join_date DATE,
    
    FOREIGN KEY (class_id) REFERENCES class(class_id)
);

INSERT INTO class (class_id, class_name, category, room, start_date) VALUES
('CLS01', '프론트엔드 12기', '프론트엔드', 'B-101', '2024-01-08'),
('CLS02', '백엔드 8기', '백엔드', 'B-102', '2024-02-05'),
('CLS03', 'AI 엔지니어 3기', 'AI', 'C-201', '2024-03-01'),
('CLS04', '모바일 앱 개발 5기', '모바일', 'A-301', '2024-04-10'),
('CLS05', 'UI/UX 디자인 6기', '디자인', 'D-401', '2024-05-15'),
('CLS06', '데이터 분석 2기', '데이터분석', 'B-201', '2024-06-03'),
('CLS07', '클라우드 인프라 1기', '클라우드', 'E-102', '2024-06-24'),
('CLS08', '게임 프로그래밍 4기', '게임개발', 'G-301', '2024-07-15');

INSERT INTO student (name, age, gender, class_id, join_date) VALUES
('정국', 25, '남', 'CLS01', '2024-01-08'),
('장원영', 21, '여', 'CLS01', '2024-01-09'),
('변우석', NULL, '남', 'CLS02', '2024-02-05'),
('고윤정', 24, '여', 'CLS02', '2024-02-06'),
('안유진', 23, '여', 'CLS03', '2024-03-01'),
('이도현', 26, '남', 'CLS03', '2024-03-02'),
('박채영', NULL, '여', 'CLS04', '2024-04-10'),
('박보검', 29, '남', 'CLS04', '2024-04-11'),
('이지은', NULL, '여', 'CLS05', '2024-05-15'),
('오해원', 22, '여', 'CLS05', '2024-05-16');

select * from class;
select * from student;