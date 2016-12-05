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


