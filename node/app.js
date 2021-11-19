const express = require("express");
const db = require("./db");

// API initialization
const app = express();
db();

// Express configuration
app.use(express.json({ extended: false }));

app.get("/", (req, res) => {
  res.send("This API is running!");
});

// Configuring routes
app.use("", require());

// Server start
app.get("/", (req, res) => {
  res.send("Hello!");
});

var server = app.listen(8081, "localhost");
