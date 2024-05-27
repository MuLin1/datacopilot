<template>
  <div class="profile-container">
    <div class="top-bar">个人主页</div>
    <div class="content-container">
      <div class="info-container">
        <div>用户名：{{ username }}</div>
        <div>注册日期：{{ registrationDate }}</div>
      </div>
      <div class="button-container">
        <button @click="showPasswordModal">修改密码</button>
      </div>
    </div>

    <div v-if="showModal" class="modal" @click.self="closeModal">
      <div class="modal-content">
        <span class="close-btn" @click="closeModal">x</span>
        <input type="password" v-model="oldPassword" placeholder="原密码">
        <input type="password" v-model="newPassword" placeholder="新密码">
        <input type="password" v-model="confirmPassword" placeholder="确认新密码">
        <button @click="submitPassword">提交</button>
        <div class="error-message" v-if="errorMessage">{{ errorMessage }}</div>
      </div>
    </div>

    <div v-if="successMessage" class="success-message">
      <div>修改密码成功！</div>
      <button @click="closeSuccessMessage">OK</button>
    </div>
  </div>
  <router-link to="/" class="return-button">返回主页面</router-link>
</template>

<script>
export default {
  data() {
    return {
      username: '', // 从后端读取的用户名数据
      registrationDate: '', // 从后端读取的注册日期数据
      oldPassword: '',
      newPassword: '',
      confirmPassword: '',
      showModal: false,
      errorMessage: '',
      successMessage: false
    };
  },
  methods: {
    closeModal() {
      this.showModal = false;
    },
    showPasswordModal() {
      this.showModal = true;
    },
    submitPassword() {
      if (this.oldPassword !== '后端数据的原密码') {
        this.errorMessage = '原密码错误！';
      } else if (this.newPassword !== this.confirmPassword) {
        this.errorMessage = '两次输入的密码不一致！';
      } else {
        // 向后端发送新密码请求的代码，此处省略
        this.successMessage = true;
      }
    },
    closeSuccessMessage() {
      this.successMessage = false;
    }
  }
};
</script>

<style>
.profile-container {
  text-align: center;
  height: 100%;
}

.top-bar {
  height: 30px;
  background-color: #808080;
  text-align: left;
}

.content-container {
  margin-top: 20px;
}

.info-container {
  margin-bottom: 20px;
  height: auto;
}

.button-container {
  margin-bottom: 20px;
}

button {
  background-color: #808080; /* 将提交按钮背景设置为灰色 */
  color: #ffffff;
  font-weight: bold;
  font-size: 16px;
  font-family: "Times New Roman", Times, serif;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  width: 150px;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.9); /* 将背景设置为白色，透明度可根据需要调整 */
  display: flex;
  justify-content: center;
  align-items: center;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
}


.modal-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
}

.error-message {
  color: red;
}

.success-message {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
}

.return-button {
  position: absolute;
  bottom: 20px;
  right: 20px;
  background-color: #808080;
  color: #ffffff;
  font-weight: bold;
  font-size: 16px;
  font-family: "Times New Roman", Times, serif;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
}
</style>
