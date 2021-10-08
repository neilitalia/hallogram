<template>
  <div>
    <h1>Hallogram is the place to go trick-or-treating online</h1>
    <form v-on:submit.prevent="createUser">
      <input v-model="name" type="text" placeholder="name" />
      <input v-model="email" type="email" placeholder="email" />
      <input v-model="tip_jar" type="text" placeholder="tip jar" />
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import { CreateUser } from "../services/UserServices";
export default {
  name: "Welcome",
  data: () => ({
    name: "",
    email: "",
    tip_jar: null,
  }),
  methods: {
    async createUser() {
      if (this.name && this.email) {
        const payload = {
          name: this.name,
          email: this.email,
          tip_jar: this.tip_jar,
        };
        const res = await CreateUser(payload);
        if (res.status === 201) {
          localStorage.setItem("name", res.data.name);
          localStorage.setItem("email", res.data.email);
          localStorage.setItem("tip_jar", res.data.tip_jar);
          localStorage.setItem("user_id", res.data.id);
          localStorage.setItem("authenticated", true);
          this.$router.push("/");
        }
      }
    },
  },
};
</script>

<style>
</style>