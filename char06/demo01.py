#coding:utf-8

#索引：将一个或多个列当作返回的DataFrame处理，以及是否从文件、用户获取列名
#类型推断和数据转换：用户定义值的转换、缺失值标记列表
#日期解析：组合功能，包括将分散在多个列中的日期时间信息组合成结果中的单个列
#迭代：支持对大文件进行逐块迭代
#不规整数据问题：跳过一些行、页脚、注释或其他一些不重要的东西


import pandas as pd

df=pd.read_csv("ex1.csv")
# print df

df=pd.read_table("ex1.csv",sep=",")
# print df

# print pd.read_csv("ex2.csv",header=None)
# print pd.read_csv("ex2.csv",names=["a","b","c","d","message"])


# print pd.read_csv("ex2.csv",names=["a","b","c","d","message"],index_col="message")

parsed=pd.read_csv("csv_mindex.csv",index_col=["key1","key2"])
# print parsed


# print list(open("ex3.txt"))
result=pd.read_table("ex3.txt",sep="\s+")#\s 任何空白字符，例如空格符、制表符等，\S 除 [\s] 之外的任何字符
# print result


# print pd.read_csv("ex4.csv",skiprows=[0,2,3])

result=pd.read_csv("ex5.csv")
# print pd.isnull(result)


sentinels={"message":["fool","NA"],"something":["two"]}
# print pd.read_csv("ex5.csv",na_values=sentinels)


chunker= pd.read_csv("ex6.csv",chunksize=1000)
# print chunker
tot= pd.Series([])
for piece in chunker:
    tot=tot.add(piece["key"].value_counts(),fill_value=0)
tot=tot.sort_values(ascending=False)

# print tot[:10]



data=pd.read_csv("ex5.csv")
# print data
# data.to_csv("out.csv")

import sys
# data.to_csv(sys.stdout,sep="|")
# data.to_csv(sys.stdout,na_rep="NULL")

import numpy as np
dates=pd.date_range("1/1/2000",periods=7)
ts= pd.Series(np.arange(7),index=dates)
# ts.to_csv(("mytseries.csv"))


# print pd.Series.from_csv("tseries.csv",parse_dates=True)

import csv
lines=list(csv.reader(open("ex7.csv")))
header,values=lines[0],lines[1:]
data_dict={h:v for h,v in zip(header,zip(*values))}
# print data_dict


frame=pd.read_csv("ex1.csv")
# print frame
import pandas
# frame.to_pickle("frame_pickle")


xls_file=pd.ExcelFile("data.xls")
table=xls_file.parse("Sheet1")
# print table


import sqlite3
query="""
CREATE TABLE test
(
    a VERCHAR(20),b VARCHAR(20),
    c REAL, d INTEGER
);"""
con=sqlite3.connect(":memory:")
con.execute(query)
con.commit()

data=[("Atlanta","Georgia",1.25,6),
      ("Tallahassee","Florida",2.6,3),
      ("Sacramento","California",1.7,5)]
stmt="INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt,data)
con.commit()

cursor=con.execute("select * from test")
rows=cursor.fetchall()
# print rows
# print cursor.description


# print pd.DataFrame(rows, columns=zip(*cursor.description)[0])


import pandas.io.sql as sql
# print sql.read_sql("select * from test",con)

