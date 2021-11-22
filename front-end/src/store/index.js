import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);
const http = axios.create({
  baseURL: "http://127.0.0.1:5000/",
  timeout: 1000,
});

export default new Vuex.Store({
  state: {
    email: "",
    password: "",
    token: "",
  },
  getters: {},
  mutations: {
    setEmail(state, email) {
      state.email = email;
    },
    setPassword(state, password) {
      state.password = password;
    },
  },
  actions: {
    login() {
      http({
        method: "post",
        url: "/login",
        data: {
          email: this.state.email,
          password: this.state.password,
        },
        responseType: "json",
        headers: {
          "Access-Control-Allow-Origin": "*",
        },
      }).then((response) => {
        console.log(response);
        this.state.token = response.data.token;
      });
    },
  },
});
