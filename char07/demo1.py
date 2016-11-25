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









