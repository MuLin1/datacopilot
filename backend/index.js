const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const app = express();

// 处理跨域请求问题
const cors = require('cors');
app.use(cors());

const connection = mysql.createConnection({
  host: 'localhost',
  port:3306,
  user: 'root',
  password: 'MuLin0301',
  database: 'userdata'
});

app.use(bodyParser.json());

connection.connect((err) => {
  if (err) {
    console.error('Error connecting to database: ' + err.stack);
    return;
  }
  console.log('Connected to database as ID ' + connection.threadId);
});

app.post('/register', (req, res) => {
  const { username, password } = req.body;

  // 检查用户名是否已存在于数据库中
  const checkUsernameQuery = 'SELECT * FROM users WHERE username = ?';
  connection.query(checkUsernameQuery, [username], (err, results) => {
    let maxUserId;
    if (err) {
      console.error(err);
      res.status(500).json({message: '注册失败'});
    } else {
      if (results.length > 0) {
        // 如果存在相同用户名的记录，返回已存在消息
        res.status(400).json({message: '该用户已存在'});
      } else {
        maxUserId = 10001
        // 获取当前最大的idusers值
        const getMaxUserIdQuery = 'SELECT MAX(idusers) AS maxUserId FROM users';
        connection.query(getMaxUserIdQuery, (err, result) => {
          if (err) {
            console.error(err);
            res.status(500).json({message: '注册失败'});
          } else {
            let nextUserId = result[0].maxUserId ? result[0].maxUserId + 1 : 10001;
            // 将用户名、密码和自动分配的idusers插入到数据库中
            const insertUserQuery = 'INSERT INTO users (idusers, username, password) VALUES (?, ?, ?)';
            connection.query(insertUserQuery, [nextUserId, username, password], (err, result) => {
              if (err) {
                console.error(err);
                res.status(500).json({message: '注册失败'});
              } else {
                res.status(200).json({message: '注册成功'});
              }
            });
          }
        });
      }
    }
  });
});


app.listen(3000, () => {
  console.log('Server is running on port 3000');
});

app.post('/sql',(req,res)=>{
console.log('请求的sql',req.body);
const { sql } = req.body;
//数据库连接查询
const connection = mysql.createConnection({
  host: 'localhost',
  port:3306,
  user: 'root',
  password: 'MuLin0301',
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
