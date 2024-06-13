<!-- App.vue -->
<template>
  <div>
    <nav v-if=false>
      <router-link to="/">首页</router-link>
      <router-link to="/login">登录</router-link>
      <router-link to="/register">注册</router-link>
      <router-link to="/profile">个人中心</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script setup lang="ts">
</script>
