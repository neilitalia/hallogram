<template>
  <div class="profile"> 
  <div class="profile-details">
  <h3>{{name}}</h3>
  <h4>{{email}}</h4>
  <!-- <h4>{{user.tipJar}}</h4> -->
  </div>
  <div class="post-container">
    <div v-for="post in posts" :key="post.id">
    <Post :post="post"/>
    </div>
  </div>
  </div>
  
</template>

<script>
import Post from "../components/Post.vue"
import {GetUser} from '../services/UserServices'

export default {
  name: "Profile",
  component: {
    Post
    },
  data: () => ({
    name: "",
    email: "",
    posts : [],
    // tipJar : ""
    user: {}
  }),
  methods: {
    async getUser() {
      this.user = await GetUser()
      this.user.name = this.name
      this.user.email = this.email
      this.user.posts = this.posts
    }
  }

}
</script>

<style>

</style>