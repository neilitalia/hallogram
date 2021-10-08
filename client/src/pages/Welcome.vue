<template>
  <div>
    <h1>Hallogram is the place to go trick-or-treating online</h1>
    <form v-on:submit.prevent="createUser">
      <input v-model="name" type="text" placeholder="name" />
      <input v-model="email" type="email" placeholder="email" />
      <input v-model="tip_jar" type="text" placeholder="tip jar" />
      <button type="submit">Submit</button>
    </form>
    <h2>Already a user?</h2>
    <p>Enter your email:</p>
    <input type="email" v-model="verifyEmail" />
    <button @click="getUser" :disabled="!this.verifyEmail">Verify</button>
    <p v-if="!found">User not found :(</p>
  </div>
</template>

<script>
import { CreateUser, VerifyUser } from "../services/UserServices";
export default {
  name: "Welcome",
  data: () => ({
    name: "",
    email: "",
    tip_jar: null,
    verifyEmail: "",
    found: true,
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
          this.storeUserData(res.data);
        }
      }
    },
    async getUser() {
      if (this.verifyEmail) {
        const payload = {
          user_email: this.verifyEmail,
        };
        const res = await VerifyUser(payload);
        if (res.data.msg === "user not found") {
          this.found = false;
        } else {
          this.storeUserData(res.data);
        }
      }
    },
    storeUserData(data) {
      localStorage.setItem("name", data.name);
      localStorage.setItem("email", data.email);
      localStorage.setItem("tip_jar", data.tip_jar);
      localStorage.setItem("user_id", data.id);
      localStorage.setItem("authenticated", true);
      this.$router.push("/");
    },
  },
};
</script>

<style>
</style>