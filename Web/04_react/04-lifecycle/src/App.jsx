import './App.css';
import LifeCycleFunc from './LifeCycleFunc';
import PostList from './PostList';
import { Practice1, Practice2 } from './PracticeLifeCycle';

function App() {
  return (
    <div className="App">
      <LifeCycleFunc />
      <PostList />

      {/* 실습 */}
      <Practice1 />
      <Practice2 />
    </div>
  );
}

export default App;
