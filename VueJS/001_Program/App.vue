<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <p>{{ subtitle }}</p>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      message: 'Hello, Vue.js!',
      subtitle: 'Welcome to Vue.js Programming'
    }
  }
}
</script>

<style scoped>
#app {
  text-align: center;
  padding: 50px;
}

h1 {
  color: #42b983;
}
</style>
