const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => {
  res.json({ message: 'EJS/Pug Templates' });
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
