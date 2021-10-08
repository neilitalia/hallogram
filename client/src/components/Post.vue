<template>
  <div class="post">
    <img :src="imageBaseUrl + postDetails.costume" alt="" />
    <h4>{{ postDetails.content }}</h4>
    <h2>{{ postDetails.claps }}</h2>
    <button @click="deletePost">Delete</button>
    <button @click="clapPost">clap</button>
  </div>
</template>

<script>
import { ClapPost, DeletePost } from "../services/PostServices";
import { S3_BASE_URL } from "../globals";

export default {
  name: "Post",
  props: ["post"],
  data: () => ({
    imageBaseUrl: S3_BASE_URL,
    postDetails: {},
  }),
  methods: {
    async deletePost() {
      const res = await DeletePost(this.postDetails.id);
      console.log("res :>> ", res);
    },
    async clapPost() {
      const res = await ClapPost(this.postDetails.id);
      if (res.status === 200) {
        this.postDetails = { ...this.postDetails, claps: res.data.claps };
      }
    },
  },
  mounted() {
    this.postDetails = { ...this.post };
  },
};
</script>

<style scoped>
img {
  max-width: 100%;
}
</style>