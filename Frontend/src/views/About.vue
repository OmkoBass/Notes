<template>
  <h1> About </h1>
  <h2> This is a beginner notes App with Vue3 and Django </h2>

  <div class="p-d-flex p-flex-column vertical-container">
    <Button
        class="p-mb-2"
        label="Log in"
        @click="this.$router.push('/login')"
    />

    <Button
        @click="this.$router.push('/signup')"
        label="Sign up"
    />
  </div>
</template>

<script>
  import Button from 'primevue/button';

  export default {
    name: 'About',
    components: {
      Button
    },
    setup() {
      return {

      }
    },
  }
</script>

<style>

</style>
