import './styles/App.css';
import Header from "./components/Header";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Header />
      <Routes>
        <Route path='/' element={<h1>Home</h1>} />
        <Route path='/products' element={<h1>Poducts Page</h1>} />
        <Route 
          path='/products/:productId'
          element = {<h1>Product detail Page</h1>} />
      </Routes>
    </div>
  );
}

export default App;
