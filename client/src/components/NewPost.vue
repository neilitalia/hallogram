<template>
  <div>
    <h1>Create a new post</h1>
    <form v-on:submit.prevent="sendPost">
      <input type="text" placeholder="costume image" accept="image/*" />
      <input
        type="file"
        placeholder="costume image"
        @change="handleFileChange"
      />
      <button @click="handleFileSend">Upload File</button>
      <textarea
        v-model="content"
        name="content"
        cols="30"
        rows="10"
        placeholder="content"
        maxlength="256"
      />
      <p>{{ 256 - content.length }}/256</p>
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import { CreatePost } from "../services/PostServices";
export default {
  name: "NewPost",
  data: () => ({
    content: "",
    costume: null,
    costumeImage: null,
    user_id: 1,
  }),
  methods: {
    async sendPost() {
      if (this.content && this.costume && this.user_id) {
        const payload = {
          content: this.content,
          costume: this.costume,
          claps: 0,
          user_id: localStorage.getItem("user_id"),
        };
        const res = await CreatePost(payload);
        if (res.status === 201) {
          console.log("res :>> ", res.data);
          this.$emit("addPost", res.data);
        }
      }
    },
    handleFileChange(e) {
      this.costumeImage = e.target.files[0];
    },
    handleFileSend() {},
  },
};
</script>

<style scoped>
h1 {
  text-align: center;
}
form {
  display: flex;
  flex-direction: column;
}
</style>