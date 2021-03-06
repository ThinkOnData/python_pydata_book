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

offset = MonthEnd()
# print offset
# print offset.rollforward(now)
# print offset.rollback(now)

ts = pd.Series(np.random.randn(20),
               index=pd.date_range("1/15/2000", periods=20, freq="4d"))
# print ts.groupby(offset.rollforward).mean()

# print ts.resample("M").mean()

import pytz

# print pytz.common_timezones[-5:]
tz = pytz.timezone("US/Eastern")
# print tz

rng = pd.date_range("3/9/2012", periods=6, freq="D")
ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print ts.index.tz

ts_utc = ts.tz_localize("UTC")
# print ts_utc.index

# print ts_utc.tz_convert("US/Mountain").index


# 时期及其算数计算
p = pd.Period(2007, freq="A-DEC")
# print p+2


values = ["2001Q3", "2002Q2", "2003Q1"]
index = pd.PeriodIndex(values, freq="Q-DEC")
# print index


p = pd.Period("2007", freq="A-DEC")
# print p.asfreq("M", how="start")
# print p.asfreq("M",how="end")

rng = pd.period_range("2011Q3", "2012Q4", freq="Q-JAN")
ts = pd.Series(np.arange(len(rng)), index=rng)
new_rng = (rng.asfreq("B", "e") - 1).asfreq("T", "s") + 16
ts.index = new_rng.to_timestamp()
# print ts

# 通过数组创建PeriodIndex
data = pd.read_csv("E:\workspace_git\python_pydata_book\char08\macrodata.csv")
# print data.quarter

index = pd.PeriodIndex(year=data.year, quarter=data.quarter, freq="Q-DEC")
# print index

data.index = index
# print data.infl


rng = pd.date_range("1/1/2000", periods=100, freq="D")
ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print ts
# print ts.resample("M").mean()
# print ts.resample("M", kind="period").mean()


# 降采样
rng = pd.date_range("1/1/2000", periods=12, freq="T")
ts = pd.Series(np.arange(12), index=rng)
# print ts.resample("5min",label="left").sum()
# print ts.resample("5min",label="right").sum()
# print ts.resample("5min",closed="left").sum()
# print ts.resample("5min", loffset="-1s").sum()
# print ts.resample("5min").ohlc()

# 通过groupby进行重采样
rng = pd.date_range("1/1/2000", periods=100, freq="D")
ts = pd.Series(np.arange(100), index=rng)
# print ts
# print ts.groupby(lambda x: x.month).mean()
# print ts.groupby(lambda x: x.weekday).mean()

# 升采样和插值
frame = pd.DataFrame(np.random.randn(2, 4),
                     index=pd.date_range("1/1/2000", periods=2, freq="W-WED"),
                     columns=["Colorado", "Texas", "New York", "Ohio"])
df_daily = frame.resample("D").ffill()
# print df_daily

# 通过时期进行重采样
frame = pd.DataFrame(np.random.randn(24, 4),
                     index=pd.period_range("1-2000", "12-2001", freq="M"),
                     columns=["Colordo", "Texas", "New York", "Ohio"])
# print frame
# annual_frame = frame.resample("A-DEC").mean()
# print annual_frame

annual_frame = frame.resample("Q-DEC")
# print annual_frame
annual_frame1 = frame.resample("Q-DEC", convention="start")
# print annual_frame1


# 时间序列绘图
close_px_all = pd.read_csv("E:\workspace_git\python_pydata_book\char09\stock_px.csv",
                           parse_dates=True,
                           index_col=0)
close_px = close_px_all[["AAPL", "MSFT", "XOM"]]
close_px = close_px.resample("B").ffill()
# print close_px
# close_px["AAPL"].plot()
# close_px.ix["2009"].plot()

# close_px["AAPL"].ix["01-2011":"03-2011"].plot()

appl_q = close_px["AAPL"].resample("Q-DEC").ffill()
# appl_q.ix["2009":].plot()

# close_px.AAPL.plot()
# pd.rolling_mean(close_px.AAPL,250).plot()


appl_std250 = pd.Series.rolling(close_px.AAPL, 250, min_periods=10).std()
# appl_std250.plot()

# expandng_mean=lambda x: pd.Series.rolling(x,len(x),min_periods=1).mean()
# pd.DataFrame.rolling(close_px, 60).mean().plot(logy=True)
# pd.DataFrame.rolling(close_px, 60).mean().plot()
# pd.DataFrame.rolling(close_px, 60).kurt().plot(logy=True)

import matplotlib.pyplot as plt

# fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True, figsize=(12, 7))
# aapl_px = close_px.AAPL["2005":"2009"]
# ma60 = pd.Series.rolling(aapl_px, 60, min_periods=50).mean()
# ewma60 = pd.Series.ewm(aapl_px, span=60).mean()

# aapl_px.plot(style="k-",ax=axes[0])
# ma60.plot(style="k--",ax=axes[0])
# aapl_px.plot(style="k-",ax=axes[1])
# ewma60.plot(style="k--",ax=axes[1])
# axes[0].set_title("Simple MA")
# axes[1].set_title("Exponetially-weighted MA")


# 二元移动窗口函数
# spx_px = close_px_all["SPX"]
# spx_rets = spx_px / spx_px.shift(1) - 1
returns = close_px.pct_change()
# corr = pd.rolling_corr(returns, spx_rets, 125, min_periods=100)
# corr.plot()

# 用户自定义移动窗口函数
from scipy.stats import percentileofscore

score_at_2percent = lambda x: percentileofscore(x, 0.02)
# result = pd.rolling_apply(returns.AAPL, 250, score_at_2percent)
# result.plot()

# plt.show()


# 性能和内存使用方面的注意事项

rng = pd.date_range("1/1/2000", periods=10000000, freq="10ms")
ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print ts

print ts.resample("15s").ohlc()
