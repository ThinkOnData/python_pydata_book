#coding:utf-8

#绘图和可视化

import numpy as np
from matplotlib.pyplot import plot, show

# show(plot(np.arange(10)))

import matplotlib.pyplot as plt
# fig=plt.figure()
#
# ax1=fig.add_subplot(2,2,1)
# ax2=fig.add_subplot(2,2,2)
# ax3=fig.add_subplot(2,2,3)
#
#
from numpy.random import randn
# # show(plt.plot(randn(50).cumsum(),"k--"))
# plt.plot(randn(50).cumsum(),"k--")
#
# _=ax1.hist(randn(100),bins=20,color="k",alpha=0.3)
# show(ax2.scatter(np.arange(30),np.arange(30)+3*randn(30)))


# fig,axes=plt.subplots(2,2,sharex=True,sharey=True)
# for i in range(2):
#     for j in range(2):
#         axes[i,j].hist(randn(500),bins=50,color="k",alpha=0.5)
# show(plt.subplots_adjust(wspace=0,hspace=0))


# show(plt.plot(randn(30).cumsum(),"ko--"))

# show(plt.plot(randn(30).cumsum(),color="k",linestyle="dashed",marker="o"))

# print plt.xlim()

# fig=plt.figure();ax=fig.add_subplot(1,1,1)
# show(ax.plot(randn(1000).cumsum()))
# ax.plot(randn(1000).cumsum())

# ticks=ax.set_xticks([0,250,500,750,1000])
# labels=ax.set_xticklabels(["one","two","three","four","five"],
#                           rotation=30,fontsize="small")
# ax.set_title("My first matplotlib plot")
# show(ax.set_xlabel("Stages"))


# fig=plt.figure();ax=fig.add_subplot(1,1,1)
# ax.plot(randn(1000).cumsum(),"k",label="one")
# ax.plot(randn(1000).cumsum(),"k--",label="two")
# ax.plot(randn(1000).cumsum(),"k.",label="_nolegend_")
# show(ax.legend(loc="best"))
# ax.legend(loc="best")
# show(ax.text(400,20,"Hello World!",family="monospace",fontsize=10))



# from datetime import datetime
# fig=plt.figure();ax=fig.add_subplot(1,1,1)
#
# import pandas as pd
# data=pd.read_csv("spx.csv",index_col=0,parse_dates=True)
# spx=data["SPX"]
#
# spx.plot(ax=ax,style="k-")
#
# crisis_data=[
#     (datetime(2007,10,11),"Peak of bull market"),
#     (datetime(2008,3,12),"Bear Stearns Fails"),
#     (datetime(2008,9,15),"Lehman Bankruptcy")
# ]
#
# for date,label in crisis_data:
#     ax.annotate(label,xy=(date,spx.asof(date)+50),
#                 xytext=(date,spx.asof(date)+200),
#                 arrowprops=dict(facecolor="black"),
#                 horizontalalignment="left",
#                 verticalalignment="top")
# ax.set_xlim(["1/1/2007","1/1/2011"])
# ax.set_ylim([600,1800])
# show(ax.set_title("Important dates in 2008-2009 financial crsis"))



# fig=plt.figure();ax=fig.add_subplot(1,1,1)
# rect=plt.Rectangle((0.2,0.75),0.4,0.15,color="k")
# circ=plt.Circle((0.7,0.2),0.15,color="b")
# pgon=plt.Polygon([[0.15,0.15],[0.35,0.4],[0.2,0.6]],color="g")
#
# ax.add_patch(rect)
# ax.add_patch(circ)
# ax.add_patch(pgon)

# plt.show()
# plt.savefig("figpath.png",dpi=400,bbox_inches="tight")


# from io import StringIO
# buffer=StringIO()
# plt.savefig(buffer)
# plot_data=buffer.getvalue()


# plt.rc("figure",figsize=(10,10))

# font_options={"family":"monospace",
#               "weight":"bold",
#               "size":20}
# plt.rc("font",**font_options)
# plt.show()


import pandas as pd
# s=pd.Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
# s.plot()
# plt.show()



# df=pd.DataFrame(np.random.randn(10,4).cumsum(0),
#                 columns=["A","B","C","D"],
#                 index=np.arange(0,100,10))
# df.plot()
# plt.show()


#柱状图
# fig,axes=plt.subplots(2,1)
# data=pd.Series(np.random.randn(16),index=list("abcdefghijklmnop"))
# data.plot(kind="bar",ax=axes[0],color="k")
# data.plot(kind="barh",ax=axes[1],color="k")
# plt.show()


# df=pd.DataFrame(np.random.randn(6,4),
#                 index=["one","two","three","four","five","six"],
#                 columns=pd.Index(["A","B","C","D"],name="Genus"))
#
# df.plot(kind="barh",stacked=True)
# plt.show()


# tips=pd.read_csv("tips.csv")
# party_counts=pd.crosstab(tips.day,tips.size)
# print party_counts

# #规格化
# party_pcts=party_counts.div(party_counts.sum(1).astype(float),axis=0)
# # print party_pcts
# party_pcts.plot(kind="bar",stacked=True)
# plt.show()


# comp1=np.random.normal(0,1,size=200)
# comp2=np.random.normal(10,2,size=200)
# values=pd.Series(np.concatenate([comp1,comp2]))
# values.hist(bins=100,color="k",normed=True)
#
# from scipy.stats import gaussian_kde
# values.plot(kind="kde",style="k--")
# plt.show()


# macro=pd.read_csv("macrodata.csv")
# data=macro[["cpi","m1","tbilrate","unemp"]]
#
# trans_data=np.log(data).diff().dropna()
# print trans_data[-5:]

# plt.scatter(trans_data["m1"],trans_data["unemp"])
# plt.title("Changes in log %s vs. log %s" % ("m1","unemp"))
# plt.show()

# pd.scatter_matrix(trans_data)
# plt.show()
