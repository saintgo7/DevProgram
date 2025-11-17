<template>
  <div class="todo-app">
    <h1>Todo List</h1>
    <div class="input-group">
      <input
        v-model="newTodo"
        @keyup.enter="addTodo"
        placeholder="Enter a task"
      />
      <button @click="addTodo">Add</button>
    </div>
    <ul class="todo-list">
      <li v-for="(todo, index) in todos" :key="index">
        <span>{{ todo }}</span>
        <button @click="removeTodo(index)" class="delete">✕</button>
      </li>
    </ul>
    <p v-if="todos.length === 0" class="empty-message">
      No tasks yet. Add one above!
    </p>
  </div>
</template>

<script>
export default {
  name: 'TodoList',
  data() {
    return {
      newTodo: '',
      todos: []
    }
  },
  methods: {
    addTodo() {
      if (this.newTodo.trim()) {
        this.todos.push(this.newTodo)
        this.newTodo = ''
      }
    },
    removeTodo(index) {
      this.todos.splice(index, 1)
    }
  }
}
</script>

<style scoped>
.todo-app {
  max-width: 500px;
  margin: 50px auto;
  padding: 20px;
}

.input-group {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

input {
  flex: 1;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

button {
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.todo-list {
  list-style: none;
  padding: 0;
}

.todo-list li {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  margin: 5px 0;
  background-color: #f5f5f5;
  border-radius: 5px;
}

.delete {
  background-color: #e74c3c;
  padding: 5px 10px;
}

.empty-message {
  text-align: center;
  color: #999;
}
</style>
