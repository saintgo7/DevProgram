#!/usr/bin/env python3
"""
Create 100 Vue.js programs
"""

import os
import json

base_dir = "/home/user/DevProgram/VueJS"

# Vue.js program templates
vue_programs = {
    1: ("Hello World", "Basic Vue.js hello world", """<template>
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
"""),

    2: ("Counter App", "Counter with increment/decrement", """<template>
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
"""),

    3: ("Todo List", "Vue.js todo list", """<template>
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
"""),

    4: ("Form Input", "Vue.js form handling", """<template>
  <div class="form-app">
    <h1>Form Input Demo</h1>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label>Name:</label>
        <input v-model="formData.name" type="text" required />
      </div>
      <div class="form-group">
        <label>Email:</label>
        <input v-model="formData.email" type="email" required />
      </div>
      <div class="form-group">
        <label>Message:</label>
        <textarea v-model="formData.message" rows="4"></textarea>
      </div>
      <button type="submit">Submit</button>
    </form>
    <div v-if="submitted" class="result">
      <h3>Submitted Data:</h3>
      <p><strong>Name:</strong> {{ formData.name }}</p>
      <p><strong>Email:</strong> {{ formData.email }}</p>
      <p><strong>Message:</strong> {{ formData.message }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FormInput',
  data() {
    return {
      formData: {
        name: '',
        email: '',
        message: ''
      },
      submitted: false
    }
  },
  methods: {
    handleSubmit() {
      this.submitted = true
      setTimeout(() => {
        this.submitted = false
      }, 5000)
    }
  }
}
</script>

<style scoped>
.form-app {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input, textarea {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

button {
  padding: 10px 30px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

.result {
  margin-top: 30px;
  padding: 20px;
  background-color: #e8f5e9;
  border-radius: 5px;
}
</style>
"""),

    5: ("Component Props", "Vue.js component with props", """<template>
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
"""),
}

# Generate remaining programs (6-100)
for i in range(6, 101):
    if i <= 20:
        # Basic Components
        code = f"""<template>
  <div class="app">
    <h1>Vue.js Program {{{{ programNumber }}}}</h1>
    <p>{{{{ message }}}}</p>
    <button @click="updateMessage">Click Me</button>
  </div>
</template>

<script>
export default {{
  name: 'Program{i:03d}',
  data() {{
    return {{
      programNumber: {i:03d},
      message: 'Basic Vue.js component'
    }}
  }},
  methods: {{
    updateMessage() {{
      this.message = 'Button clicked!'
    }}
  }}
}}
</script>

<style scoped>
.app {{
  text-align: center;
  padding: 50px;
}}

button {{
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}}
</style>
"""
    elif i <= 40:
        # State Management
        code = f"""<template>
  <div class="state-demo">
    <h1>State Management {{{{ programNumber }}}}</h1>
    <p>Count: {{{{ count }}}}</p>
    <p>Status: {{{{ isActive ? 'Active' : 'Inactive' }}}}</p>
    <button @click="toggleActive">Toggle</button>
    <button @click="increment">Increment</button>
  </div>
</template>

<script>
export default {{
  name: 'StateDemo{i:03d}',
  data() {{
    return {{
      programNumber: {i:03d},
      count: 0,
      isActive: false
    }}
  }},
  methods: {{
    toggleActive() {{
      this.isActive = !this.isActive
    }},
    increment() {{
      this.count++
    }}
  }},
  computed: {{
    doubledCount() {{
      return this.count * 2
    }}
  }}
}}
</script>

<style scoped>
.state-demo {{
  text-align: center;
  padding: 50px;
}}

button {{
  margin: 5px;
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}}
</style>
"""
    elif i <= 60:
        # Computed Properties
        code = f"""<template>
  <div class="computed-demo">
    <h1>Computed Properties {{{{ programNumber }}}}</h1>
    <input v-model="firstName" placeholder="First Name" />
    <input v-model="lastName" placeholder="Last Name" />
    <p>Full Name: {{{{ fullName }}}}</p>
    <p>Length: {{{{ nameLength }}}}</p>
  </div>
</template>

<script>
export default {{
  name: 'ComputedDemo{i:03d}',
  data() {{
    return {{
      programNumber: {i:03d},
      firstName: '',
      lastName: ''
    }}
  }},
  computed: {{
    fullName() {{
      return `${{this.firstName}} ${{this.lastName}}`.trim()
    }},
    nameLength() {{
      return this.fullName.length
    }}
  }}
}}
</script>

<style scoped>
.computed-demo {{
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
}}

input {{
  display: block;
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: 1px solid #ddd;
  border-radius: 5px;
}}
</style>
"""
    elif i <= 80:
        # Watchers and Lifecycle
        code = f"""<template>
  <div class="watcher-demo">
    <h1>Watchers Demo {{{{ programNumber }}}}</h1>
    <input v-model="searchTerm" placeholder="Type to search" />
    <p>Search term: {{{{ searchTerm }}}}</p>
    <p>Character count: {{{{ searchTerm.length }}}}</p>
  </div>
</template>

<script>
export default {{
  name: 'WatcherDemo{i:03d}',
  data() {{
    return {{
      programNumber: {i:03d},
      searchTerm: ''
    }}
  }},
  watch: {{
    searchTerm(newVal, oldVal) {{
      console.log(`Search term changed from "${{oldVal}}" to "${{newVal}}"`)
    }}
  }},
  mounted() {{
    console.log('Component mounted')
  }},
  beforeUnmount() {{
    console.log('Component before unmount')
  }}
}}
</script>

<style scoped>
.watcher-demo {{
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
}}

input {{
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 5px;
}}
</style>
"""
    else:
        # Advanced Features
        code = f"""<template>
  <div class="advanced-demo">
    <h1>Advanced Features {{{{ programNumber }}}}</h1>
    <transition name="fade">
      <p v-if="show">{{{{ message }}}}</p>
    </transition>
    <button @click="toggle">Toggle</button>
    <div class="list">
      <transition-group name="list" tag="ul">
        <li v-for="item in items" :key="item" class="list-item">
          {{{{ item }}}}
        </li>
      </transition-group>
    </div>
  </div>
</template>

<script>
export default {{
  name: 'AdvancedDemo{i:03d}',
  data() {{
    return {{
      programNumber: {i:03d},
      message: 'This is an advanced Vue.js component',
      show: true,
      items: [1, 2, 3, 4, 5]
    }}
  }},
  methods: {{
    toggle() {{
      this.show = !this.show
    }}
  }}
}}
</script>

<style scoped>
.advanced-demo {{
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
}}

.fade-enter-active, .fade-leave-active {{
  transition: opacity 0.5s;
}}

.fade-enter-from, .fade-leave-to {{
  opacity: 0;
}}

.list-item {{
  padding: 10px;
  margin: 5px 0;
  background-color: #42b983;
  color: white;
  border-radius: 5px;
}}

.list-move {{
  transition: transform 0.5s;
}}

button {{
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}}
</style>
"""

    vue_programs[i] = (f"Program {i}", f"Vue.js program {i}", code)

# Create directories and files
os.makedirs(base_dir, exist_ok=True)

for num, (title, desc, code) in vue_programs.items():
    program_dir = f"{base_dir}/{num:03d}_Program"
    os.makedirs(program_dir, exist_ok=True)

    # Write App.vue
    with open(f"{program_dir}/App.vue", 'w') as f:
        f.write(code)

    # Create package.json
    package_json = {
        "name": f"vue-program-{num:03d}",
        "version": "1.0.0",
        "description": desc,
        "private": True,
        "scripts": {
            "dev": "vite",
            "build": "vite build",
            "preview": "vite preview"
        },
        "dependencies": {
            "vue": "^3.3.0"
        },
        "devDependencies": {
            "@vitejs/plugin-vue": "^4.4.0",
            "vite": "^5.0.0"
        }
    }

    with open(f"{program_dir}/package.json", 'w') as f:
        json.dump(package_json, f, indent=2)

    # Create vite.config.js
    vite_config = """import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()]
})
"""

    with open(f"{program_dir}/vite.config.js", 'w') as f:
        f.write(vite_config)

    print(f"Created: {num:03d} - {title}")

print(f"\nCreated {len(vue_programs)} Vue.js programs in {base_dir}")
