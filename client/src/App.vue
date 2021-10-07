<template>
  <div id="app">
    <header><Feed/></header>
    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>

import Feed from "./pages/Feed.vue"
export default {
  name: 'App',
  components: {
    Feed
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
