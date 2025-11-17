<template>
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
