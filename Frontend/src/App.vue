<template>
  <router-view/>
</template>

<style>
/*color: #42b983;*/

* {
  margin: 0;
  padding: 0;
}

:root {
  --main-color: #883cae;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.icon {
  cursor: pointer;
  transition: 0.3s all ease-in;
}

.icon:hover {
  opacity: 0.5;
}
</style>
