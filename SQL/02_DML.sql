-- 1. SELECT 기본 문법

-- 모든 컬럼 선택
SELECT * FROM class;

-- 일부 컬럼만 선택
SELECT class_name, category FROM class;

--  2. WHERE
SELECT * FROM student WHERE name = "이지은";
SELECT * FROM student WHERE student_id = 10;

SELECT name, age FROM student WHERE age >= 25;
SELECT name, age FROM student WHERE age >= 25 AND age <= 27;

SELECT name, age FROM student WHERE class_id IN ('CLS01', 'CLS02', 'CLS03');

SELECT * FROM student WHERE name LIKE '이%';

SELECT * FROM class WHERE category LIKE '%엔드';

SELECT * FROM student WHERE join_date LIKE '%04%';

-- 3. ORDER BY 정렬
SELECT name, age FROM student ORDER BY age;
SELECT name, age FROM student ORDER BY age DESC;

SELECT class_id, class_name, start_date FROM class ORDER BY class_name;
SELECT class_id, class_name, start_date FROM class WHERE category LIKE "%엔드%" ORDER BY class_name;

SELECT name, gender FROM student ORDER BY gender, name;

-- 4. LIMIT
SELECT * FROM student LIMIT 3;

SELECT * FROM student ORDER BY age LIMIT 5;

-- 5. 중복 제거
SELECT DISTINCT gender FROM student;

-- 6. GROUP BY, HAVING
USE my_shop;

SELECT cust_id, amount FROM orders ORDER BY cust_id;
SELECT cust_id "고객 아이디", sum(amount) "총 구매 개수" FROM orders GROUP BY cust_id;

SELECT cust_id "고객 아이디", sum(amount * price) "총 구매 금액" FROM orders
GROUP BY cust_id
ORDER BY sum(amount * price) DESC;

SELECT cust_id "고객 아이디", avg(amount) "평균 구매 개수" FROM orders GROUP BY cust_id;

SELECT COUNT(*) FROM customer;

USE codingon_db;
SELECT COUNT(*) "나이가 입력된 수" FROM student WHERE age IS NOT NULL;

SELECT cust_id "고객 아이디", sum(price * amount) "총 구매 금액"
FROM orders
WHERE sum(price * amount) > 370000
GROUP BY cust_id;

SELECT cust_id "고객 아이디", sum(price * amount) "총 구매 금액"
FROM orders
GROUP BY cust_id
HAVING sum(price * amount) > 370000;

SELECT * FROM student;

UPDATE student SET age = 26 WHERE student_id = 1;

UPDATE student SET age = age + 1 WHERE class_id = "CLS01" and age < 25;

SELECT * FROM class;

DELETE FROM class WHERE room LIKE "G%";

-- 실습 SELECT 연습하기

SELECT name, gender 
FROM student 
WHERE age >= 25;

SELECT DISTINCT class_id FROM student;

SELECT name, age FROM student 
WHERE gender='남' 
ORDER BY AGE ASC;

SELECT name, class_id FROM student 
WHERE name LIKE '이%';

SELECT * FROM student 
WHERE AGE IS NULL;

SELECT * FROM student 
WHERE join_date BETWEEN '2024-03-01' AND '2024-04-30';

SELECT * FROM class 
ORDER BY start_date DESC 
LIMIT 3;

SELECT name FROM student 
where class_id IN ('CLS01', 'CLS02', 'CLS03') 
AND (name LIKE '%정%' or name LIKE '%영%');

-- 실습 GROUP BY와 HAVING

SELECT class_id, COUNT(*) student_count
FROM student
GROUP BY class_id;

SELECT gender, AVG(age) avg_age
FROM student
GROUP BY gender;

SELECT gender, AVG(age) avg_age
FROM student
GROUP BY gender
HAVING AVG(age) >= 26;

SELECT class_id, MIN(join_date) first_join
FROM student
GROUP BY class_id;

SELECT class_id, MIN(age) min_age
FROM student
GROUP BY class_id
HAVING MIN(age) >= 25;

SELECT gender, MAX(age)-Min(age) age_gap
FROM student
GROUP BY gender
HAVING (MAX(age)-MIN(age)) >= 3;

SELECT class_id, AVG(age) avg_age
FROM student
GROUP BY class_id
HAVING AVG(age) >= 24
ORDER BY avg_age DESC;












