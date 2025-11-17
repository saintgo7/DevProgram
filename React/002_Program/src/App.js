import React, { useState } from 'react';
import './App.css';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <div className="counter-container">
        <h1>Counter App</h1>
        <div className="counter-display">{count}</div>
        <div className="button-group">
          <button onClick={() => setCount(count - 1)} className="btn btn-danger">
            -
          </button>
          <button onClick={() => setCount(0)} className="btn btn-warning">
            Reset
          </button>
          <button onClick={() => setCount(count + 1)} className="btn btn-success">
            +
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;