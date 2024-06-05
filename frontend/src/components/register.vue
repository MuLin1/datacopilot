<template>
  <div class="container">
    <div class="left-column">
      <img src="../images/Register.png" alt="Register-img" class="c1">
    </div>
    <div class="right-column">
      <form @submit.prevent="register">
        <img src="../images/logo.png" alt="logo" class="c2">
        <div class="input-group">
          <input type="text" placeholder="用户名" v-model="username">
        </div>
        <div class="input-group">
          <input type="password" placeholder="密码" v-model="password">
        </div>
        <div class="input-group">
          <input type="password" placeholder="再输入一次密码" v-model="confirmPassword" @input="checkPassword">
          <span v-if="passwordMismatch" class="error-message">密码不一样！</span>
        </div>
        <button type="submit">CONFIRM</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';


export default {
  data() {
    return {
      username: '',
      password: '',
      confirmPassword: '',
      passwordMismatch: false
    };
  },
  methods: {
    register() {
      if (this.password === this.confirmPassword) {
      console.log('to register');
        axios.post('http://localhost:3000/register', {
          username: this.username,
          password: this.password
        })
          .then(response => {
            console.log(response.data);
            // 注册成功后的处理逻辑
            this.$router.push({ path: '/login' })
          })
          .catch(error => {
            console.error(error);
            // 处理错误情况
          });
      } else {
        this.password = '';
        this.confirmPassword = '';
        this.passwordMismatch = true;
      }
    },
    checkPassword() {
      this.passwordMismatch = this.password !== this.confirmPassword;
    }
  }
};
</script>

<style>
.container {
  display: flex;
  height: 100%;
  background: linear-gradient(to right, #666666 0%,#666666 40%,#f5f5f5 41%,#f5f5f5 100%);
}

.left-column {
  width: 40%;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.right-column {
  width: 60%;
  padding: 20px;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.input-group {
  margin-bottom: 10px;
  display: flex;
  flex-direction: column;
}

img {
  .c1{
    width: 500px;
    height: 120px;
  }
  .c2{
    width: 243px;
    height: 95px;
  }
}

.error-message {
  color: red;
  font-size: 12px;
  align-self: flex-start;
  margin-left: 5px;
}

button{
  background-color: #808080;
  color: #ffffff;
  font-weight: bold;
  font-size: 16px;
  font-family: "Times New Roman", Times, serif;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  width: 150px;
}
</style>
