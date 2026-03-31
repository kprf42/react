import { HashRouter, Routes, Route, Link } from 'react-router-dom';
import Home from './Home';
import House from './House';

function App() {
  return (
    <HashRouter>
      <div>
        <nav>
          <Link to="/">Главная</Link>
          {' | '}
          <Link to="/House">О нас</Link>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/House" element={<House />} />
        </Routes>
      </div>
    </HashRouter>
  );
}

export default App;
