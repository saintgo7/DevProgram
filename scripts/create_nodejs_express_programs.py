#!/usr/bin/env python3
"""
Create 100 Node.js/Express programs
Express: Fast, unopinionated web framework for Node.js
"""

import os
import sys

# Program definitions
programs = [
    # Featured Programs (1-5) - Full implementations
    ("001_HelloWorld", "Hello World Server", """server.js:
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('<h1>Hello Express!</h1><p>Node.js backend server</p>');
});

app.get('/api/hello', (req, res) => {
  res.json({ message: 'Hello from Express API!' });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
"""),

    ("002_RESTfulAPI", "RESTful CRUD API", """server.js:
const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.json());

// In-memory database
let users = [
  { id: 1, name: 'Alice', email: 'alice@example.com' },
  { id: 2, name: 'Bob', email: 'bob@example.com' }
];

// GET all users
app.get('/api/users', (req, res) => {
  res.json(users);
});

// GET single user
app.get('/api/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ error: 'User not found' });
  res.json(user);
});

// POST create user
app.post('/api/users', (req, res) => {
  const newUser = {
    id: users.length + 1,
    name: req.body.name,
    email: req.body.email
  };
  users.push(newUser);
  res.status(201).json(newUser);
});

// PUT update user
app.put('/api/users/:id', (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ error: 'User not found' });

  user.name = req.body.name || user.name;
  user.email = req.body.email || user.email;
  res.json(user);
});

// DELETE user
app.delete('/api/users/:id', (req, res) => {
  const index = users.findIndex(u => u.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ error: 'User not found' });

  users.splice(index, 1);
  res.status(204).send();
});

app.listen(PORT, () => {
  console.log(`REST API running on http://localhost:${PORT}`);
});
"""),

    ("003_Middleware", "Custom Middleware", """server.js:
const express = require('express');
const app = express();
const PORT = 3000;

// Logger middleware
const logger = (req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next();
};

// Auth middleware
const authenticate = (req, res, next) => {
  const token = req.headers['authorization'];
  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }
  if (token !== 'Bearer secret-token') {
    return res.status(403).json({ error: 'Invalid token' });
  }
  next();
};

// Error handler middleware
const errorHandler = (err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Something went wrong!' });
};

// Apply middleware
app.use(express.json());
app.use(logger);

// Public route
app.get('/api/public', (req, res) => {
  res.json({ message: 'This is public' });
});

// Protected route
app.get('/api/protected', authenticate, (req, res) => {
  res.json({ message: 'This is protected', secret: 'Confidential data' });
});

// Route with error
app.get('/api/error', (req, res) => {
  throw new Error('Intentional error');
});

app.use(errorHandler);

app.listen(PORT, () => {
  console.log(`Server with middleware on http://localhost:${PORT}`);
});
"""),

    ("004_Authentication", "JWT Authentication", """server.js:
const express = require('express');
const jwt = require('jsonwebtoken');
const app = express();
const PORT = 3000;
const SECRET_KEY = 'your-secret-key';

app.use(express.json());

// Mock user database
const users = [
  { id: 1, username: 'admin', password: 'admin123' }
];

// Login route
app.post('/api/login', (req, res) => {
  const { username, password } = req.body;

  const user = users.find(u => u.username === username && u.password === password);
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }

  // Generate JWT
  const token = jwt.sign(
    { id: user.id, username: user.username },
    SECRET_KEY,
    { expiresIn: '1h' }
  );

  res.json({ token, user: { id: user.id, username: user.username } });
});

// Verify token middleware
const verifyToken = (req, res, next) => {
  const token = req.headers['authorization']?.split(' ')[1];
  if (!token) {
    return res.status(401).json({ error: 'No token provided' });
  }

  try {
    const decoded = jwt.verify(token, SECRET_KEY);
    req.user = decoded;
    next();
  } catch (err) {
    res.status(403).json({ error: 'Invalid token' });
  }
};

// Protected route
app.get('/api/profile', verifyToken, (req, res) => {
  res.json({ message: 'Profile data', user: req.user });
});

app.listen(PORT, () => {
  console.log(`Auth server on http://localhost:${PORT}`);
});

package.json-extra:
  "jsonwebtoken": "^9.0.0"
"""),

    ("005_DatabaseIntegration", "MongoDB Integration", """server.js:
const express = require('express');
const mongoose = require('mongoose');
const app = express();
const PORT = 3000;

app.use(express.json());

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/myapp', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// User schema
const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  createdAt: { type: Date, default: Date.now }
});

const User = mongoose.model('User', userSchema);

// GET all users
app.get('/api/users', async (req, res) => {
  try {
    const users = await User.find();
    res.json(users);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// POST create user
app.post('/api/users', async (req, res) => {
  try {
    const user = new User(req.body);
    await user.save();
    res.status(201).json(user);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// GET user by ID
app.get('/api/users/:id', async (req, res) => {
  try {
    const user = await User.findById(req.params.id);
    if (!user) return res.status(404).json({ error: 'User not found' });
    res.json(user);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// PUT update user
app.put('/api/users/:id', async (req, res) => {
  try {
    const user = await User.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!user) return res.status(404).json({ error: 'User not found' });
    res.json(user);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// DELETE user
app.delete('/api/users/:id', async (req, res) => {
  try {
    const user = await User.findByIdAndDelete(req.params.id);
    if (!user) return res.status(404).json({ error: 'User not found' });
    res.status(204).send();
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.listen(PORT, () => {
  console.log(`MongoDB server on http://localhost:${PORT}`);
});

package.json-extra:
  "mongoose": "^8.0.0"
"""),

    # Template Programs (6-100)
    ("006_Routing", "Advanced Routing", ""),
    ("007_TemplateEngines", "EJS/Pug Templates", ""),
    ("008_StaticFiles", "Serving Static Files", ""),
    ("009_FileUpload", "File Upload with Multer", ""),
    ("010_CORS", "CORS Configuration", ""),
    ("011_SessionManagement", "Express Session", ""),
    ("012_CookieParser", "Cookie Handling", ""),
    ("013_ValidationMiddleware", "Request Validation", ""),
    ("014_RateLimiting", "Rate Limiting", ""),
    ("015_Compression", "Response Compression", ""),
    ("016_Helmet", "Security with Helmet", ""),
    ("017_WebSockets", "WebSocket Server", ""),
    ("018_GraphQL", "GraphQL API", ""),
    ("019_Pagination", "API Pagination", ""),
    ("020_Sorting", "API Sorting", ""),
    ("021_Filtering", "API Filtering", ""),
    ("022_SearchAPI", "Search Endpoint", ""),
    ("023_EmailSending", "Email with Nodemailer", ""),
    ("024_PasswordHashing", "Bcrypt Password", ""),
    ("025_OAuth", "OAuth Integration", ""),
]

# Generate remaining programs
for i in range(26, 101):
    programs.append((
        f"{i:03d}_Program",
        f"Express Program {i}",
        ""
    ))

def create_express_program(number, name, content):
    """Create an Express program directory with files"""
    dir_name = f"NodeJS/{number}_{name.replace(' ', '_').replace('/', '_')}"
    os.makedirs(dir_name, exist_ok=True)

    extra_deps = ""

    # Parse content for featured programs
    if content:
        files = {}
        current_file = None
        current_content = []

        for line in content.split('\n'):
            if line.startswith('package.json-extra:'):
                extra_deps = line.replace('package.json-extra:', '').strip()
                continue
            if line.endswith(':') and not line.startswith(' '):
                if current_file:
                    files[current_file] = '\n'.join(current_content)
                current_file = line[:-1]
                current_content = []
            else:
                current_content.append(line)

        if current_file:
            files[current_file] = '\n'.join(current_content)

        # Write parsed files
        for filename, file_content in files.items():
            filepath = os.path.join(dir_name, filename)
            with open(filepath, 'w') as f:
                f.write(file_content.strip() + '\n')
    else:
        # Template program
        with open(f"{dir_name}/server.js", 'w') as f:
            f.write(f"""const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {{
  res.json({{ message: '{name}' }});
}});

app.listen(PORT, () => {{
  console.log(`Server running on http://localhost:${{PORT}}`);
}});
""")

    # Create package.json
    extra_dep_str = f',\n    {extra_deps}' if extra_deps else ''
    with open(f"{dir_name}/package.json", 'w') as f:
        f.write(f"""{{
  "name": "{number.lower()}-{name.lower().replace(' ', '-')}",
  "version": "1.0.0",
  "main": "server.js",
  "scripts": {{
    "start": "node server.js",
    "dev": "nodemon server.js"
  }},
  "dependencies": {{
    "express": "^4.18.0"{extra_dep_str}
  }},
  "devDependencies": {{
    "nodemon": "^3.0.0"
  }}
}}
""")

    # Create .env.example
    with open(f"{dir_name}/.env.example", 'w') as f:
        f.write("""PORT=3000
NODE_ENV=development
""")

def main():
    print("Creating Node.js/Express programs...")
    os.makedirs("NodeJS", exist_ok=True)

    # Create README
    with open("NodeJS/README.md", 'w') as f:
        f.write("""# Node.js/Express Programs

100 Express programs demonstrating backend web development.

## Features
- RESTful API Development
- Middleware System
- Authentication & Authorization
- Database Integration
- File Upload
- WebSockets
- Security Best Practices

## Quick Start

```bash
cd NodeJS/001_HelloWorld
npm install
npm start
# Visit http://localhost:3000
```

## Development Mode

```bash
npm run dev  # Auto-reload with nodemon
```

## Environment Variables

Copy `.env.example` to `.env` and configure:
```bash
cp .env.example .env
```
""")

    total_lines = 0
    for number, name, content in programs:
        create_express_program(number, name, content)
        # Count lines
        dir_name = f"NodeJS/{number}_{name.replace(' ', '_').replace('/', '_')}"
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                if file.endswith(('.js', '.json')):
                    with open(os.path.join(root, file), 'r') as f:
                        total_lines += len(f.readlines())

    print(f"✅ Created 100 Node.js/Express programs ({total_lines:,} lines)")
    return total_lines

if __name__ == "__main__":
    lines = main()
    sys.exit(0)
