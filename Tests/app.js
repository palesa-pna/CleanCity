// app.js
const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
  res.status(200).json({ message: 'Welcome to the API' });
});

module.exports = app; // ✅ Export the app for testing