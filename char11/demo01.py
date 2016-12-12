# coding:utf-8

# 金融和经济数据应用
import pandas as pd

close_px = pd.read_csv('stock_px.csv', parse_dates=True, index_col=0)
volume = pd.read_csv('volume.csv', parse_dates=True, index_col=0)
prices = close_px.ix['2011-09-05':'2011-09-14', ['AAPL', 'JNJ', 'SPX', 'XOM']]
volume = volume.ix['2011-09-05':'2011-09-12', ['AAPL', 'JNJ', 'XOM']]

# print prices * volume

vwap = (prices * volume).sum() / volume.sum()
# print vwap.dropna()

# print prices.align(volume, join="inner")

s1 = pd.Series(range(3), index=["a", "b", "c"])
s2 = pd.Series(range(4), index=["d", "b", "c", "e"])
s3 = pd.Series(range(3), index=["f", "a", "c"])
# print pd.DataFrame({"one":s1,"two":s2,"three":s3})
# print pd.DataFrame({"one": s1, "two": s2, "three": s3}, index=list("face"))


# 频率不同的时间序列的运算
import numpy as np

ts1 = pd.Series(np.random.randn(3), index=pd.date_range("2012-6-13", periods=3, freq="W-WED"))
# print ts1.resample("B").ffill()

dates = pd.DatetimeIndex(["2012-6-12", "2012-6-17", "2012-6-18", "2012-6-21", "2012-6-22", "2012-6-29"])
ts2 = pd.Series(np.random.randn(6), index=dates)
# print ts2

# print ts1.resample("B").ffill().reindex(ts2.index).ffill()+ts2

# 使用Period
gdp = pd.Series([1.78, 1.94, 2.08, 2.01, 2.15, 2.31, 2.46], index=pd.period_range("1984Q2", periods=7, freq="Q-SEP"))
infl = pd.Series([0.025, 0.045, 0.037, 0.04], index=pd.period_range("1982", periods=4, freq="A-DEC"))

infl = infl.asfreq("Q-SEP", how="end")
# print infl.reindex(gdp.index).ffill()

# 时间和"最当前"数据选取
rng = pd.date_range("2012-06-01 09:30", "2012-06-01 15:59", freq="T")
rng = rng.append([rng + pd.offsets.BDay(i) for i in range(1, 4)])
ts = pd.Series(np.arange(len(rng), dtype=float), index=rng)
# print ts

from datetime import time

# print ts[time(10,1)]
# print ts.at_time(time(10,1))

# print ts.between_time(time(10, 0), time(10, 1))

indexer = np.sort(np.random.permutation(len(ts))[700:])
irr_ts = ts.copy()
# print len(indexer)
irr_ts[indexer] = np.nan
# print irr_ts["2012-06-01 09:50":"2012-06-01 10:00"]

selection = pd.date_range("2012-06-01 10:00", periods=4, freq="B")
# print irr_ts.asof(selection)


# 拼接多个数据源
data1 = pd.DataFrame(np.ones((6, 3), dtype=float),
                     columns=["a", "b", "c"],
                     index=pd.date_range("6/12/2012", periods=6))
data2 = pd.DataFrame(np.ones((6, 4), dtype=float) * 2,
                     columns=["a", "b", "c", "d"],
                     index=pd.date_range("6/13/2012", periods=6))
# print data1
# print data2

spliced = pd.concat([data1.ix[:"2012-06-14"], data2.ix["2012-06-15":]])
# print spliced
spliced_filled = spliced.combine_first(data2)

# print spliced_filled

# spliced.update(data2, overwrite=False)
# print spliced

cp_spliced = spliced.copy()
cp_spliced[["a", "c"]] = data1[["a", "c"]]
# print cp_spliced
# print data1

# 收益指数和累计收益

from pandas_datareader import data as web

price = web.DataReader("AAPL", "yahoo", "2011-01-01", "2012-07-27")["Adj Close"]
# print price["2011-10-03"]/price["2011-03-01"]-1


returns = price.pct_change()
ret_index = (1 + returns).cumprod()
ret_index[0] = 1
# print returns
# print ret_index

m_returns = ret_index.resample("BM").last().pct_change()
# print m_returns

m_rets = (1 + returns).resample("M", kind="period").prod() - 1
# print m_rets


# 分组变换和分析

import random;

random.seed(0)
import string

N = 1000


def rands(n):
    choices = string.ascii_uppercase
    return ''.join([random.choice(choices) for _ in xrange(n)])


tickers = np.array([rands(5) for _ in xrange(N)])

M = 500
df = pd.DataFrame({'Momentum': np.random.randn(M) / 200 + 0.03,
                   'Value': np.random.randn(M) / 200 + 0.08,
                   'ShortInterest': np.random.randn(M) / 200 - 0.02},
                  index=tickers[:M])

ind_names = np.array(['FINANCIAL', 'TECH'])
sampler = np.random.randint(0, len(ind_names), N)
industries = pd.Series(ind_names[sampler], index=tickers,
                       name='industry')

by_industry = df.groupby(industries)


# 行业内标准化处理
def zscore(group):
    return (group - group.mean()) / group.std()


df_stand = by_industry.apply(zscore)

# print df_stand.groupby(industries).agg(["mean", "std"])

# 行业内降序排名
ind_rank = by_industry.rank(ascending=False)
# print ind_rank.groupby(industries).agg(["min", "max"])

# 行业内排名和标准化
# print by_industry.apply(lambda x: zscore(x.rank()))

# 分组因子
from numpy.random import rand

fac1, fac2, fac3 = np.random.rand(3, 1000)
ticker_subset = tickers.take(np.random.permutation(N)[:1000])

# 因子加权和噪声
port = pd.Series(0.7 * fac1 - 1.2 * fac2 + 0.3 * fac3 + rand(1000),
                 index=ticker_subset)
factors = pd.DataFrame({"f1": fac1, "f2": fac2, "f3": fac3},
                       index=ticker_subset)

import statsmodels.api as sm

# print sm.OLS(port,factors).fit().summary()

# def beta_exposure(chunk, factors=None):
#     return pd.ols(y=chunk, x=factors).beta


# by_ind = port.groupby(industries)
# exposures = by_ind.apply(beta_exposure, factors=factors)
# print exposures.unstack()


# 十分位和四分位分析
from pandas_datareader import data as web

data = web.DataReader("SPY", "yahoo", "2006-001-01")
# print data

px = data['Adj Close']
returns = px.pct_change()


def to_index(rets):
    index = (1 + rets).cumprod()
    first_loc = max(index.index.get_loc(index.idxmax()) - 1, 0)
    index.values[first_loc] = 1
    return index


def trend_signal(rets, lookback, lag):
    signal = pd.Series.rolling(rets, lookback, min_periods=lookback - 5).sum()
    return signal.shift(lag)


signal = trend_signal(returns, 100, 3)
trade_friday = signal.resample('W-FRI').resample('B').ffill()
trade_rets = trade_friday.shift(1) * returns
trade_rets = trade_rets[:len(returns)]

# to_index(trade_rets).plot()

from matplotlib import pyplot as plt

# plt.show()


vol = pd.Series.rolling(returns, 250, min_periods=200).std() * np.sqrt(250)


def sharpe(rets, ann=250):
    return rets.mean() / rets.std() * np.sqrt(250)

# print trade_rets.groupby(pd.qcut(vol, 4)).agg(sharpe)
