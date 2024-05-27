<template>
  <div>
    <div class="top-bar">主页面</div>
    <div class="search-box">
      <p>查询输入框</p>
      <input type="text" placeholder="请输入查询内容">
      <button class="submit-button">提交</button>
    </div>
    <div class="profile-box">
      <router-link to="/profile">个人中心</router-link>
    </div>
    <div class="history-table">
      <img src="../images/历史查询.png" alt="历史查询记录">
      <table v-bind:class="{ 'collapsed': !isExpanded }">
        <tr>
          <th>时间</th>
          <th>操作人员</th>
          <th>操作内容</th>
        </tr>
        <tr v-for="record in records" :key="record.id">
          <td>{{ record.time }}</td>
          <td>{{ record.operator }}</td>
          <td>{{ record.action }}</td>
        </tr>
      </table>
      <button @click="toggleTable">{{ isExpanded ? '折叠' : '展开' }}</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
  data() {
    return {
      // ... (之前的数据)
      records: [
        { id: 1, time: '2022-01-01', operator: 'User1', action: '登录' },
        { id: 2, time: '2022-01-02', operator: 'User2', action: '注册' },
        // 其他记录
      ],
      isExpanded: false
    };
  },
  methods: {
    // ... (之前的方法)
    toggleTable() {
      this.isExpanded = !this.isExpanded;
    }
  }
};
</script>

<style>
.top-bar {
  width: 100%;
  height: 30px;
  background-color: #808080;
  text-align: center;
  line-height: 30px;
  color: #fff;
}

.search-box {
  margin-top: 20px;
}

.profile-box {
  float: right;
  margin-right: 20px;
}

.history-table {
  text-align: center;
  margin-top: 50px;
}

.history-table img {
  width: 50px;
  height: 50px;
  display: block;
  margin: 0 auto 10px;
  cursor: pointer;
}

.history-table table {
  width: 50%;
  margin: 0 auto;
}

.history-table table.collapsed {
  display: none;
}
</style>
