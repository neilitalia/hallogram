<template>
  <div id="app">
    <header>
      <Nav @signOut="signOut" />
    </header>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import Nav from "./components/Nav.vue";

export default {
  name: "App",
  components: {
    Nav,
  },
  methods: {
    signOut() {
      localStorage.clear();
      this.$router.push("/welcome");
    },
  },
};
</script>

