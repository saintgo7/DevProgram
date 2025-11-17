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

  "jsonwebtoken": "^9.0.0"
