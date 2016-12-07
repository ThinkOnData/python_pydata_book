# coding:utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 2012联邦选举委员会数据库
fec = pd.read_csv("P00000001-ALL.csv")
# print fec.ix[12345]
unique_cands = fec.cand_nm.unique()
# print unique_cands

parties = {'Bachmann, Michelle': "Republican",
           'Romney, Mitt': "Republican",
           'Obama, Barack': "Democrat",
           "Roemer, Charles E. 'Buddy' III": "Republican",
           'Pawlenty, Timothy': "Republican",
           'Johnson, Gary Earl': "Republican",
           'Paul, Ron': "Republican",
           'Santorum, Rick': "Republican",
           'Cain, Herman': "Republican",
           'Gingrich, Newt': "Republican",
           'McCotter, Thaddeus G': "Republican",
           'Huntsman, Jon': "Republican",
           'Perry, Rick': "Republican"}

# print fec.cand_nm[123456:123461].map(parties)
fec["party"] = fec.cand_nm.map(parties)
# print fec["parties"].value_counts()
# print (fec.contb_receipt_amt > 0).value_counts()
fec = fec[fec.contb_receipt_amt > 0]
fec_mrbo = fec[fec.cand_nm.isin(["Obama, Barack", "Romney, Mitt"])]
# print fec_mrbo

# 根据职业和雇主信息统计赞助信息
# print fec.contbr_occupation.value_counts()[:10]

occ_mapping = {
    "INFORMATION REQUESTED PER BEST EFFORTS": "NOT PROVIDED",
    "INFORMATION REQUESTED": "NOT PROVIDED",
    "INFORMATION REQUESTED (BEST EFFORTS)": "NOT PROVIDED",
    "C.E.O.": "CEO"
}

f = lambda x: occ_mapping.get(x, x)
fec.contbr_occupation = fec.contbr_occupation.map(f)

emp_mapping = {
    "INFORMATION REQUESTED PER BEST EFFORTS": "NOT PROVIDED",
    "INFORMATION REQUESTED": "NOT PROVIDED",
    "SELF": "SELF-EMPLOYED",
    "SELF EMPLOYED": "SELF EMPLOYED"
}

f = lambda x: emp_mapping.get(x, x)
fec.contbr_employer = fec.contbr_employer.map(f)

by_occupation = fec.pivot_table("contb_receipt_amt", index="contbr_occupation", columns="party", aggfunc="sum")
over_2m = by_occupation[by_occupation.sum(1) > 2000000]


# over_2m.plot(kind="barh")
# plt.show()


def get_top_amounts(group, key, n=5):
    totals = group.groupby(key)["contb_receipt_amt"].sum()
    return totals.sort_values(ascending=False)[n:]


grouped = fec_mrbo.groupby("cand_nm")
# print grouped.apply(get_top_amounts, "contbr_occupation", n=7)


# 对出资额分组
bins = np.array([0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
labels = pd.cut(fec_mrbo.contb_receipt_amt, bins)

grouped = fec_mrbo.groupby(["cand_nm", labels])
# print grouped.size().unstack()

bucker_sums = grouped.contb_receipt_amt.sum().unstack(0)
# print bucker_sums
normed_sums = bucker_sums.div(bucker_sums.sum(axis=1), axis=0)
# print normed_sums

# normed_sums[:-2].plot(kind="barh",stacked=True)
# plt.show()


# 根据州统计赞助信息
grouped = fec_mrbo.groupby(["cand_nm", "contbr_st"])
totals = grouped.contb_receipt_amt.sum().unstack(0).fillna(0)
totals = totals[totals.sum(1) > 100000]

percent = totals.div(totals.sum(1), axis=0)
