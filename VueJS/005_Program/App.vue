<template>
  <div class="props-demo">
    <h1>Component Props Demo</h1>
    <UserCard
      v-for="user in users"
      :key="user.id"
      :name="user.name"
      :email="user.email"
      :age="user.age"
    />
  </div>
</template>

<script>
const UserCard = {
  props: ['name', 'email', 'age'],
  template: `
    <div class="user-card">
      <h3>{{ name }}</h3>
      <p>Email: {{ email }}</p>
      <p>Age: {{ age }}</p>
    </div>
  `
}

export default {
  name: 'PropsDemo',
  components: {
    UserCard
  },
  data() {
    return {
      users: [
        { id: 1, name: 'Alice', email: 'alice@example.com', age: 30 },
        { id: 2, name: 'Bob', email: 'bob@example.com', age: 25 },
        { id: 3, name: 'Charlie', email: 'charlie@example.com', age: 35 }
      ]
    }
  }
}
</script>

<style scoped>
.props-demo {
  max-width: 800px;
  margin: 50px auto;
  padding: 20px;
}

.user-card {
  background-color: #f5f5f5;
  padding: 20px;
  margin: 15px 0;
  border-radius: 8px;
  border-left: 4px solid #42b983;
}

.user-card h3 {
  margin-top: 0;
  color: #42b983;
}
</style>
