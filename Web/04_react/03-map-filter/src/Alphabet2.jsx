import { useState } from 'react';

function Alphabet2() {
    const [alphabet, setAlphabet] = useState([]);
    const [inputAlpha, setInputAlpha] = useState('');
    
    const addAlpha = () => {
        if (!inputAlpha) return; // 빈 값이면 추가 안함

        setAlphabet([
            ...alphabet,  // 기존 배열 복사
            {
                id: alphabet.length + 1,  // 고유 id 생성
                alpha: inputAlpha,        // 입력한 알파벳
            },
        ]);

        setInputAlpha('');  // input 초기화
    };

    const deleteAlpha = (targetId) => {
        const newAlpha  = alphabet.filter((alpha) => alpha.id !== targetId);
        setAlphabet(newAlpha);
    };

    return (
        <>
            <input
                type="text"
                placeholder="알파벳 입력"
                value={inputAlpha}  // 제어 컴포넌트
                onChange={(e) => setInputAlpha(e.target.value)}  // 입력값 업데이트
            />
            
            <button onClick={addAlpha}>추가</button>
            
            <ol>
                {alphabet.map((value) => (
                    // 더블클릭 시 해당 id를 deleteAlpha에 전달
                    <li key={value.id} onDoubleClick={() => deleteAlpha(value.id)}>
                        {value.alpha}
                    </li>
                ))}
            </ol>

            {/* 단축 평가: alphabet이 비었으면 메시지 출력 */}
            {alphabet.length === 0 && (
                <span>알파벳을 입력해주세요!</span>
            )}
        </>
    );
}

export default Alphabet2;