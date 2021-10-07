<template>
  <div class="feed">
    <NewPost />
    <h3>Feed</h3>
    <div v-for="post in posts" :key="post.id">
      <Post :post="post" />
    </div>
  </div>
</template>

<script>
import Post from "../components/Post.vue";
import { GetPosts } from "../services/PostServices";
import NewPost from '../components/NewPost.vue'

export default {
  name: "Feed",
  components: {
    Post,
    NewPost
  },
  data: () => ({
    posts: [],
  }),
  mounted: function () {
    this.getPosts();
  },
  methods: {
    async getPosts() {
      this.posts = await GetPosts();
      console.log(this.posts);
    },
  },
};
</script>
