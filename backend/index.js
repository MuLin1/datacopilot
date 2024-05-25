const express = require('express');
const app = express();

app.use(express.json()); // 用于解析JSON格式的请求体

// 处理跨域请求问题
const cors = require('cors');
app.use(cors());

app.post('/register', (req, res) => {
  console.log('接收到的注册数据:', req.body);
  // 这里应该添加注册逻辑
  res.status(200).send('注册成功');
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`服务器运行在 http://localhost:${PORT}`);
});