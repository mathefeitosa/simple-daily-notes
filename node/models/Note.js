const mongoose = require("mongoose");

const NoteSchema = new mongoose.Schema("Note", {
  date: {
    type: Date,
    required: true,
  },
  text: {
    type: String,
    required: true,
  },
  user_id: {
    type: mongoose.Schema.Types.ObjectId,
    ref: "User",
    required: true,
  },
  created: Date.now(),
});

module.exports = {
  Note: mongoose.model("Note", NoteSchema),
  NoteSchema: NoteSchema,
};
