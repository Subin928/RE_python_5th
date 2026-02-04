// 실습. input으로 새로운 알파벳 추가해보기
// map과 input으로 구현
// onChange 이벤트로 값의 변경 감지 -> state 변수값이 변경되게끔 만들기

import { useState } from 'react';

function PracticeMapFilter() {
    const [alphabet, setAlphabet] = useState(['a', 'b', 'c']);
    const [inputValue, setInputValue] = useState('');

    const addAlpha = () => {
        if (!inputValue) return;
        
        setAlphabet([...alphabet, inputValue]);
        setInputValue('');
        };

        return (
        <div>
            <input
            type="text"
            placeholder="알파벳 입력"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)} 
            />
            
            <button onClick={addAlpha}>추가</button>
            
            <ol>
                {alphabet.map((value, idx) => (
                    <li key={idx}>{value}</li>))}
            </ol>
        </div>
        );
    }

export default PracticeMapFilter;