<template>
  <div style="min-height: 100vh">
    <Header />

    <div class="p-fluid p-grid p-jc-center" style="padding: 1em; max-width: 100%;">
      <router-view/>
    </div>

    <Footer/>
  </div>
</template>

<script>
  import Header from '../components/Header';
  import CreateNote from '../components/CreateNote';
  import Footer from '../components/Footer';
  import Button from 'primevue/button';
  import router from "@/router";

  export default {
    name: 'Home',
    components: {
      Header,
      CreateNote,
      Footer,
      Button
    },
    setup() {
      if(!localStorage.getItem('accessToken') || !localStorage.getItem('refreshToken')) {
        router.push({ name: 'Login' })
      }

      return {
      }
    }
  }
</script>

<style scoped>

</style>
