import csv
import pandas as pd

file = r'data.csv'
df = pd.read_csv(file,header=0)
df.columns = ["产品名","价格","起订量","单价","发货地","剩余量","公司名","所在地区","认证信息","食品生产许可证","产品执行标准",
              "商品产地","净含量","产品形态","种植方式","种类","商品满意度","商品好评率","评论数","好评数","追评数","中评数","差评数",
              "晒图数","评鉴内容数"]

columns = ["起订量","单价","发货地","剩余量","公司名","所在地区","食品生产许可证","产品执行标准",
           "商品产地","净含量","产品形态","种植方式","种类","商品满意度","商品好评率","评论数","好评数","追评数","中评数","差评数",
           "晒图数","评鉴内容数"]

df=df.astype(str)

for column in columns:
    for i in range(len(df[column])):
        d = df[column][i]
        d.replace('\n','')
        d.replace(' ','')

df.to_csv(file,index=False)

