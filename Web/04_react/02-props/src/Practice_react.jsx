import { useState } from "react";

// 실습 1
// 1. 본인이 좋아하는 음식을 소개하는 문구 작성
// 2. food라는 props 생성
// 3. props 기본값을 설정하여 food에 값이 없을 때도 기본값이 출력되게
// 4. food props만 빨간색 출력되도록 설정

const Practice1 = (props) => {
    const { food = '치킨' } = props;

    return (
    <div>
        <p>
            제가 좋아하는 음식은{' '}
        <span style={{ color: 'red' }}>{food}</span>입니다.
        </p>
    </div>
    );
}

// 실습 2

const Practice2 = ({title, author, price, type}) => {
    return (
        <div className="book">
            <h1 className="book-title">이번주 베스트셀러</h1>
            <img 
                src="https://image.yes24.com/goods/8759796/XL" 
                alt="책 표지" 
            />
            <h2>{title}</h2>
            <div className="book-info">
                <p>저자: {author}</p>
                <p>판매가: {price}원</p>
                <p>구분: {type}</p>
            </div>
        </div>
    );
};

// 실습 3
// 1. 함수형 컴포넌트를 만들기
// 2. 숫자의 초깃값은 0으로 설정
// 3. increase라는 함수를 만들고 1씩 증가하는 역할
// 4. decrease라는 함수를 만들고 2씩 감소하는 역할

const Practice3 = () => {
    const [number, setNumber] = useState(0);

    const increase = () => {
        setNumber(number + 1);
    };

    const decrease = () => {
        setNumber(number - 2);
    };

    return (
        <div>
            <h1>{number}</h1>
            <button onClick={increase}>+1</button>
            <button onClick={decrease}>-2</button>
        </div>
    );
};

export {Practice1, Practice2, Practice3};
