# coding:utf-8

# 对分组进行迭代
import pandas as pd
import numpy as np

df = pd.DataFrame({"key1": ["a", "a", "b", "b", "a"],
                   "key2": ["one", "two", "one", "two", "one"],
                   "data1": np.random.rand(5),
                   "data2": np.random.rand(5)})
# print df

# for name,group in df.groupby("key1"):
#     print name
#     print group

# for (k1, k2), group in df.groupby(["key1", "key2"]):
#     print k1, k2
#     print group


pieces = dict(list(df.groupby("key1")))
# print pieces

# print df.groupby("key1")["data1"]
# print df.groupby("key1")[["data1"]]

# print df.groupby(["key1","key2"])[["data2"]].mean()


people = pd.DataFrame(np.random.rand(5, 5),
                      columns=["a", "b", "c", "d", "e"],
                      index=["Joe", "Steve", "Wes", "Jim", "Travis"])
people.ix[2:3, ["b", "c"]] = np.nan
# print people

mapping = {"a": "red", "b": "red", "c": "blue", "d": "blue", "e": "red", "f": "orange"}
by_column = people.groupby(mapping, axis=1)
# print by_column.sum()

map_series = pd.Series(mapping)
# print map_series

# print people.groupby(map_series,axis=1).count()

key_list = ["one", "one", "one", "two", "two"]
# print people.groupby([len, key_list]).min()


# 根据索引级别分组
columns = pd.MultiIndex.from_arrays([["US", "US", "US", "JP", "JP"],
                                     [1, 3, 5, 1, 3]], names=["cty", "tenor"])
hier_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)


# grouped = df.groupby("key1")


# print grouped["data1"].quantile(0.9)


def peak_to_peak(arr):
    return arr.max() - arr.min()


# print grouped.agg(peak_to_peak)
# print grouped.describe()


tips = pd.read_csv("tips.csv")
tips["tip_pct"] = tips["tip"] / tips["total_bill"]

# print tips[:6]

grouped = tips.groupby(["sex", "smoker"])
grouped_pct = grouped["tip_pct"]
# print grouped_pct.agg(["mean", "std", peak_to_peak])

# print grouped_pct.agg([("foo", "mean"), ("bar", np.std)])

functions = ["count", "mean", "max"]
result = grouped["tip_pct", "total_bill"].agg(functions)
# print result

# print result["tip_pct"]
# print result["total_bill"]

ftuples = [("Durchschnitt", "mean"), ("Abweicung", np.var)]
# print grouped["tip_pct", "total_bill"].agg(ftuples)

# print grouped.agg({"tip": np.max, "size": "sum"})
# print grouped.agg({"tip_pct": ["min", "max", "mean", "std"], "size": "sum"})
# print tips.groupby(["sex", "smoker"], as_index=False).mean()
# print tips.groupby(["sex", "smoker"]).mean()


k1_mean = df.groupby("key1").mean().add_prefix("mean_")
# print pd.merge(df, k1_mean, left_on="key1", right_index=True)

key = ["one", "two", "one", "two", "one"]


# print people
# print people.groupby(key).mean()
# print people.groupby(key).transform(np.mean)

def demean(arr):
    return arr - arr.mean()


demeaned = people.groupby(key).transform(demean)


# print demeaned

def top(df, n=5, column="tip_pct"):
    return df.sort_values(by=column)[-n:]


# print top(tips, n=6)

# print tips.groupby("smoker").apply(top)
# print tips.groupby(["smoker", "day"]).apply(top, n=1, column="total_bill")

result = tips.groupby("smoker")["tip_pct"].describe()

# print type(result)

# print tips.groupby("smoker",group_keys=False).apply(top)
# print tips.groupby("smoker").apply(top)


frame = pd.DataFrame({"data1": np.random.randn(1000),
                      "data2": np.random.randn(1000)})
factor = pd.cut(frame.data1, 4)


# print factor[:10]

def get_stats(group):
    return {"min": group.min(), "max": group.max(),
            "count": group.count(), "mean": group.mean()}


grouped = frame.data2.groupby(factor)

# print grouped.apply(get_stats).unstack()

grouping = pd.qcut(frame.data1, 10, labels=False)
grouped = frame.data2.groupby(grouping)
# print grouped.apply(get_stats).unstack()

s = pd.Series(np.random.randn(6))
s[::2] = np.nan
# print s.fillna(s.mean())

states = ["Ohio", "New York", "Vermont", "Florida", "Oregon", "Nevada", "California", "Idaho"]
group_key = ["East"] * 4 + ["West"] * 4
data = pd.Series(np.random.randn(8), index=states)
data[["Vermont", "Nevada", "Idaho"]] = np.nan
# print data
fill_mean = lambda g: g.fillna(g.mean())
# print data.groupby(group_key).apply(fill_mean)


fill_values = {"East": 0.5, "West": -1}

fill_func = lambda g: g.fillna(fill_values[g.name])
# print data.groupby(group_key).apply(fill_func)



# 随机采样和排列
suits = ["H", "S", "C", "D"]
card_val = (range(1, 11) + [10] * 3) * 4
base_names = ["A"] + range(2, 11) + ["J", "K", "Q"]
cards = []
for suit in ["H", "S", "C", "D"]:
    cards.extend(str(num) + suit for num in base_names)
deck = pd.Series(card_val, index=cards)


def draw(deck, n=5):
    return deck.take(np.random.permutation(len(deck))[:n])


# print draw(deck)

get_suit = lambda card: card[-1]
# print deck.groupby(get_suit).apply(draw, n=2)

# 分组加权平均数和相关系数
# 根据groupby的“拆分-应用-合并”范式，DataFrame的列与列之间或两个Series之间的运算成为一种标准作业

df = pd.DataFrame({"category": ["a", "a", "a", "a", "b", "b", "b", "b"],
                   "data": np.random.randn(8),
                   "weights": np.random.rand(8)})

grouped = df.groupby("category")
get_wavg = lambda g: np.average(g["data"], weights=g["weights"])
# print grouped.apply(get_wavg)

close_px = pd.read_csv("stock_px.csv", parse_dates=True, index_col=0)
rets = close_px.pct_change().dropna()
spx_corr = lambda x: x.corrwith(x["SPX"])
by_year = rets.groupby(lambda x: x.year)
# print by_year.apply(spx_corr)
# print by_year.apply(lambda g: g["AAPL"].corr(g["MSFT"]))


# 面向分组的线性回归
# 对各数据块执行普通最小二乘法回归

import statsmodels.api as sm


def regress(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X["intercept"] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params

# print by_year.apply(regress,"AAPL",["SPX"])


# 透视表和交叉表
# print tips.pivot_table(index=["sex","smoker"])
# print tips.pivot_table(["tip_pct","size"],index=["sex","day"],columns="smoker")

# print tips.pivot_table(["tip_pct","size"],index=["sex","day"],columns="smoker",margins=True)

# print tips.pivot_table("tip_pct", index=["sex", "smoker"], columns="day", aggfunc=len, margins=True)
# print tips.pivot_table("size",index=["time","sex","smoker"],columns="day",aggfunc='sum',fill_value=0)
