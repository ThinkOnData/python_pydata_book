# coding:utf-8

# 时间序列
# 时间戳（timestamp）：特定的时间
# 固定时间（period）
# 时间间隔（interval）：由起始和结束时间戳表示

# 日期和时间数据类型及工具

from datetime import datetime

now = datetime.now()
# print now

# print now.year, now.month, now.day

delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
# print delta.seconds

from datetime import timedelta

start = datetime(2011, 1, 7)
# print start+timedelta(12)

# 字符串和datetime的相互转换
stamp = datetime(2011, 1, 3)
# print stamp.strftime("%Y/%m/%d")

datestrs = ["7/6/2011", "8/6/2011"]
# print [datetime.strptime(x, "%m/%d/%Y") for x in datestrs]

from dateutil.parser import parse
# print parse("2011-1-3")

# dateutil几乎能理解所有人类能够理解的日期表示形式

# print parse("Jan 31,1997 10:45 PM")

# print parse("6/12/2011", dayfirst=True)
# print parse("6/12/2011")

import pandas as pd

# print type(pd.to_datetime(datestrs))

idx = pd.to_datetime(datestrs + [None])
# print idx

# 时间序列基础
import numpy as np

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),
         datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12), ]
ts = pd.Series(np.random.randn(6), index=dates)
# print ts[::2]

# 索引、选取、子集构造
stamp = ts.index[2]
# print ts
# print stamp
# print ts[stamp]

longer_ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))

# print ts["1/7/2011":"1/10/2011"]
# print ts.truncate(before="1/9/2011")


dates = pd.date_range("1/1/2000", periods=100, freq="W-WED")
long_df = pd.DataFrame(np.random.randn(100, 4),
                       index=dates,
                       columns=["Colorado", "Texas", "New York", "Ohio"])
# print long_df

# 带有重复索引的时间序列
dates = pd.DatetimeIndex(["1/1/2000", "1/2/2000", "1/2/2000", "1/2/2000", "1/3/2000"])
dup_ts = pd.Series(np.arange(5), index=dates)
# print dup_ts

# print dup_ts.index.is_unique

grouped = dup_ts.groupby(level=0)
# print grouped.mean()


# 日期的范围、频率以及移动
# print ts.resample("D")

# 生成日期范围
index = pd.date_range("4/1/2012", "6/1/2012")
# print index
# print pd.date_range(start="4/1/2012",periods=20)

# print pd.date_range("1/1/2000","12/1/2000",freq="BM")
# print pd.date_range("5/2/2012 12:56:31", periods=5, normalize=True)


# 频率和日期偏移量
from pandas.tseries.offsets import Hour, Minute

hour = Hour(4)
# print hour

# print pd.date_range("1/1/2000","1/3/2000 23:59",freq="4h")

# print Hour(2)+Minute(30)

# print pd.date_range("1/1/2000",periods=10,freq="1h30min")


ts = pd.Series(np.random.randn(4),
               index=pd.date_range("1/1/2000", periods=4, freq="M"))
# print ts
# print ts.shift(2)
# print ts.shift(-2)

# print ts.shift(2,freq="M")
# print ts/ts.shift(1)-1

from pandas.tseries.offsets import Day, MonthEnd

now = datetime(2011, 11, 17)
# print now+3*Day()
# print now+MonthEnd(2)

offset=MonthEnd()
# print offset
# print offset.rollforward(now)
# print offset.rollback(now)

