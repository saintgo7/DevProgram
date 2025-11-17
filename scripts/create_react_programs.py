#!/usr/bin/env python3
"""
Script to create 100 React programs for DevProgram repository
"""

import os

# Base directory
BASE_DIR = "/home/user/DevProgram/React"

# Program definitions (5 featured programs with full implementations)
FEATURED_PROGRAMS = {
    1: {
        "name": "Hello World",
        "description": "Basic React component",
        "app_content": """import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Hello, React World!</h1>
        <p>Welcome to React - A JavaScript library for building user interfaces</p>
      </header>
    </div>
  );
}

export default App;""",
        "css_content": """.App {
  text-align: center;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}"""
    },
    2: {
        "name": "Counter App",
        "description": "useState hook demonstration",
        "app_content": """import React, { useState } from 'react';
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

export default App;""",
        "css_content": """.App {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.counter-container {
  background: white;
  padding: 3rem;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
  text-align: center;
}

.counter-display {
  font-size: 4rem;
  font-weight: bold;
  color: #667eea;
  margin: 2rem 0;
}

.button-group {
  display: flex;
  gap: 1rem;
  justify-content: center;
}

.btn {
  padding: 1rem 2rem;
  font-size: 1.5rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
  transition: transform 0.2s;
}

.btn:hover {
  transform: scale(1.1);
}

.btn-danger { background-color: #e74c3c; color: white; }
.btn-warning { background-color: #f39c12; color: white; }
.btn-success { background-color: #27ae60; color: white; }"""
    },
    3: {
        "name": "Todo List",
        "description": "State management and list rendering",
        "app_content": """import React, { useState } from 'react';
import './App.css';

function App() {
  const [todos, setTodos] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const addTodo = () => {
    if (inputValue.trim()) {
      setTodos([...todos, { id: Date.now(), text: inputValue, completed: false }]);
      setInputValue('');
    }
  };

  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  const deleteTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  return (
    <div className="App">
      <div className="todo-container">
        <h1>React Todo List</h1>
        <div className="input-group">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && addTodo()}
            placeholder="Enter a task..."
          />
          <button onClick={addTodo}>Add</button>
        </div>
        <ul className="todo-list">
          {todos.map(todo => (
            <li key={todo.id} className={todo.completed ? 'completed' : ''}>
              <span onClick={() => toggleTodo(todo.id)}>{todo.text}</span>
              <button onClick={() => deleteTodo(todo.id)} className="delete-btn">×</button>
            </li>
          ))}
        </ul>
        <div className="stats">
          Total: {todos.length} | Completed: {todos.filter(t => t.completed).length}
        </div>
      </div>
    </div>
  );
}

export default App;""",
        "css_content": """.App {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 2rem;
}

.todo-container {
  background: white;
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
  width: 100%;
  max-width: 500px;
}

.input-group {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.input-group input {
  flex: 1;
  padding: 0.75rem;
  border: 2px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
}

.input-group button {
  padding: 0.75rem 1.5rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
}

.todo-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.todo-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #eee;
  cursor: pointer;
}

.todo-list li.completed span {
  text-decoration: line-through;
  color: #999;
}

.delete-btn {
  background: #e74c3c;
  color: white;
  border: none;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  cursor: pointer;
  font-size: 1.5rem;
}

.stats {
  margin-top: 1rem;
  text-align: center;
  color: #666;
}"""
    },
    4: {
        "name": "useEffect Example",
        "description": "useEffect hook and side effects",
        "app_content": """import React, { useState, useEffect } from 'react';
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

export default App;""",
        "css_content": """.App {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.effect-container {
  background: white;
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
  text-align: center;
}

.section {
  margin: 2rem 0;
  padding: 1.5rem;
  border: 2px solid #f0f0f0;
  border-radius: 10px;
}

.time-display, .counter {
  font-size: 3rem;
  font-weight: bold;
  color: #667eea;
  margin: 1rem 0;
}

button {
  padding: 1rem 2rem;
  font-size: 1.2rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: transform 0.2s;
}

button:hover {
  transform: scale(1.05);
}

.info {
  color: #666;
  font-size: 0.9rem;
  margin-top: 1rem;
}"""
    },
    5: {
        "name": "Form Handling",
        "description": "Form inputs and controlled components",
        "app_content": """import React, { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    age: '',
    country: '',
    terms: false
  });
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  };

  if (submitted) {
    return (
      <div className="App">
        <div className="form-container">
          <h1>Submission Successful!</h1>
          <div className="submitted-data">
            <p><strong>Name:</strong> {formData.name}</p>
            <p><strong>Email:</strong> {formData.email}</p>
            <p><strong>Age:</strong> {formData.age}</p>
            <p><strong>Country:</strong> {formData.country}</p>
          </div>
          <button onClick={() => setSubmitted(false)}>Submit Another</button>
        </div>
      </div>
    );
  }

  return (
    <div className="App">
      <div className="form-container">
        <h1>React Form</h1>
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Name:</label>
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Email:</label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Password:</label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Age:</label>
            <input
              type="number"
              name="age"
              value={formData.age}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label>Country:</label>
            <select name="country" value={formData.country} onChange={handleChange} required>
              <option value="">Select a country</option>
              <option value="USA">USA</option>
              <option value="UK">UK</option>
              <option value="Korea">Korea</option>
              <option value="Japan">Japan</option>
            </select>
          </div>

          <div className="form-group checkbox">
            <label>
              <input
                type="checkbox"
                name="terms"
                checked={formData.terms}
                onChange={handleChange}
                required
              />
              I agree to the terms and conditions
            </label>
          </div>

          <button type="submit">Submit</button>
        </form>
      </div>
    </div>
  );
}

export default App;""",
        "css_content": """.App {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 2rem;
}

.form-container {
  background: white;
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
  width: 100%;
  max-width: 500px;
}

.form-group {
  margin-bottom: 1.5rem;
  text-align: left;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: bold;
  color: #333;
}

.form-group input,
.form-group select {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #ddd;
  border-radius: 8px;
  font-size: 1rem;
}

.form-group.checkbox label {
  display: flex;
  align-items: center;
  font-weight: normal;
}

.form-group.checkbox input {
  width: auto;
  margin-right: 0.5rem;
}

button {
  width: 100%;
  padding: 1rem;
  background: #667eea;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: transform 0.2s;
}

button:hover {
  transform: translateY(-2px);
}

.submitted-data {
  background: #f8f9fa;
  padding: 1.5rem;
  border-radius: 10px;
  margin: 1.5rem 0;
  text-align: left;
}"""
    }
}

# All 100 program titles
ALL_PROGRAMS = [
    "Hello World", "Counter App", "Todo List", "useEffect Example", "Form Handling",
    "Toggle Component", "Conditional Rendering", "List Rendering", "Event Handling", "Props Example",
    "useState Array", "useState Object", "Multiple State", "State Lifting", "Controlled Input",
    "Uncontrolled Input", "Ref Example", "useRef Hook", "Custom Hook", "useContext Example",
    "Theme Switcher", "Modal Component", "Dropdown Menu", "Accordion Component", "Tabs Component",
    "Slider Component", "Rating Component", "Progress Bar", "Loading Spinner", "Tooltip Component",
    "Alert Component", "Badge Component", "Card Component", "Avatar Component", "Button Variants",
    "Input Validation", "Search Filter", "Sorting List", "Pagination", "Infinite Scroll",
    "Dark Mode Toggle", "Local Storage", "Session Storage", "Cookie Manager", "Fetch API",
    "Axios Example", "API Integration", "Error Handling", "Loading States", "Debounce Search",
    "Throttle Example", "Memoization", "useMemo Hook", "useCallback Hook", "React.memo",
    "Performance Optimization", "Code Splitting", "Lazy Loading", "Suspense Example", "Error Boundary",
    "Portal Example", "Fragment Usage", "Key Props", "Spread Props", "Children Props",
    "Render Props", "HOC Pattern", "Compound Components", "Context API", "Reducer Hook",
    "useReducer Example", "Redux-like State", "Form Builder", "Multi-step Form", "File Upload",
    "Image Upload", "Drag and Drop", "Sortable List", "Resizable Panel", "Draggable Modal",
    "Chart Component", "Data Visualization", "Table Component", "Data Grid", "Calendar Component",
    "Date Picker", "Time Picker", "Color Picker", "Range Slider", "Number Input",
    "Currency Input", "Phone Input", "Email Validator", "Password Strength", "Password Toggle",
    "Login Form", "Signup Form", "Auth Context", "Protected Route", "Role-based Access",
    "Notification System", "Toast Messages", "Confirmation Dialog", "Image Gallery", "Carousel Component",
    "Video Player", "Audio Player", "Timer Component", "Stopwatch", "Countdown Timer"
]

def create_package_json(program_num, program_name):
    """Create package.json file"""
    return f'''{{
  "name": "react-program-{program_num:03d}",
  "version": "1.0.0",
  "description": "{program_name}",
  "private": true,
  "dependencies": {{
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-scripts": "5.0.1"
  }},
  "scripts": {{
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }},
  "eslintConfig": {{
    "extends": [
      "react-app"
    ]
  }},
  "browserslist": {{
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }}
}}
'''

def create_index_html():
    """Create public/index.html file"""
    return '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="React application" />
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
'''

def create_index_js():
    """Create src/index.js file"""
    return '''import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
'''

def create_index_css():
    """Create src/index.css file"""
    return '''* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
'''

def create_default_app(program_name):
    """Create default App.js for programs 6-100"""
    return f'''import React from 'react';
import './App.css';

function App() {{
  return (
    <div className="App">
      <div className="container">
        <h1>{program_name}</h1>
        <p>This is a React component demonstrating {program_name.lower()}.</p>
        <p>Implement the component logic here...</p>
      </div>
    </div>
  );
}}

export default App;
'''

def create_default_css():
    """Create default App.css for programs 6-100"""
    return '''.App {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.container {
  background: white;
  padding: 3rem;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3);
  text-align: center;
  max-width: 600px;
}

h1 {
  color: #333;
  margin-bottom: 1rem;
}

p {
  color: #666;
  line-height: 1.6;
  margin: 0.5rem 0;
}
'''

def create_program(program_num):
    """Create a single React program directory with all necessary files"""
    program_name = ALL_PROGRAMS[program_num - 1]
    program_dir = os.path.join(BASE_DIR, f"{program_num:03d}_Program")
    src_dir = os.path.join(program_dir, "src")
    public_dir = os.path.join(program_dir, "public")

    # Create directories
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(public_dir, exist_ok=True)

    # Create package.json
    with open(os.path.join(program_dir, "package.json"), "w") as f:
        f.write(create_package_json(program_num, program_name))

    # Create public/index.html
    with open(os.path.join(public_dir, "index.html"), "w") as f:
        f.write(create_index_html())

    # Create src/index.js
    with open(os.path.join(src_dir, "index.js"), "w") as f:
        f.write(create_index_js())

    # Create src/index.css
    with open(os.path.join(src_dir, "index.css"), "w") as f:
        f.write(create_index_css())

    # Create src/App.js and src/App.css
    if program_num in FEATURED_PROGRAMS:
        featured = FEATURED_PROGRAMS[program_num]
        with open(os.path.join(src_dir, "App.js"), "w") as f:
            f.write(featured["app_content"])
        with open(os.path.join(src_dir, "App.css"), "w") as f:
            f.write(featured["css_content"])
    else:
        with open(os.path.join(src_dir, "App.js"), "w") as f:
            f.write(create_default_app(program_name))
        with open(os.path.join(src_dir, "App.css"), "w") as f:
            f.write(create_default_css())

    print(f"Created program {program_num:03d}: {program_name}")

def main():
    """Main function to create all 100 React programs"""
    print("Creating React programs...")
    print(f"Base directory: {BASE_DIR}")

    # Create base directory
    os.makedirs(BASE_DIR, exist_ok=True)

    # Create all 100 programs
    for i in range(1, 101):
        create_program(i)

    print("\n✓ Successfully created 100 React programs!")
    print(f"Location: {BASE_DIR}")

    # Count total lines
    total_lines = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(('.js', '.jsx', '.css', '.html', '.json')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    total_lines += len(f.readlines())

    print(f"Total lines of code: {total_lines:,}")

if __name__ == "__main__":
    main()
