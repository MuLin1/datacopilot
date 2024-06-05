<template>
  <div class="home-container">
    <div class="top-bar">主页面</div>
    <div class="search-box">
      <p>查询输入框</p>
      <input v-model="sqlStatement" type="text" placeholder="请输入查询内容">
      <button @click="sendSql"  class="submit-button">提交</button>
    </div>
    <div v-if="queryResults && queryResults.length > 0">
      <h2>查询结果：</h2>
      <div v-for="(result, index) in queryResults" :key="index">
        <h3>结果 {{ index + 1 }}</h3>
        <ul>
          <li v-for="(row, rowIndex) in result" :key="rowIndex">
            {{ row.column_name }}
          </li>
        </ul>
      </div>
    </div>
    <div class="image-box" @click="goToProfile">
    <img src="../images/个人中心.png" alt="Your Image">
    <p>个人主页</p>
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
import axios from 'axios';
export default {
  name: 'Home',
  data() {
    return {
<<<<<<< Updated upstream
=======
      // ... (之前的数据)
      sqlStatement:'',
      queryResults:[],
>>>>>>> Stashed changes
      records: [
        { id: 1, time: '2022-01-01', operator: 'User1', action: '登录' },
        { id: 2, time: '2022-01-02', operator: 'User2', action: '注册' },
        { id: 3, time: '2022-01-02', operator: 'User2', action: '登录' },
        { id: 4, time: '2022-01-03', operator: 'User1', action: '登录' },
        { id: 5, time: '2022-01-03', operator: 'User1', action: '修改密码' },
      ],
      isExpanded: false
    };
  },
  methods: {
    goToProfile() {
      this.$router.push('/profile');
    },
    toggleTable() {
      this.isExpanded = !this.isExpanded;
    },
    sendSql(){
    axios.post('http://localhost:3000/sql',{sql:this.sqlStatement})
    .then(response=>{
    console.log("success send",response.data);
    queryResults=response.data;
    })
    .catch(error=>{
    console.error("error sending",error);
    });
    }
  }
};
</script>

<style>
.home-container {
  text-align: center;
  height: 100%;
}

.top-bar {
  height: 30px;
  background-color: #808080;
  text-align: left;
}

.search-box {
  position: fixed;
  left:200px;
  top:200px;
  margin-top: 20px;
  height:200px;
}

.search-box p {
  position: fixed;
  top:100px;
  left:450px;
  font-family: "Times New Roman", Times, serif;
  font-size: 40px;
  color: #333;
  font-weight: bold;
  /* 其他样式属性 */
}

.search-box input[type="text"] {
  width: 600px; /* 设置宽度 */
  height: 40px; /* 设置高度 */
  font-size: 16px;
}

.image-box {
  position: fixed;
  top:50px;
  right:20px;
  text-align: center;
  border: 2px solid #ccc;
  padding: 10px;
  margin: 20px auto;
  width: 200px;
  cursor: pointer;
}

.image-box img {
  width: 100%;
  height: auto;
}

.image-box p {
  margin-top: 10px;
  color: #333;
  font-weight: bold;
}

.history-table {
  position: fixed;
  bottom: 150px;
  left:100px;
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
  width: 500px;
  position: absolute;
  left: 100%;
  top: 0;
}

.history-table.expanded {
  margin-top: 20px;
}


.history-table table.collapsed {
  display: none;
}
</style>
