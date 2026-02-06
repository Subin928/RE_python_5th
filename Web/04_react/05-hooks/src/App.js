import './App.css';
import CssModule from './components/CssMkdule';
import StyledComponent from './components/StyledComponent';
// import Faq from './components/Faq';
// import UseMemoEx from './components/UseMemo';

function App() {
  return (
    <div className="App">
      {/* <UseMemoEx />

      <hr />
      <Faq /> */}

      <hr />
      {/* CSS Styling */}
      <CssModule />

      {/* Styled Component */}
      <h2>Styled-components</h2>
      <StyledComponent />
    </div>
    
  );
}

export default App;
