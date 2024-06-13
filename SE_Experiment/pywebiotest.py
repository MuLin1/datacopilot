import mysql.connector
import matplotlib.pyplot as plt
from pywebio import start_server
from pywebio.input import textarea
from pywebio.output import put_image, put_text, put_error
import io
import matplotlib

# 设置Matplotlib使用非GUI后端
matplotlib.use('Agg')

# 设置支持中文的字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像时负号显示为方块的问题

def execute_sql_and_plot():
    # 输入SQL查询
    query = textarea('请输入SQL查询:', rows=10, placeholder='例如: SELECT column1, column2 FROM your_table')

    try:
        # 连接到本地MySQL数据库
        conn = mysql.connector.connect(
            host='localhost',       # 数据库主机地址
            user='root',   # 数据库用户名
            password='root', # 数据库密码
            database='1' # 数据库名称
        )
        cursor = conn.cursor()

        # 执行SQL查询
        cursor.execute(query)
        result = cursor.fetchall()

        # 检查结果是否为空
        if not result:
            put_text('查询结果为空')
            return

        # 假设查询结果有两列，第一列为X轴，第二列为Y轴
        x_data = [row[0] for row in result]
        y_data = [row[1] for row in result]

        # 创建图像
        plt.figure()
        plt.plot(x_data, y_data)
        plt.xlabel('X轴')
        plt.ylabel('Y轴')
        plt.title('SQL查询结果图像')

        # 将图像保存到字节流
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        plt.close()
        buf.seek(0)

        # 显示图像
        put_image(buf.getvalue())

    except mysql.connector.Error as db_err:
        put_error(f'数据库错误: {db_err}')
    except Exception as e:
        put_error(f'执行SQL查询时出错: {e}')
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'conn' in locals() and conn is not None:
            conn.close()

if __name__ == '__main__':
    start_server(execute_sql_and_plot, port=8080)
