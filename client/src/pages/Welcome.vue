<template>
  <div>
    <h1>Hallogram is the place to go trick-or-treating online</h1>
    <input v-model="name" type="text" placeholder="name" />
    <input v-model="email" type="text" placeholder="email" />
    <input v-model="tip_jar" type="text" placeholder="tip jar" />
  </div>
</template>

<script>
export default {
  name: "Welcome",
  data: () => ({
    name: "",
    email: "",
    tip_jar: null,
  }),
};
</script>

<style>
</style>