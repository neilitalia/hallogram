<template>
  <div class="profile"> 
  <div class="profile-details">
  <h3>{{name}}</h3>
  <h4>{{email}}</h4>
  <h4>{{tipJar}}</h4>
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
export default {
  name: "Profile",
  component: {
    Post
    },
  data: () => ({
    name: "",
    email: "",
    posts : [],
    tipJar : ""
  })
 
}
</script>

<style>

</style>