#coding:utf-8

#MoviesLens 1M数据集

import pandas as pd
unames=["user_id","gender","age","occupation","zip"]
users=pd.read_table("users.dat",sep="::",header=None,names=unames,engine="python")#ERROR：engine=’Python’

rnames=["user_id","movie_id","rating","timestamp"]
ratings=pd.read_table("ratings.dat",sep="::",header=None,names=rnames,engine="python")

mnames=["movie_id","title","genres"]
movies=pd.read_table("movies.dat",sep="::",header=None,names=mnames,engine="python")

#pandas的merge函数会根据列名的重叠情况推断出哪些列是合并键
data=pd.merge(pd.merge(ratings,users),movies)
#print data.ix[0]


#按性别计算每部电影的平均得分
mean_ratings=data.pivot_table("rating",index="title",columns="gender",aggfunc="mean")#ERROR：用 index 替换 rows，用 columns 替换 cols
#print mean_ratings[:5]


#过滤掉评分数据不够25条的电影，先对title进行分组，然后利用size()得到一个含有电影分组大小的Series对象
rating_by_title=data.groupby("title").size()
#print rating_by_title[:10]

active_titles=rating_by_title.index[rating_by_title>=250]
#print active_titles

mean_ratings=mean_ratings.ix[active_titles]
#print mean_ratings


#为了了解女性观众最喜欢的电影，对F列降序排列
top_female_ratings=mean_ratings.sort_values(by="F",ascending=False)
#print top_female_ratings[:10]


#找出男性和女性观众分歧最大的电影，给mean_ratings加上一个用于存放平均得分之差的列，并对其进行排列
mean_ratings["diff"]=mean_ratings["M"]-mean_ratings["F"]
sorted_by_diff=mean_ratings.sort_values(by="diff")
#print sorted_by_diff[:15]

#print sorted_by_diff[::-1][:15]#反序

rating_std_by_title=data.groupby("title")["rating"].std()#根据电影名称分组的得分数据的标准差

rating_std_by_title=rating_std_by_title.ix[active_titles]#根据active_titles进行过滤

print rating_std_by_title.order(ascending=False)[:10]#根据值对Series进行降序排列
