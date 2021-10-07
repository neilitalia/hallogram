<template>
  <div class="post">
    <img :src="post.costume" alt="" />
    <h4>{{ post.content }}</h4>
    <h2>{{ post.claps }}</h2>
    <button><Clap /></button>
  </div>
</template>

<script>
import Clap from "../icons/Clap";

export default {
  name: "Post",
  components: { Clap },
  props: ["post"],
};
</script>