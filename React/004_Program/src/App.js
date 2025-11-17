import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [time, setTime] = useState(new Date());
  const [count, setCount] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setTime(new Date());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  useEffect(() => {
    document.title = `Count: ${count}`;
  }, [count]);

  return (
    <div className="App">
      <div className="effect-container">
        <h1>useEffect Demo</h1>

        <div className="section">
          <h2>Current Time</h2>
          <div className="time-display">
            {time.toLocaleTimeString()}
          </div>
          <p className="info">Updates every second using useEffect</p>
        </div>

        <div className="section">
          <h2>Counter</h2>
          <div className="counter">{count}</div>
          <button onClick={() => setCount(count + 1)}>Increment</button>
          <p className="info">Check the browser tab title!</p>
        </div>
      </div>
    </div>
  );
}

export default App;