import Vue from "vue";
import App from "./App.vue";
import VueMeta from "vue-meta";
import Vuex from "vuex";
import axios from "axios";

import store from "./store";

import "./assets/css/index.css";
import router from "./router";

Vue.use(Vuex);
Vue.use(VueMeta, { refreshOnceOnNavegation: true });
Vue.config.productionTip = false;

//Adding axios to Vue
Vue.prototype.$http = axios;

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount("#app");
