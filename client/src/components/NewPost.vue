<template>
  <div class="NewPost">
    <h1>Create a new post</h1>
    <img
      v-if="uploadPreview"
      :src="uploadPreview"
      alt="Preview"
      class="upload-preview"
    />
    <div class="file-upload">
      <input
        type="file"
        placeholder="costume image"
        accept="image/*"
        @change="handleFileChange"
      />
      <button class="upload" @click="handleFileSend">Upload File</button>
    </div>
    <textarea
      v-model="content"
      name="content"
      cols="30"
      rows="10"
      placeholder="content"
      maxlength="256"
    />
    <p>{{ 256 - content.length }}/256</p>
    <button class="submit" @click="sendPost" :disabled="!content || !costume">
      Submit
    </button>
  </div>
</template>

<script>
import { CreatePost, UploadImage } from "../services/PostServices";
export default {
  name: "NewPost",
  data: () => ({
    content: "",
    costume: null,
    costumeImage: null,
    uploadPreview: null,
  }),
  methods: {
    async sendPost() {
      if (this.content && this.costume && this.costume) {
        const payload = {
          content: this.content,
          costume: this.costume,
          claps: 0,
          user_id: localStorage.getItem("user_id"),
        };
        const res = await CreatePost(payload);
        if (res.status === 201) {
          this.$emit("addPost", res.data);
          this.content = "";
          this.costume = null;
          this.costumeImage = null;
          this.uploadPreview = null;
        }
      }
    },
    handleFileChange(e) {
      const file = e.target.files;
      if (file && file[0]) {
        console.log("file :>> ", file);
        this.costumeImage = file[0];
        const reader = new FileReader();
        reader.onload = (e) => {
          this.uploadPreview = e.target.result;
        };
        reader.readAsDataURL(file[0]);
      }
    },
    async handleFileSend() {
      const formData = new FormData();
      formData.append("file", this.costumeImage);
      const res = await UploadImage(formData);
      if (res.status === 200) {
        this.costume = this.costumeImage.name;
      }
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Creepster&display=swap");

div.NewPost {
  display: flex;
  flex-direction: column;
}
div.file-upload {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.submit,
.upload {
  background-color: #f75f1c;
  color: black;
  font-family: "Creepster", cursive;
}

.NewPost {
  background-image: url("https://cdn.pixabay.com/photo/2019/07/15/07/01/halloween-background-4338710__480.jpg");
  background-repeat: no-repeat;
  background-size: 100%;
  font-family: "Creepster", cursive;
  text-align: center;
  color: #ff9a00;
}
</style>