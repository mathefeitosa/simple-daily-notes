const express = require("express");
const router = express.Router();
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const config = require("../config");


const User = require("../models/User");
const Note = require('../models/Note')

//---------------------------- UTILITY FUNCTIONS -------------------------------
// function that returns JWT
const check_token = (token) => {
  try {
    payload = jwt.verify(token, config.SECRET_KEY)
    user = payload.user
    return user
  }
  catch (error) {
    res.status(401).json({ msg: "Token is not valid!" });
    return false
  }
};
//------------------------------------------------------------------------------

/**
 * @method        POST
 * @route         /note
 * @description   create note
 * @access        public
 */
router.post("/", async (req, res) => {
  const { date, token } = req.body;
  
  user = check_token(token)

  try {
    //Verifying note existance
    let note = await Note.findOne({ date:date, user_id:user.id });
    if (user) {
      return res.status(400).json({ errors: { msg: "Essa nota já existe." } });
    }

    //creating note
    note = new Note({
      user_id,
      text,
    });
    
    await note.save();
    return res.status(200).json({ msg: 'Nota criada.'})

  } catch (error) {
    console.error(error.message);
    res.status(500).send("Internal server error!");
  }
});

/**
 * @method        POST
 * @route         /login
 * @description   user authentication
 * @access        public
 */
router.post("/", async (req, res) => {
  const { email, password } = req.body;

  try {
    //finding the user
    let user = await User.findOne({ email });
    if (!user) {
      return res
        .status(400)
        .json({ errors: [{ msg: "Usuário inexistente." }] });
    }

    //verify if the passwords match
    match = await bcrypt.compare(password, user.password);
    if (!match) {
      return res
        .status(400)
        .json({ errors: [{ msg: "Usuário/senha incorretos." }] });
    }

    //retornando o JWT
    return {
      user,
      generate_token(user)
    };
  } catch (error) {}
});

module.exports = router;
