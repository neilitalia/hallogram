<template>
  <div class="feed">
    <div class="new-post">
      <NewPost :posts="posts" @addPost="addPost" />
    </div>
    <h3 class="feed-title">Feed</h3>
    <div class="post-container">
    <div v-for="post in posts" :key="post.id">
      <Post :post="post" />
    </div>
    </div>
  </div>
</template>

<script>
import Post from "../components/Post.vue";
import { GetPosts } from "../services/PostServices";
import NewPost from "../components/NewPost.vue";

export default {
  name: "Feed",
  components: {
    Post,
    NewPost,
  },
  data: () => ({
    posts: [],
  }),
  mounted: function () {
    this.getPosts();
  },
  methods: {
    async getPosts() {
      const res = await GetPosts();
      this.posts = res.reverse();
    },
    addPost(post) {
      this.posts.unshift(post);
    },
  },
};
</script>

<style>
  body {
    background-color: rgb(0,0,0);
  }
  .feed-title {
    color: #ff9a00;
    text-align: center;
    font-size: 3vh;
  }
  .new-post {
    height: 8%;
    width: 60%;
    margin: auto;
    margin-top: 5vh;
    border: 5px solid #881ee4;
    padding: 4rem;
    padding-left: 10rem;
    padding-right: 10rem;
    border-radius: 8px;
  }
  .post-container {
    width: 60%;
    margin: auto;
    margin-top: 3vh;
    margin-bottom: 100vh;
    border: 3px solid #85e21f;
    border-radius: 8px;
    padding: 5rem;
    padding-left: 10rem;
    padding-right: 10rem;
  }
</style>
