const mongoose = require("mongoose");

const UserSchema = new mongoose.Schema("User", {
  email: {
    type: String,
    required: true,
  },
  password: {
    type: String,
    required: true,
  },
});

module.exports = {
  User: mongoose.model("User", NoteSchema),
  UserSchema: UserSchema,
};
