<template>
  <div class="counter-app">
    <h1>Counter App</h1>
    <div class="counter-display">
      <p>Counter Value:</p>
      <h2>{{ count }}</h2>
    </div>
    <div class="button-group">
      <button @click="decrement">-</button>
      <button @click="reset" class="reset">Reset</button>
      <button @click="increment">+</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CounterApp',
  data() {
    return {
      count: 0
    }
  },
  methods: {
    increment() {
      this.count++
    },
    decrement() {
      this.count--
    },
    reset() {
      this.count = 0
    }
  }
}
</script>

<style scoped>
.counter-app {
  text-align: center;
  padding: 50px;
}

.counter-display h2 {
  font-size: 48px;
  color: #42b983;
  margin: 20px 0;
}

.button-group {
  display: flex;
  gap: 15px;
  justify-content: center;
}

button {
  padding: 10px 30px;
  font-size: 18px;
  border: none;
  border-radius: 5px;
  background-color: #42b983;
  color: white;
  cursor: pointer;
}

button.reset {
  background-color: #e74c3c;
}

button:hover {
  opacity: 0.8;
}
</style>
