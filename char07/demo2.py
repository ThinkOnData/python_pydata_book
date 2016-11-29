#coding:utf-8

#USDA食品数据库

import json

from pandas.core.algorithms import quantile

db=json.load(open("foods-2011-10-03.json"))
# print len(db)

# print db[0].keys()

# print db[0]["nutrients"][0]


import pandas as pd
nutrients=pd.DataFrame(db[0]["nutrients"])
# print nutrients[:7]

info_keys=["descripton","group","id","manufacturer"]
info=pd.DataFrame(db,columns=info_keys)
# print info[:5]

# print pd.value_counts(info.group)[:10]


nutrients=[]
for rec in db:
    fnuts=pd.DataFrame(rec["nutrients"])
    fnuts["id"]=rec["id"]
    nutrients.append(fnuts)
nutrients=pd.concat(nutrients,ignore_index=True)
# print nutrients.duplicated().sum()

nutrients=nutrients.drop_duplicates()
col_mapping={"descripton":"food","group":"fgroup"}
info=info.rename(columns=col_mapping,copy=False)
# print info
col_mapping={"description":"nutrient","group":"nutgroup"}
nutrients=nutrients.rename(columns=col_mapping,copy=False)

ndata=pd.merge(nutrients,info,on="id",how="outer")
# print ndata.ix[30000]

from pylab import *
result=ndata.groupby(["nutrient","fgroup"])["value"].quantile(0.5)
# show(result["Zinc, Zn"].sort_values().plot(kind="barh"))

by_nutrient=ndata.groupby(["nutgroup","nutrient"])
get_maximum=lambda x:x.xs(x.value.idxmax())
get_minimum=lambda x:x.xs(x.value.idxmin())

max_foods=by_nutrient.apply(get_maximum)[["value","food"]]

# print max_foods
