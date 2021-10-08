<template>
  <div id="app">
    <header>
      <Nav @signOut="signOut" />
    </header>
    <main>
      <router-view @checkRegistration="checkRegistration" />
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
  mounted: function () {
    this.checkRegistration();
  },
  methods: {
    signOut() {
      localStorage.clear();
      this.$router.push("/welcome");
    },
    checkRegistration() {
      const authenticated = localStorage.getItem("authenticated");
      if (!authenticated) {
        this.$router.push("/welcome");
      }
    },
  },
};
</script>

