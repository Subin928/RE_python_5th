import './App.css';
import FunctionComponent from './FunctionComponent';
import Button from './Button';
import {Practice1, Practice2, Practice3} from './Practice_react';
import Counter from './Counter';

function App() {
  return (
    <div className="App">
      <FunctionComponent name='로이' age='10' />
      <FunctionComponent />

      <hr />
      <Button link='https://www.google.com'>Google</Button>

      {/* 실습 1 */}
      <Practice1 food="치킨" /> {/* food 있음 -> 치킨 */}
      <Practice1 /> {/* food 없음 -> 기본값 치킨 */}

      {/* 실습 2 */}
      <Practice2
        title = "모순"
        author = "양귀자"
        price = "11,700"
        type = "소설"
        />

      <hr/>
      <h2>useState 활용</h2>
      <Counter />

      {/* 실습 3 */}
      <Practice3 />

    </div>
  );
}

export default App;
