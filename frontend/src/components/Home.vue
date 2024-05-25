<template>
  <div>
    <h1>欢迎来到我的网站</h1>
    <nav>
      <ul>
        <li><router-link to="/login">登录</router-link></li>
        <li><router-link to="/register">注册</router-link></li>
      </ul>
    </nav>
  </div>
</template>

<script>
export default {
  name: 'Home'
};
</script>

<style>
/* 添加你的CSS样式 */
</style>