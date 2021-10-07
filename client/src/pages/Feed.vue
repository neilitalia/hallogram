<template>
  <div class="feed">
    <h3>Feed</h3>
    <NewPost />
  </div>
</template>

<script>
import NewPost from "../components/NewPost.vue";
export default {
  name: "Feed",
  components: { NewPost },
};
</script>

<style>
</style>