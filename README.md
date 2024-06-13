# dtacopilot

### 运行步骤
##前端构建编译：先cd frontend，然后依次
```sh
npm run dev
```
```sh
npm run preview
```
##之后点击链接进入网站

##后端：cd backend，然后
```sh
node index.js
```
##链接后点按钮提交数据时可以在终端看到数据


# NL2SQL

A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8
I = 9
J = 10
K = 11
L = 12
M = 13
N = 14
O = 15
P = 16
Q = 17
R = 18
S = 19
T = 20
U = 21
V = 22
W = 23
X = 24
Y = 25
Z = 26
AA = 27
AB = 28
AC = 29
AD = 30
AE = 31
AF = 32
AG = 33
AH = 34
AI = 35
AJ = 36
AK = 37
AL = 38
AM = 39
AN = 40
AO = 41
AP = 42
AQ = 43
AR = 44
AS = 45
AT = 46
AU = 47
AV = 48
AW = 49
AX = 50
AY = 51
AZ = 52


# 使用的数据库sql语句
CREATE TABLE stock_prices (
    stock_code VARCHAR(10) PRIMARY KEY,
    stock_name VARCHAR(50),
    avg_price_jan FLOAT,
    avg_price_feb FLOAT,
    avg_price_mar FLOAT,
    avg_price_apr FLOAT,
    avg_price_may FLOAT,
    avg_price_jun FLOAT,
    avg_price_jul FLOAT,
    avg_price_aug FLOAT,
    avg_price_sep FLOAT,
    avg_price_oct FLOAT,
    avg_price_nov FLOAT,
    avg_price_dec FLOAT
);


INSERT INTO stock_prices (stock_code, stock_name, avg_price_jan, avg_price_feb, avg_price_mar, avg_price_apr, avg_price_may, avg_price_jun, avg_price_jul, avg_price_aug, avg_price_sep, avg_price_oct, avg_price_nov, avg_price_dec) 
VALUES ('000001', '平安银行', 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0),
       ('000002', '万科', 8.0, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4, 9.6, 9.8, 10.0, 10.2),
       ('000003', '招商银行', 15.0, 15.5, 16.0, 16.5, 17.0, 17.5, 18.0, 18.5, 19.0, 19.5, 20.0, 20.5),
       ('000004', '格力电器', 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0, 24.5, 25.0, 25.5),
       ('000005', '贵州茅台', 150.0, 160.0, 170.0, 180.0, 190.0, 200.0, 210.0, 220.0, 230.0, 240.0, 250.0, 260.0);

===属于在后端index.js把端口改成3306（一般默认端口）个人信息连接）===