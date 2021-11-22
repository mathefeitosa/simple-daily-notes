<template>
  <div class="flex place-content-center">
    <div class="bg-gray-100 space-y-3 p-10 rounded-lg">
      <input
        class="block rounded-lg"
        type="text"
        v-model="email"
        placeholder="email"
      />
      <input
        class="block rounded-lg"
        type="password"
        v-model="password"
        placeholder="senha"
      />
      <div
        @click="login"
        type="button"
        class="block rounded-lg bg-gray-300 hover:bg-blue-200 p-2"
        placeholder="senha"
      >
        {{ $store.state.token }}
        Login
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Login",
    data() {
      return {
        email: "",
        password: "",
      };
    },
    methods: {
      login() {
        this.$store.dispatch("login");
      },
    },
    watch: {
      email() {
        this.$store.commit("setEmail", this.email);
      },
      password() {
        this.$store.commit("setPassword", this.password);
      },
    },
  };
</script>
