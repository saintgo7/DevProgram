<template>
  <div class="computed-demo">
    <h1>Computed Properties {{ programNumber }}</h1>
    <input v-model="firstName" placeholder="First Name" />
    <input v-model="lastName" placeholder="Last Name" />
    <p>Full Name: {{ fullName }}</p>
    <p>Length: {{ nameLength }}</p>
  </div>
</template>

<script>
export default {
  name: 'ComputedDemo058',
  data() {
    return {
      programNumber: 058,
      firstName: '',
      lastName: ''
    }
  },
  computed: {
    fullName() {
      return `${this.firstName} ${this.lastName}`.trim()
    },
    nameLength() {
      return this.fullName.length
    }
  }
}
</script>

<style scoped>
.computed-demo {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
}

input {
  display: block;
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 5px;
}
</style>
