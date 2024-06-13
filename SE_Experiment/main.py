import pymysql
import matplotlib.pyplot as plt

# 数据库配置
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'db': '1',
}

# 连接数据库
connection = pymysql.connect(**db_config)

# 查询数据
try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT id,180day FROM 180day LIMIT 10")
        data = cursor.fetchall()
finally:
    connection.close()

# 假设data是一个列表，每个元素是一个包含两个元素的元组
# 处理数据
column1_data = [item[0] for item in data]
column2_data = [item[1] for item in data]

# 生成图表
plt.figure(figsize=(8, 6))
plt.plot(column1_data, column2_data, marker='o')
plt.title('180day')
plt.ylabel('rate')
plt.grid(True)


# 如果需要在屏幕上显示图表，取消注释下面的行
plt.show()
