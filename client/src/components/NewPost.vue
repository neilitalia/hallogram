<template>
  <div>
    <h1>Create a new post</h1>
    <form v-on:submit.prevent="sendPost">
      <input v-model="costume" type="text" placeholder="costume" />
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
    user_id: 1,
  }),
  methods: {
    async sendPost() {
      if (this.content && this.costume && this.user_id) {
        const payload = {
          content: this.content,
          costume: this.costume,
          claps: 0,
          user_id: this.user_id,
        };
        const res = await CreatePost(payload);
        if (res.status === 201) {
          console.log("res :>> ", res.data);
          this.$emit("addPost", res.data);
        }
      }
    },
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