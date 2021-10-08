<template>
  <div class="post">
    <img :src="post.costume" alt="" />
    <h4>{{ post.content }}</h4>
    <h2>{{ post.claps }}</h2>
    <button @click="deletePost(post.id)">Delete</button>
    <button>clap</button>
  </div>
</template>

<script>
import { DeletePost } from "../services/PostServices";

export default {
  name: "Post",
  props: ["post"],
  methods: {
    async deletePost(id) {
      await DeletePost(id);
    },
  },
};
</script>