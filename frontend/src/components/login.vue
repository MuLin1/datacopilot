<template>
  <div class="login-container">
    <div class="input-container">
      <img src="../images/logo.png" alt="logo">
      <div class="text-container">
        WELCOME BACK
      </div>
      <div class="form-container">
        <input type="text" placeholder="用户名" v-model="username">
      </div>
      <div class="form-container">
        <input type="password" placeholder="密码" v-model="password">
      </div>
      <div class="form-container">
        <button @click="login">LOGIN</button>
      </div>
      <div class="register-link">
        <router-link to="/register">没有账户？</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      if (this.validateInput()) {
        console.log(`登录信息：用户名=${this.username}, 密码=${this.password}`);
      }
    },
    validateInput() {
      if (!this.username || !this.password) {
        alert('用户名和密码不能为空');
        return false;
      }
      // Additional validation logic can go here
      return true;
    }
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.input-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.text-container {
  font-weight: bold;
  font-family: "Times New Roman", Times, serif;
  font-size: 30px;
  margin-bottom: 20px;
}

.form-container {
  margin: 10px;
  text-align: center;
}

input {
  margin: 5px;
  padding: 10px;
  width: 300px;
  border-radius: 10px;
  height: 40px;
  border: 1px solid #ccc;
}

button {
  background-color: #808080;
  color: #ffffff;
  font-weight: bold;
  font-size: 16px;
  font-family: "Times New Roman", Times, serif;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  width: 150px;
  cursor: pointer;
}

button:hover {
  background-color: #696969;
}

img {
  width: 243px;
  height: 95px;
  margin-bottom: 20px;
}

.register-link {
  margin-top: 20px;
}
</style>
