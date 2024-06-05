const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const app = express();
const PORT = 3000;

// 解析请求体中的 JSON 数据
app.use(bodyParser.json());

// 处理跨域请求问题
const cors = require('cors');
app.use(cors());

app.post('/register', (req, res) => {
  console.log('接收到的注册数据:', req.body);
  // 这里应该添加注册逻辑
  res.status(200).send('注册成功');
});

app.post('/sql',(req,res)=>{
console.log('请求的sql',req.body);
const { sql } = req.body;
//数据库连接查询
const connection = mysql.createConnection({
  host: 'localhost',
  port:3308,
  user: 'root',
  password: 'chd123456',
  database: 'todomvc',});



// 连接到MySQL数据库
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to database:', err);
    return;
  }
  console.log('Connected to database');
});

// 执行SQL查询
  connection.query(sql, (err, results) => {
    if (err) {
      console.error('Error executing query:', err);
      res.status(500).json({ error: 'Error executing query' });
      return;
    }

    // 返回查询结果
    res.json(results);
  });

});


app.listen(PORT, () => {
  console.log(`服务器运行在 http://localhost:${PORT}`);
});