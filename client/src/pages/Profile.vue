<template>
  <div class="profile">
    <h3 class="profile-title">Profile</h3>
    <div class="profile-details">
      <h4>User Name: {{ user.name }}</h4>
      <h4>Email: {{ user.email }}</h4>
      <h4>Tip Jar: {{ user.tip_jar }}</h4>
    </div>
    <h3 class="profile-title">Posts</h3>
    <div class="post-container">
      <div v-for="post in user.posts" :key="post.id">
        <Post :post="post" :author="user.name" />
      </div>
    </div>
  </div>
</template>

<script>
import Post from "../components/Post.vue";
import { GetUser } from "../services/UserServices";

export default {
  name: "Profile",
  components: {
    Post,
  },
  data: () => ({
    user: {},
  }),
  mounted: function () {
    this.$emit("checkRegistration");
    this.getUser();
  },
  methods: {
    async getUser() {
      const userId = localStorage.getItem("user_id");
      if (userId) {
        const response = await GetUser(userId);
        console.log(response);
        this.user = response;
      }
    },
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Creepster&display=swap");

.profile-details {
  color: white;
  text-align: center;
  font-size: 2vh;
}
.profile-title {
  color: #ff9a00;
  text-align: center;
  margin: 4rem;
  font-size: 3vh;
  font-family: "Creepster", cursive;
}
</style>