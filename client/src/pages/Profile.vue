<template>
  <div class="profile">
    <div class="profile-details">
      <h3>{{ user.name }}</h3>
      <h4>{{ user.email }}</h4>
      <h3>{{ user.tip_jar }}</h3>
      <!-- <h4>{{user.tipJar}}</h4> -->
    </div>
    <div class="post-container">
      <div v-for="post in user.posts" :key="post.id">
        <Post :post="post" />
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
    this.getUser();
  },
  methods: {
    async getUser() {
      const response = await GetUser(localStorage.getItem("user_id"));
      console.log(response);
      this.user = response;
    },
  },
};
</script>

<style>
</style>