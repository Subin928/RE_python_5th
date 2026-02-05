import { useState } from "react";

// 실습 1 - 이벤트 핸들링
// 01
// 글자색의 초기값은 검정색으로 설정해주세요
// 02
// 그림과 같이 "빨간색" 버튼과 "파란색" 버튼을 만들어주세요.
// 03
// 각 버튼을 클릭할 시 글의 내용과 색이 해당 버튼의 값으로 변경되도록 해주세요.
const Practice1 = () => {
  let [textcolor, changeColor] = useState({ color: "black", text: "검정색" });

  const setColor = (color, obj) => {
    changeColor({ color: color, text: obj.innerText });
  };

  return (
    <>
      <h4 style={{ color: textcolor.color }}>{textcolor.text} 글씨</h4>
      <button
        onClick={(e) => {
          setColor("red", e.target);
        }}
      >
        빨간색
      </button>
      <button
        onClick={(e) => {
          setColor("blue", e.target);
        }}
      >
        파란색
      </button>
    </>
  );
};


// 실습 2
// 아래 그림과 같은 기능을 만들어주세요.

const Practice2 = () => {
  let [display, changeDisplay] = useState(true);

  const setDisplay = () => {
    changeDisplay(!display);
  };

  return (
    <>
      <button onClick={setDisplay}>{display ? "사라져라" : "보여라"}</button>
      {display && <h4>안녕하세요</h4>}
    </>
  );
};

export { Practice1, Practice2};