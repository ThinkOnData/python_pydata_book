#coding:utf-8

import numpy as np
from pandas import DataFrame,Series
import pandas as pd

frame=DataFrame(np.random.randn(4,3),columns=list("bde"),index=["Utah","Ohio","Texas","Oregon"])

def f(x):
    return Series([x.min(),x.max()],index=["min","max"])
# print frame.apply(f)

format=lambda x:"%.2f" % x
# print frame.applymap(format)

# print frame["e"].map(format)

from pandas_datareader import data
all_data={}
for ticker in ["AAPL","IBM","MSFT","GOOG"]:
    all_data[ticker]=data.DataReader(ticker,"yahoo","1/1/2000","1/1/2010")
# print all_data


price=DataFrame({tic:data["Adj Close"] for tic,data in all_data.iteritems()})
volume=DataFrame({tic:data["Volume"] for tic ,data in all_data.iteritems()})

returns=price.pct_change()
# print returns.tail()


# print returns.MSFT.corr(returns.IBM)
# print returns.corr()


from numpy import nan as NA
df=DataFrame(np.random.randn(7,3))
df.ix[:4,1]=NA;df.ix[:2,2]=NA
# print df.fillna({1:0.5,2:-1})


_=df.fillna(0,inplace=True)#返回被填充对象的引用，对现有对象进行修改
# print df


frame=DataFrame(np.arange(6).reshape(3,2),index=[2,0,1])
# print frame.irow(2)


#面板数据
from pandas_datareader import data
pdata=pd.Panel(dict((stk,data.DataReader(stk,"yahoo","1/1/2009","6/1/2012")) for stk in ["AAPL","GOOG","MSFT","DELL"]))
stacked=pdata.ix[:,"5/30/2012":,:].to_frame()
# print stacked.to_panel()
