<template>
  <nav>
    <router-link to="/">Home</router-link>
    <router-link to="/profile" v-if="authenticated"
      >{{ name }}'s Profile</router-link
    >
    <button v-if="authenticated" @click="signOut">Sign Out</button>
  </nav>
</template>

<script>
export default {
  name: "Nav",
  data: () => ({
    authenticated: false,
    name: "",
  }),
  mounted: function () {
    const authenticated = localStorage.getItem("authenticated");
    if (authenticated) {
      this.name = localStorage.getItem("name");
      this.authenticated = true;
    }
  },
  methods: {
    signOut() {
      this.authenticated = false;
      this.name = "";
      this.$emit("signOut");
    },
  },
};
</script>