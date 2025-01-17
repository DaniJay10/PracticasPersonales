import logo from './logo.svg';
import './App.css';
import { PrimerComponente } from './components/PrimerComponente';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Primer proyecto react</p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> 
        <PrimerComponente />
        <PrimerComponente />
      </header>
    </div>
  );
}

export default App;
