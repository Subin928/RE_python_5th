// 1. object 변수 선언 실습

const mongryong = {
    name: "이몽룡",
    age: 18,
    like: ["강아지", "고양이"],
    isMarried: true,
    girlfriend: {
        name: "성춘향",
        age: 16,
    },
};

console.log(mongryong);

//  2. 형 변환 실습
// 변수 mathScore, engScore를 만들어 주세요.
// mathScore="77"; engScore="88";
// 시험 점수 평균을 계산하여 avgScore에 저장하고,
// 이를 console.log(avgScore)를 이용해서 콘솔창에서 확인하는프로그램을 작성해보세요
// 형 변환을 사용하여 평균 점수가 정확하게 나와야 합니다

let mathScore = "77";
let engScore = "88";

let avgScore = (Number(mathScore) + Number(engScore)) / 2;

console.log("수학", mathScore.toString() + "점");
console.log("영어", engScore.toString() + "점");
console.log("평균", avgScore + "점");


// 3. 성적 평균 구하는 프로그램 만들기

// prompt로 입력받은 값은 string 타입 값을 number로 형변환해서 변수에 저장
// let mathScore2 = Number(prompt('수학점수 입력'));
// let engScore2 = Number(prompt('영어점수 입력'));
// let avg = (mathScore2) + (engScore2)/ 2;
// console.log(`수학과 영어의 평균 점수는 ${avg}점 입니다.`);

// 3. 함수 만들기1
// multifly() 함수를 함수 선언문 형식으로 만들어주세요
// 조건
//  - 매개변수로 두 개의 숫자를 입력받기
//  - 두 인자의 곱을 '반환'하는 함수를 정의
// 콘솔창에 출력하고 싶다면 아래처럼 테스트
//  console.log(multifly(3, 7));
//  console.log(multifly(2, 2));

function multifly(a, b) {
    return a * b
}

console.log(multifly(3, 7));
console.log(multifly(2, 2));

// 3. 함수 만들기2
// square() 함수를 함수 표현식을 이용해서 만들어주세요
// 조건
//  - 매개변수로 하나의 숫자를 입력받기
//  - 입력받은 수의 제곱을 콘솔창에 출력하는 함수 정의
// 콘솔창에 출력하고 싶다면 아래처럼 테스트 해보기
//  square(4);
//  square(11);
//  square(5);

const square = (x) => {
  x = Number(x);
  return x ** 2;
};

// 4. if문 실습
// if문을 이용해서 console창에 연령대별 단어 출력해보기!
// age 변수 선언, prompt로 입력받기
// age가 20이상: 성인
// age가 17 이상: 고등학생
// age가 14 이상: 중학생
// age가 8 이상: 초등학생
// age가 0 이상: 유아

// let age = Number(prompt('나이를 입력하세요'));

// if (age >= 20) {
//     console.log('성인');
// } else if (age >= 17) {
//     console.log('고등학생');
// } else if (age >= 14) {
//     console.log('중학생');
// } else if (age >= 8) {
//     console.log('초등학생');
// } else if (age >= 0) {
//     console.log('유아');
// }

// 5. 삼항연산자 실습
// let now = new Date().getHours();
// 위의 코드는 현재 '시간'만을 받아오는 코드
// 0~23까지의 숫자를 반환하고 0이 자정, 12가 정오를 뜻한다
// now라는 변수에는 현재 시간에 대한 숫자가 저장이 되어있다
// 삼항연산자로 지금이 오전인지 오후인지 콘솔창에 출력

// let now = new Date().getHours();
// console.log('현재시간', now);

// now < 12 ? console.log('오전') : console.log('오후');

// 6. 반복문 실습 - 배수 찾기
// 10000까지의 숫자 중에서
// 13의 배수이면서 홀수인 숫자 찾기
// prompt를 이용해서 입력받은 수까지 13의 배수면서 홀수인 숫자를 찾는 프로그램 만들기

for (let i = 1; i <= 10000; i++) {
    if (i % 13 === 0 && i % 2 === 1) {
    console.log(i);
    }
}

// 추가) prompt 사용
// let num = Number(prompt('범위 입력'));

// console.log(`1~${num}의 숫자 중 13의 배수이면서 홀수인 숫자 구하기`);

// for (let i = 1; i <= num; i++) {
//     if (i % 13 === 0 && i % 2 === 1) {
//     console.log(i);
//     }
// }

// 7. 이중 for문 실습 - 구구단 출력

// console.log('구구단');

// for (let i = 1; i < 10; i++) {
//    console.log(`=== ${단} ===`);
//    for (let j = 1; j < 10; j++) {
//        console.log(`${i} X ${j} = ${i * j}`);
//    }
//}

// 8. 0~100의 숫자 중에서 2 또는 5의 배수 총합 구하기
// 힌트
// 나머지 연산자 % 사용

console.log('=== 2 또는 5의 배수 총합 ===');

let total = 0; // 합
let count = 0; // for문에서 i 역할 (반복 횟수)

while (count <= 100) {
    if (count % 2 === 0 || count % 5 === 0) {
        total += count;
    }
    count++;
}

console.log('0`100까지의 총합', total);

// 9. 내장 메소드 실습문제1 - 배열과 반복문 실습
// 1~100 까지의 배열을 for문을 사용해서 만들기
// 그리고 해당 배열의 합을
// for문
// for of문
// forEach문

let numbers =[];
for (let i = 1; i <= 100; i++) {
    numbers.push(i);
}

// for문
let sum1 = 0;
for (let i = 1; i <= 100; i++) {
    sum1 += numbers[i];
}
console.log(sum1);

// for of문
let sum2 = 0;
for (let num of numbers) {
    sum2 += num;
}
console.log(sum2);

// forEach문
let sum3 = 0;
numbers.forEach((num) => {
    sum3 += num;
});
console.log(sum3);

// reduce
let sum4 = numbers.reduce((acc, cur) => acc + cur);

// 10. 내장 메소드 실습문제2 - 내장 메소드 실습
// 참고)) fruits1은 fruits2를 포함하고 있습니다
let fruits1 = ['사과', '딸기', '파인애플', '수박', '참외','오렌지', '자두', '망고'];
let fruits2 = ['수박', '사과', '참외', '오렌지', '파인애플', '망고'];

// 두 배열에서 동일한 요소만을 가지는 배열 same 만들기
let same = fruits1.filter((fruit) => fruits2.includes(fruit));
console.log(same);

// 두 배열에서 서로 다른 요소만을 가지는 배열 diff 만들기
let diff = fruits1.filter((fruit) => !fruits2.includes(fruit));
console.log(diff);

// 11. 내장 객체 실습문제 - 주말과 평일
// JS에 내장된 Date 객체 활용
// Date.getDay(): 요일별로 0~6(일~토)로 숫자 반환
let nowDay = new Date().getDay();

// switch문
switch (nowDay) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5: 
        console.log("평일");      
        break;
    case 0:
    case 6:
        console.log("주말");
        break;
    default:
        console.log("몰라요");
        break;
}

// if - else문
if (nowDay === 0 || nowDay === 6) {
    console.log("주말");
} else {
    console.log("평일");
}

// 삼항연산자
let today = nowDay === 0 || nowDay === 6 ? '주말' : '평일';
console.log(today);

// 12. 내장 객체 실습문제 - 난수 생성
// 0~10 사이의 랜덤한 숫자를 출력
// 0과 10은 포함해서 뽑음
// Math.random(): 0이상 1미만의 난수 생성
// Math.floor(x): 양수 기준으로는 소수점 버림, 음수 기준으로는 더 작은 음수로 소수점 사라짐

// Math.random() * 10의 결과는 0이상 10미만 결과 출력
// 실습 조건은 10을 포함해야 함 -> Math.random() * 11
console.log(Math.floor(Math.random() * 11));
