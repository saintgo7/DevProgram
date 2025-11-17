<template>
  <div class="watcher-demo">
    <h1>Watchers Demo {{ programNumber }}</h1>
    <input v-model="searchTerm" placeholder="Type to search" />
    <p>Search term: {{ searchTerm }}</p>
    <p>Character count: {{ searchTerm.length }}</p>
  </div>
</template>

<script>
export default {
  name: 'WatcherDemo079',
  data() {
    return {
      programNumber: 079,
      searchTerm: ''
    }
  },
  watch: {
    searchTerm(newVal, oldVal) {
      console.log(`Search term changed from "${oldVal}" to "${newVal}"`)
    }
  },
  mounted() {
    console.log('Component mounted')
  },
  beforeUnmount() {
    console.log('Component before unmount')
  }
}
</script>

<style scoped>
.watcher-demo {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
}

input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
