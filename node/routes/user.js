const express = require("express");
const router = express.Router();
const bcrypt = require("bcrypt");
const jwt = require("jsonwebtoken");
const config = require("../config");
const User = require("../models/User");

//---------------------------- UTILITY FUNCTIONS -------------------------------
// function that returns JWT
const generate_token = (user) => {
  jwt.sign(
    {
      user: {
        id: user.id,
      },
    },
    config.SECRET_KEY,
    { expiresIn: 3600 },
    (error, token) => {
      if (error) throw error;
      return token;
    }
  );
};
//------------------------------------------------------------------------------

/**
 * @method        POST
 * @route         /users
 * @description   register user
 * @access        public
 */
router.post("/", async (req, res) => {
  const { email, password } = req.body;

  try {
    //Verifying user existance
    let user = await User.findOne({ email });
    if (user) {
      return res.status(400).json({ errors: { msg: "Usuário já existe." } });
    }

    user = new User({
      email,
      password,
    });

    //Ecrypting password
    user.password = await bcrypt.hash(password, await bcrypt.genSalt(10));

    //creating user
    await user.save();

     //retornando o JWT
    return {
      user,
      generate_token(user)
    };
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
