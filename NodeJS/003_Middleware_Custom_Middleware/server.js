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
