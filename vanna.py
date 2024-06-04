import vanna
from vanna.remote import VannaDefault
import pandas as pd
import mysql.connector

def run_sql(sql: str) -> pd.DataFrame:
    cnx = mysql.connector.connect(user='root',password='root',host='localhost',database='1')
    cursor = cnx.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    return df


api_key = '274f3eff5f68445da46acccd924d46b1'
vanna_model_name = 'mygo'
vn = VannaDefault(model=vanna_model_name, api_key=api_key)
vn.run_sql = run_sql
vn.run_sql_is_set = True

'''
第一次运行的时候要运行这个
vn.train(ddl="""
CREATE TABLE IF NOT EXISTS mygoooo (
    ...
) COMMENT='mygoooo' CHARACTER SET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
""")
vn.train(question='身高最高的是哪个？',sql='SELECT name FROM customer ORDER BY height DESC LIMIT 1')

'''

vn.ask("谁的职业是guitar？")
