<template>
  <nav>
    <p class="link icon">HALLOGRAM</p>
    <router-link class="link home" to="/">Home</router-link>
    <router-link class="link home" to="/profile" v-if="authenticated"
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

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Creepster&display=swap');

.link {
  text-decoration: none;
  font-family: 'Creepster', cursive;
  color:#F75F1C;
}
.link:visited{
  text-decoration: none;
}
.icon {
  font-size: 2rem;
}
.home {
  color: #85e21f;
}
nav{
  display: flex;
  justify-content: space-around;
  align-items: center;
}
</style>

