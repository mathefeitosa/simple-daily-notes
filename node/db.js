const mongoose = require("mongoose");

const URI =
  "mongodb+srv://admin:admin@cluster0.uxp4g.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

const db = async () => {
  try {
    mongoose.connect(URI, {
      useNewUrlParser: true,
      useUnifiedTopology: true,
      useCreateIndex: true,
    });
    console.log("MongoDB connected!");
  } catch (error) {
    console.log(error.message);
  }
};

module.exports = db;
