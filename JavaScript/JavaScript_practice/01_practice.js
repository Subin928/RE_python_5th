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
let mathScore2 = Number(prompt('수학점수 입력'));
let engScore2 = Number(prompt('영어점수 입력'));
let avg = (mathScore2) + (engScore2)/ 2;
console.log(`수학과 영어의 평균 점수는 ${avg}점 입니다.`);

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

