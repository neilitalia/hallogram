<template>
  <div>
    <h1 class="auth-title">Hallogram is the place to go trick-or-treating online</h1>
    <form v-on:submit.prevent="createUser">
      <input class="auth-input" v-model="name" type="text" placeholder="name" />
      <input class="auth-input" v-model="email" type="email" placeholder="email" />
      <input class="auth-input" v-model="tip_jar" type="text" placeholder="tip jar" />
      <div class="auth-button">
      <button class="button" type="submit">Submit</button>
      </div>
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
  .auth-input {
    display: block;
    margin: auto;
    height: 4vh;
    width: 40%;
    margin-top: 1vh;
    margin-bottom: 1vh;
  }
  .auth-title {
    color: #ff9a00;
    text-align: center;
    margin: 5ch;
  }
  .auth-button {
    display: flex;
    justify-content: center;
  }
  .button {
    display:inline-block;
    background-color: #881ee4;
    padding:0.5em 3em;
    border:0.16em solid #881ee4;
    box-sizing: border-box;
    text-decoration:none;
    font-weight:400;
    color: white;
    text-align:center;
  }
  .button:hover{
    color: #85e21f;
  }
</style>