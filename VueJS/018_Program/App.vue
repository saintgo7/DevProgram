<template>
  <div class="app">
    <h1>Vue.js Program {{ programNumber }}</h1>
    <p>{{ message }}</p>
    <button @click="updateMessage">Click Me</button>
  </div>
</template>

<script>
export default {
  name: 'Program018',
  data() {
    return {
      programNumber: 018,
      message: 'Basic Vue.js component'
    }
  },
  methods: {
    updateMessage() {
      this.message = 'Button clicked!'
    }
  }
}
</script>

<style scoped>
.app {
  text-align: center;
  padding: 50px;
}

button {
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
