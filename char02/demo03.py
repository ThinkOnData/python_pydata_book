#coding:utf-8

#1880-2010年间全美婴儿姓名，仅含有当年出现超过5次的名字

import pandas as pd
names1880=pd.read_csv("names/yob1880.txt",names=["name","sex","births"])#文件是非常标准的以逗号隔开的形式，所以用read_csv加载
# print names1880


#用births列的sex分子小计表示该年度的births总计
# print names1880.groupby("sex").births.sum()


#将所有数据组装到一个DataFrame中，并加上year字段
years=range(1880,2011)#1880-2010
pieces=[]
columns=["name","sex","births"]

for year in years:
    path="names/yob%d.txt" % year
    frame=pd.read_csv(path,names=columns)

    frame['year']=year
    pieces.append(frame)

names=pd.concat(pieces,ignore_index=True)#concat默认按行组合，ignore_index不保留read_csv返回的原始行号
# print names


total_births=names.pivot_table("births",index="year",columns="sex",aggfunc="sum")
# print total_births.tail()
from pylab import *
# show(total_births.plot(title="Total births by sex and year"))


#插入prop列，用于存放指定名字的婴儿数相对于总出生数的比例，先按year和sex分组
def add_prop(group):
    births=group.births.astype(float)#整数除法会向下圆整，births是整数，转成浮点数，python3不需要

    group["prop"]=births/births.sum()
    return group

names=names.groupby(["year","sex"]).apply(add_prop)
# print names


#执行这样分组处理时，应该做一些有效性检查，比如验证所有分组的prop的总和是否为1
# print np.allclose(names.groupby(["year","sex"]).prop.sum(),1)#近似于1


#取sex/year组合前1000各名字
def get_top1000(group):
    return group.sort_values(by="births",ascending=False)[:1000]

grouped=names.groupby(["year","sex"])
top1000=grouped.apply(get_top1000)
# print top1000


##分析命名趋势
boys=top1000[top1000.sex=="M"]
girls=top1000[top1000.sex=="F"]

total_births=top1000.pivot_table("births",index="year",columns="name",aggfunc="sum")
# print total_births

subset=total_births["John"]
# show(subset.plot(subplots=True,figsize=(12,10),grid=False,title="Number of births per year"))#不能传入array


##评估命名多样性的增长
table=top1000.pivot_table("prop",index="year",columns="sex",aggfunc="sum")
# show(table.plot(title="Sum of table1000.prop by year and sex",yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10)))


df=boys[boys.year==2010]
# print df


#对prop降序排列后，希望知道多少个名字总数加起来够50%
#NumPy矢量方法：先计算prop的累计和cumsum，再通过serchsorted方法找出0.5应该被插入在哪个位置才能保证不破坏顺序
prop_cumsum=df.sort_values(by="prop",ascending=False).prop.cumsum()
# print prop_cumsum[:10]
# print prop_cumsum.searchsorted(0.5)#索引从0开始，结果+1


df=boys[boys.year==1900]
in1900=df.sort_values(by="prop",ascending=False).prop.cumsum()
# print in1900.searchsorted(0.5)+1


def get_quantile_count(group,q=0.5):
    group=group.sort_values(by="prop",ascending=False)
    return group.prop.cumsum().searchsorted(1)+1

diversity=top1000.groupby(["year","sex"]).apply(get_quantile_count)
diversity=diversity.unstack("sex")
# print diversity.head()



##"最后一个字母"的变革
get_last_letter=lambda x:x[-1]#从name列取出最后一个字母
last_letters=names.name.map(get_last_letter)
last_letters.name="last_letter"

table=names.pivot_table("births",index=last_letters,columns=["sex","year"],aggfunc="sum")
# print table

subtable=table.reindex(columns=[1910,1960,2010],level="year")
#print subtable.head()


letter_prop=subtable/subtable.sum().astype(float)
import matplotlib.pyplot as plt
#fig,axes=plt.subplots(2,1,figsize=(10,8))

#show(letter_prop["M"].plot(kind="bar",rot=0,ax=axes[0],title="Male"))
#show(letter_prop["F"].plot(kind="bar",rot=0,axes=[1],title="Female",legend=False))


letter_prop=table/table.sum().astype(float)
dny_ts=letter_prop.ix[["d","n","y"],"M"].T#转置
# print dny_ts.head()

# show(dny_ts.plot())


##变成女孩名字的男孩名字
all_names=top1000.name.unique()
mask=np.array(["lel"in x.lower() for x in all_names])
lesley_like=all_names[mask]
# print lesley_like #['Lela' 'Lelia' 'Lella' 'Leland' 'Lelah' 'Lelar' 'Clella' 'Clell' 'Mcclellan''Nallely''Kalel']

filtered=top1000[top1000.name.isin(lesley_like)]
filtered.groupby("name").births.sum()

table=filtered.pivot_table("births",index="year",columns="sex",aggfunc="sum")

table=table.div(table.sum(1),axis=0)

table.tail()

show(table.plot(style={"M":"k-","F":"k--"}))
