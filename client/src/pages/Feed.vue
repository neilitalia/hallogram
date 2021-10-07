<template>
  <div class="feed">
    <NewPost :posts="posts" @addPost="addPost" />
    <h3>Feed</h3>
    <div v-for="post in posts" :key="post.id">
      <Post :post="post" />
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
