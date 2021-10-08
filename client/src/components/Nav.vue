<template>
  <nav>
    <router-link to="/">Feed</router-link>
    <router-link to="/profile">{{ name }}'s Profile</router-link>
    <button @click="signOut">Sign Out</button>
  </nav>
</template>

<script>
export default {
  name: "Nav",
  data: () => ({
    name: "",
  }),
  mounted: function () {
    this.name = localStorage.getItem("name");
  },
  methods: {
    signOut() {
      this.$emit("signOut");
    },
  },
};
</script>