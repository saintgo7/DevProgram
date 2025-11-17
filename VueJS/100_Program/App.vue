<template>
  <div class="advanced-demo">
    <h1>Advanced Features {{ programNumber }}</h1>
    <transition name="fade">
      <p v-if="show">{{ message }}</p>
    </transition>
    <button @click="toggle">Toggle</button>
    <div class="list">
      <transition-group name="list" tag="ul">
        <li v-for="item in items" :key="item" class="list-item">
          {{ item }}
        </li>
      </transition-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AdvancedDemo100',
  data() {
    return {
      programNumber: 100,
      message: 'This is an advanced Vue.js component',
      show: true,
      items: [1, 2, 3, 4, 5]
    }
  },
  methods: {
    toggle() {
      this.show = !this.show
    }
  }
}
</script>

<style scoped>
.advanced-demo {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}

.list-item {
  padding: 10px;
  margin: 5px 0;
  background-color: #42b983;
  color: white;
  border-radius: 5px;
}

.list-move {
  transition: transform 0.5s;
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
