import { useState } from 'react';

function Alphabet() {
    const list = ['a', 'b', 'c', 'd', 'e'];

    const [alphabet, setAlphabet] = useState(['b', 'a', 'n', 'a', 'n', 'a']);

    const addAlpha = () => {
        const newAlpha = alphabet.concat('a')
        setAlphabet(newAlpha);
    };
    return (
        <>
            {/* <ol>
                {list.map((value, idx) => {
                    return ( <li key={idx}>{value}</li>)
                })}
            </ol> */}
            
            <input type='text' placeholder='알파벳 입력' />
            <button onClick={addAlpha}>추가</button>
            <ol>
                {alphabet.map((value, idx) => {
                    return ( <li key={idx}>{value}</li>)
                })}
            </ol>
            
        </>

    );
}

export default Alphabet;