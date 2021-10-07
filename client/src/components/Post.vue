<template>
  <div class="post">
    <img :src="post.costume" alt="">
    <h4>{{post.content}}</h4>
    <h2>{{post.claps}}</h2>
  
  </div>
</template>

<script>
export default {
  name: 'Post',
  props: [
    'post'
  ]
}
</script>