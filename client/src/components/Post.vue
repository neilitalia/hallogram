<template>
  <div class="post">
    <img :src="imageBaseUrl + postDetails.costume" alt="" />
    <div class="content">
      <h2>{{ postDetails.content }}</h2>
      <h4>{{ postDetails.claps }} claps</h4>
      <!-- <h4 v-if="postDetails.user.name">by {{ postDetails.user.name }}</h4> -->
    </div>
    <button class="delete" @click="deletePost">Delete</button>
    <button class="clap" @click="clapPost">clap</button>
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
@import url("https://fonts.googleapis.com/css2?family=Creepster&display=swap");
.post {
  display: flex;
  flex-direction: column;
  border-radius: 8px;
  cursor: pointer;
  background-color: #efbd76;
  transition: all 0.2s ease;
  margin-bottom: 10px;
}
.delete:hover {
  opacity: 0.7;
}
.clap:hover {
  opacity: 0.7;
}
.content {
  background-color: white;
  margin: 1em;
}

h4,
h2 {
  text-align: center;
}
.delete,
.clap {
  background-color: #f75f1c;
  color: black;
  font-family: "Creepster", cursive;
  width: 20%;
  margin: auto;
  margin-bottom: 5px;
}

img {
  max-width: 50%;
  max-height: 500px;
  margin: 0 auto;
  padding: 1em;
}
</style>