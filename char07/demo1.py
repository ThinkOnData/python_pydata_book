#coding:utf-8

# 数据规整化：清理、转换、合并、重塑

#合并：
# pandas.merge：根据一个键或多个键将不同DataFrame中的行连接起来
# pandas.concat:沿着一条轴将多个对象堆叠到一起
# combine_first:将重复数据编接在一起，用一个对象的值填充另一个对象中的缺失值

import pandas as pd
df1= pd.DataFrame({"key":["b","b","a","c","a","a","b"],"data1":range(7)})
df2= pd.DataFrame({"key":["a","b","d"],"data2":range(3)})
# print df1
# print df2
# print pd.merge(df1,df2)


df3= pd.DataFrame({"lkey":["b","b","a","c","a","a","b"],"data1":range(7)})
df4= pd.DataFrame({"rkey":["a","b","d"],"data2":range(3)})
# print pd.merge(df3,df4,left_on="lkey",right_on="rkey")
# print pd.merge(df1,df2,how="outer")


df1=pd.DataFrame({"key":["b","b","a","c","a","b"],"data1":range(6)})
df2=pd.DataFrame({"key":["b","b","a","b","d"],"data2":range(5)})
# print pd.merge(df1,df2,on="key",how='left')


left=pd.DataFrame({"key1":["foo","foo","bar"],"key2":["one","two","one"],"lval":[1,2,3]})
right=pd.DataFrame({"key1":["foo","foo","bar","bar"],"key2":["one","one","one","two"],"rval":[4,5,6,7]})
# print pd.merge(left,right,on=["key1","key2"],how="outer")
# print left
# print right
# print pd.merge(left,right,on="key1",suffixes=("_left","_right"))


import numpy as np
lefth=pd.DataFrame({"key1":["Ohio","Ohio","Ohio","Nevada","Nevada"],
                    "key2":[2000,2001,2002,2001,2002],
                    "data":np.arange(5.)})
righth=pd.DataFrame(np.arange(12).reshape((6,2)),
                     index=[["Nevada","Nevada","Ohio","Ohio","Ohio","Ohio"],
                            [2001,2000,2000,2000,2001,2002]],
                     columns=["event1","event2"])
# print lefth
# print righth


# print pd.merge(lefth,righth,left_on=["key1","key2"],right_index=True)
# print pd.merge(lefth,righth,left_on=["key1","key2"],right_index=True,how="outer")


arr=np.arange(12).reshape((3,4))
# print np.concatenate([arr,arr],axis=1)


s1= pd.Series([0,1],index=["a","b"])
s2= pd.Series([2,3,4],index=["c","d","e"])
s3= pd.Series([5,6],index=["f","g"])
# print pd.concat([s1,s2,s3])


s4=pd.concat([s1*5,s3])
# print s4


# print pd.concat([s1,s4],axis=1,join="inner")

# print pd.concat([s1,s4],axis=1,join_axes=[["a","c","b","e"]])


result=pd.concat([s1,s1,s3],keys=["one","two","three"])
# print result.unstack()


result=pd.concat([s1,s1,s3],axis=1,keys=["one","two","three"])
# print result


a= pd.Series([np.nan, 2.5, np.nan,3.5,4.5,np.nan],
             index=["f","e","d","c","b","a"])
b= pd.Series(np.arange(len(a),dtype=np.float64),
             index=["f","e","d","c","b","a"])
b[-1]=np.nan
# print np.where(pd.isnull(a),b,a)
# print a

# print b[:-2].combine_first(a[2:])


data=pd.DataFrame(np.arange(6).reshape((2,3)),
                  index=pd.Index(["Ohio","Colorado"],name="state"),
                  columns=pd.Index(["one","two","three"],name="number"))
result=data.stack()
# print result.unstack("number")


s1= pd.Series([0,1,2,3],index=["a","b","c","d"])
s2=pd.Series([4,5,6],index=["c","d","e"])
data2=pd.concat([s1,s2],keys=["one","two"])
# print data2.unstack()
# print data2.unstack().stack()


df=pd.DataFrame({"left":result,"right":result+5},
                columns=pd.Index(["left","right"],name="side"))
# print df.unstack("state").stack("side")


data=pd.read_csv("macrodata.csv")
period=pd.PeriodIndex(year=data.year,quarter=data.quarter,name="date")
data=pd.DataFrame(data.to_records(),
                  columns=pd.Index(["realgdp","infl","unemp"],name="item"),
                  index=period.to_timestamp("D","end"))
# print data
ldata=data.stack().reset_index().rename(columns={0:"value"})
# print ldata[:10]


pivoted=ldata.pivot("date","item","value")
# print pivoted.head()


ldata["value2"]=np.random.rand(len(ldata))
# print ldata[:10]

pivoted=ldata.pivot("date","item")
# print pivoted["value"]

unstacked=ldata.set_index(["date","item"]).unstack("item")
# print unstacked

data=pd.DataFrame({"k1":["one"]*3+["two"]*4,
                   "k2":[1,1,2,3,3,4,4]})
# print data
data["v1"]=range(7)
# print data
# print data.drop_duplicates(["k1"])



data=pd.DataFrame({"food":["bacon","pulled pork","bacon","Pastrami","corned beef","Bacon","pastrami","honey ham","nova lox"],
                   "ounces":[4,3,12,6,7.5,8,3,5,6]})
# print data

meat_to_animal={"bacon":"pig",
                "pulled pork":"pig",
                "pastrami":"cow",
                "corned beef":"cow",
                "honey ham":"pig",
                "nova lox":"salmon"}


data["animal"]=data["food"].map(str.lower).map(meat_to_animal)
# print data

data["food"].map(lambda x:meat_to_animal[x.lower()])
# print data


#替换值
data= pd.Series([1.,-999.,2.,-999.,-1000.,3.])
# print data
# print data.replace(-999,np.nan)
# print data.replace({-999:np.nan,-1000:0})
# print data.replace([-999,-1000],[np.nan,0])


#重命名轴索引
data=pd.DataFrame(np.arange(12).reshape((3,4)),
                  index=["Ohio","Colorado","New York"],
                  columns=["one","two","three","four"])
# print data
# print data.index.map(str.upper)

data.index=data.index.map(str.upper)
# print data


# print data.rename(index={"OHIO":"INDIANA"},
#             columns={"threee":"peekaboo"})


_=data.rename(index={"OHIO":"INDIANA"},inplace=True) #总是返回DataFrame的引用
# print data


#离散化和面元（bin）划分
ages=[20,22,25,27,21,23,37,31,61,45,41,32]
bins=[18,25,35,60,100]
group_names=["Youth","YoughAdult","MiddleAged","Senior"]
cats=pd.cut(ages,bins,labels=group_names)
# print cats


data=np.random.rand(20)
# print data
# print pd.cut(data,4,precision=2)

data=np.random.randn(1000)
cats=pd.qcut(data,4)
# print pd.value_counts(cats)

cats=pd.qcut(data,[0,0.1,0.5,0.9,1.])
# print pd.value_counts(cats)


#检测和过滤异常值
np.random.seed(12345)
data=pd.DataFrame(np.random.randn(1000,4))
# print data.describe()


col=data[3]
# print col
# print col[np.abs(col)>3]


df=pd.DataFrame(np.arange(20).reshape((5,4)))
sampler=np.random.permutation(5)
# print df
# print sampler
# print df.take(sampler)


# print df.take(np.random.permutation(len(df))[:2])


bag=np.array([5,7,-1,6,4])
sampler=np.random.randint(0,len(bag),size=10)
draws=bag.take(sampler)
# print sampler
# print bag
# print draws


df=pd.DataFrame({"key":["b","b","a","c","a","b"],
                 "data1":range(6)})
# print pd.get_dummies(df["key"])


mnames=["movie_id","title","genres"]
movies=pd.read_table("movies.dat",sep="::",header=None,names=mnames,engine="python")
# print movies[:10]
















