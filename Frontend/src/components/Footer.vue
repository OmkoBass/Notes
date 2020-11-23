<template>
  <footer>
    <h1>
      <a href="https://www.github.com/Omkobass" target="_blank"> My Github </a>
    </h1>
  </footer>
</template>

<script>
  export default {
    name: 'Footer',
    setup() {

    },
  }
</script>

<style scoped>
  footer {
    display: flex;
    justify-content: center;
    height: 7vh;
    padding: 1em;
    text-align: center;
    color: white;
    background-color: var(--main-color);
  }

  footer a {
    color: white;
    text-decoration: none;
    transition: 0.3s all ease-in-out;
  }

  footer a:hover {
    color: lightgray;
  }

  footer {
    position: fixed;
    bottom: 0;
    width: 100%;
  }
</style>

