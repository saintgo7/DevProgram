const express = require('express');
const app = express();
app.get('/', (req, res) => res.send('Node.js Program 145'));
app.listen(3000);