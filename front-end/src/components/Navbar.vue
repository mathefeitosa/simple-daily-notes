<template>
  <div>
    <router-link to="/Login">Login</router-link> |
    <router-link to="/">Notes</router-link> |
    <router-link to="/about">About</router-link>
  </div>
</template>

<script>
  export default {
    name: "Navbar",
    data() {
      return {
        iconClass: "duration-200 transform hover:scale-105",
      };
    },
  };
</script>
