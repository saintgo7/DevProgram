<template>
  <div class="state-demo">
    <h1>State Management {{ programNumber }}</h1>
    <p>Count: {{ count }}</p>
    <p>Status: {{ isActive ? 'Active' : 'Inactive' }}</p>
    <button @click="toggleActive">Toggle</button>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
export default {
  name: 'StateDemo034',
  data() {
    return {
      programNumber: 034,
      count: 0,
      isActive: false
    }
  },
  methods: {
    toggleActive() {
      this.isActive = !this.isActive
    },
    increment() {
      this.count++
    }
  },
  computed: {
    doubledCount() {
      return this.count * 2
    }
  }
}
</script>

<style scoped>
.state-demo {
  text-align: center;
  padding: 50px;
}

button {
  margin: 5px;
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
</style>
