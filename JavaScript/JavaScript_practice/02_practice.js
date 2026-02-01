// 1. DOM 실습(1) - 요소 선택 및 다루기(html 내용 변경하기)

// 주어진 HTML 코드에서 span 요소를 선택하여 JavaScript만 사용해 
// 해당 요소의 텍스트를 ‘맛있다’에서 ‘맛없다’로 변경하고, 
// 글자 색상과 글자 크기를 함께 변경한다. 
// 이때 HTML 구조는 수정하지 않고, script 태그 내부에 
// JavaScript 코드만 작성하여 요소를 선택하고 조작해야 한다.

const spanEl = document.querySelector('span');

spanEl.textContent = '맛없다 ---;;';
spanEl.style.color = 'red';
spanEl.style.fontSize = '32px';
