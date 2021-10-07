<template>
  <div class="profile"> 
  <div class="profile-details">
  <h3>{{user.name}}</h3>
  <h4>{{user.email}}</h4>
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
    // name: "",
    // email: "",
    posts : [],
    // tipJar : ""
    user: {}
  }),
  mounted: function(){
    this.getUser()
  },
  methods: {
    async getUser() {
      const response = await GetUser(3)
      console.log(response)
      this.user = response
      // this.user.name = this.name
      // this.user.email = this.email
      this.posts = this.user.posts
    }

  }

}
</script>

<style>

</style>