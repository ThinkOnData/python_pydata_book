#coding:utf-8

path="usagov_bitly_data2012-03-16-1331923249.txt"
#print open(path).readline()



import json
path="usagov_bitly_data2012-03-16-1331923249.txt"
records=[json.loads(line) for line in open(path)] #列表推导式list comprehension
#print records[0]



##用纯Python代码对时区进行计数

time_zones=[rec['tz'] for rec in records if 'tz' in rec]
#print time_zones[:10]



def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts

#标准库简洁写法
from collections import defaultdict

def get_counts2(sequence):
    counts=defaultdict(int)#所有的值均会被初始化为0
    for x in sequence:
        counts[x]+=1
    return counts

counts=get_counts(time_zones)
#print counts[u'America/New_York']
#print len(time_zones)



#得到前10位的时区及其计数值
def top_counts(count_dict,n=10):
    value_key_pairs=[(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]
#print top_counts(counts)

#标准库中collections.Counter类
from collections import Counter

counts=Counter(time_zones)
#print counts.most_common(10)



##用pandas对时区进行计数，将数据表示为一个表格

from pandas import DataFrame,Series
import pandas as pd;import numpy as np

frame=DataFrame(records)
#print frame['tz'][:10] #摘要视图summary view

tz_counts=frame['tz'].value_counts()#Series对象的方法value_counts()
#print tz_counts[:10]



clean_tz=frame['tz'].fillna('Missing')#fillna函数替换缺失值NA
clean_tz[clean_tz==""]='Unknown'#未知值（空字符串）通过布尔型数组索引加以替换
tz_counts=clean_tz.value_counts()
#print tz_counts[:10]

from pylab import *
#show(tz_counts[:10].plot(kind="barh",rot=0))#画出水平条形图


# {
#     "a": "Mozilla\/5.0 (Windows NT 6.1; WOW64) AppleWebKit\/535.11 (KHTML, like Gecko) Chrome\/17.0.963.78 Safari\/535.11",
#     "c": "US",
#     "nk": 1,
#     "tz": "America\/New_York",
#     "gr": "MA",
#     "g": "A6qOVH",
#     "h": "wfLQtf",
#     "l": "orofrog",
#     "al": "en-US,en;q=0.8",
#     "hh": "1.usa.gov",
#     "r": "http:\/\/www.facebook.com\/l\/7AQEFzjSi\/1.usa.gov\/wfLQtf",
#     "u": "http:\/\/www.ncbi.nlm.nih.gov\/pubmed\/22415991",
#     "t": 1331923247,
#     "hc": 1331822918,
#     "cy": "Danvers",
#     "ll": [
#         42.576698,
#         -70.954903
#     ]
# }

#将“agent”字符串的第一节分离出来得到另外一份用户行为摘要
results=Series([x.split()[0] for x in frame.a.dropna()])
#print results[:5]

#print results.value_counts()[:8]


cframe=frame[frame.a.notnull()]#移除agent缺失数据
operating_system=np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')#计算各行是否是Windows

by_tz_os=cframe.groupby(['tz',operating_system])#根据时区和新得到的操作系统列表对数据进行分组

agg_counts=by_tz_os.size().unstack().fillna(0)#size对分组结果进行计数，unstack对计数结果进行重塑（行列索引和值互换）
#print agg_counts[:10]


#选取最长出现的行数，构造一个间接索引数组
indexer=agg_counts.sum(1).argsort()
#print indexer[:10]

count_subset=agg_counts.take(indexer)[-10:] #take按照顺序截取最后10行
#print count_subset


#show(count_subset.plot(kind="barh",stacked=True))#stacked=True生成堆积条形图

normed_subset=count_subset.div(count_subset.sum(1),axis=0)#各行规范化为“总计为1”
#show(normed_subset.plot(kind="barh",stacked=True))