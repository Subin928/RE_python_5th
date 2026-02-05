// 실습1. input으로 새로운 알파벳 추가해보기
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

// 실습 2

function PracticeMapFilter2() {
    const [contacts, setContacts] = useState([
        { id: 1, name: 'codi', email: 'codi@gmail.com' },
        { id: 2, name: 'bin', email: 'binee@gmail.com' }]);

    const [inputName, setInputName] = useState('');
    const [inputEmail, setInputEmail] = useState('');

    // 등록 함수
    const addContact = () => {
        if (!inputName || !inputEmail) return; // 빈 값이면 추가 안함

        setContacts([
            ...contacts,  // 기존 배열 복사
        {
            id: contacts.length + 1, // 고유 id 생성
            name: inputName,
            email: inputEmail
        }
        ]);

        setInputName('');   // input 초기화
        setInputEmail('');
    };

    // Enter 키 감지
    const handleKeyPress = (e) => {
        if (e.key === 'Enter') {  // Enter 키를 누르면
            addContact();
        }
    };

    // 삭제 함수 (더블클릭 시)
    const deleteContact = (targetId) => {
        const newContacts = contacts.filter((contact) => contact.id !== targetId);
        setContacts(newContacts);
    };

    return (
        <div>
        {/* 이름, 이메일 입력 */}
        <input
            type="text"
            placeholder="이름"
            value={inputName}
            onChange={(e) => setInputName(e.target.value)}
        />
        <input
            type="text"
            placeholder="이메일"
            value={inputEmail}
            onChange={(e) => setInputEmail(e.target.value)}
            onKeyPress={handleKeyPress}  // Enter 키 감지
        />
        <button onClick={addContact}>등록</button>


        {/* 리스트 출력 */}
        <div>
            {contacts.map((contact) => (
                <p
                    key={contact.id}
                    onDoubleClick={() => deleteContact(contact.id)} // 더블클릭 시 삭제
                >
                    {contact.name}: {contact.email}
                </p>
            ))}
        </div>

        {/* 단축 평가: 연락처가 비었으면 메시지 출력 */}
        {contacts.length === 0 && (
            <span>연락처를 추가해주세요!</span>
            )}
        </div>
    );
}

// 실습 3

const PracticeMapFilter3 = () => {
    const [inputWriter, setInputWriter] = useState('')
    const [inputTitle, setInputTitle] = useState('')
    const [comment, setComment] = useState([
    
    {
        writer: '민수',
        title: '안뇽',
    },
    
    {
        writer: '지민',
        title: '하이하이',
    },
    
    {
        writer: '희수',
        title: '멋쟁이',
    },
])

    const addComment = () => {
        let newComment = {
        writer: inputWriter,
        title: inputTitle,
        }

        // state 추가
        // console.log(...comment);
        setComment([...comment, newComment])
        // comment = [
        //     { writer: xxx, title: xxx },
        //     { writer: xxx, title: xxx },
        //     { writer: xxx, title: xxx },
        //     { writer: xxx, title: xxx },
        // ]

        // // input 초기화
        setInputWriter('')
        setInputTitle('')
    }

    return (
        <div>
            <form>
                <label htmlFor="writer">작성자:</label>
                <input
            id="writer"
            type="text"
            name="writer"
            value={inputWriter}
            onChange={(e) => setInputWriter(e.target.value)}
            />
        
                <label htmlFor="title">제목:</label>
                <input
            id="title"
            type="text"
            name="title"
            value={inputTitle}
            onChange={(e) => setInputTitle(e.target.value)}
            />
                <button type="button" onClick={addComment}>
                    작성
                </button>
            </form>

            <table border={1} style={{ marginTop: '30px', width: '500px' }}>
                <thead>
                    <tr>
                        <th>번호</th>
                        <th>제목</th>
                        <th>작성자</th>
                    </tr>
                </thead>
                <tbody>
                    {comment.map((value, idx) => {
                        return (
                            <tr key={idx + 1}>
                                <td>{idx + 1}</td>
                                <td>{value.title}</td>
                                <td>{value.writer}</td>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </div>
    )
}

export {PracticeMapFilter, PracticeMapFilter2, PracticeMapFilter3};