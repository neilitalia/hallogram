<template>
  <div class="feed">
    <h3>Feed</h3>
    <div v-for="post in posts" :key="post.id">
      <Post :post="post"/>
    </div>
  </div>
</template>

<script>
import Post from '../components/Post.vue'
import {GetPosts} from '../services/PostServices'

export default {
  name: "Feed",
  components: {
    Post
  },
  data: () => ({
    posts: []
  }),
  mounted: function(){
    this.getPosts()
  },
  methods: {
    async getPosts(){
    this.posts = await GetPosts()
    console.log(this.posts)
  }
}}
</script>
