let str = "   Hello JavaScript World    ";

console.log("원본 str", str);

// .length
console.log('길이: ', str.length); // 함수 X, 하나의 속성

// .trim: 공백 제거
console.log('공백 제거:', str.trim()); // 앞 뒤 공백 사라짐
console.log("원본 str", str); // 원본 변경 X

// 대소문자 변환
console.log('대문자 변환:', str.toUpperCase()); //     Hello JavaScript World    
console.log("원본 str", str); // 원본 변경 X

console.log('대문자 변환:', str.toLowerCase()); //    hello javascript world    
console.log("원본 str", str); // 원본 변경 X

// 탐색
console.log('글자 인덱스 찾기:', str.indexOf('J')); // 9
console.log('단어 인덱스 찾기:', str.indexOf('Java')); // 9 -> 매개변수로 받은 문자열의 첫 번째 글자 인덱스 반환
console.log('없는 단어 인덱스 찾기:', str.indexOf('Jva')); // -1 -> 매개변수로 받은 문자열이 없다면 -1 반환

console.log('문자열의 포함 여부 확인:', str.includes('Java')) // true -> 불리언으로 반환
// .indesOf()로도 문자열에 포함 여부 알 수 있음 -> -1 반환하면 없다는 의미
console.log('문자열의 포함 여부 확인:', str.includes('Jva')) // false

// 슬라이싱
console.log('슬라이싱:', str.slice(6, 16)); // lo JavaScr -> 6번 인덱스부터 15번 인덱스 문자열까지 출력
console.log("원본 str", str); // 원본 변경 X

// 치환
console.log('한 글자 치환', str.replace('a', 'e')); // Hello JevaScript World -> 문자열 중에서 가장 처음 나오는 a라는 문자를 e로 치환
console.log('한 단어 치환:', str.replace('World', 'universe')); // Hello JavaScript universe -> 단어도 치환 가능
console.log('전부 치환:', str.replaceAll('l', 'v')); // Hevvo JavaScript Worvd 
console.log("원본 str", str); // 원본 변경 X

// 분할
console.log('"" 기준 분할:', str.split('')); // ''(공백)을 매개변수로 전달 시 문자열의 모든 글자들이 하나씩 짤려서 배열로 반환
console.log('" " 기준 분할:', str.split(' ')); // " "(공백 한 칸)을 기준으로 문자열을 나눠서 배열로 반환
                                      // ['', '', '', 'Hello', 'JavaScript', 'World', '', '', '', '']

// 분할하는 기준인 매개변수는 사라지고 배열로 만들어져서 반환
console.log('l 기준 분할:', str.split('l')); // ['   He', '', 'o JavaScript Wor', 'd    ']

console.log("원본 str", str); // 원본 변경 X

// 합치기
let str2 = "with JavaScript";
console.log("문자열 합치기:", str.concat(str2)); //     Hello JavaScript World    with JavaScript

console.log(`문자열 합치기 2: ${"Hello ". concat(str2)}`); // Hello with JavaScript
console.log(`문자열 합치기 3: ${"Hello ". concat(str2, str)}`); // Hello with JavaScript   Hello JavaScript World    
console.log(`문자열 합치기 4: ${"Hello ".concat("I'm Subin", " nice to meet you")}`); //  Hello I'm Subin nice to meet you

console.log("원본 str", str); // 원본 변경 
console.log("원본 str2", str2); // 원본 변경 X