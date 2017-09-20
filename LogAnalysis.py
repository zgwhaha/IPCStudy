from pandas import Series, DataFrame
import pandas as pd



# af=pd.read_csv('E:/self/python/pydata/pydata-book/ch06/ex6.csv')
# m=af['key'].value_counts()
# print(m)

# af=pd.read_csv('E:/self/python/pydata/pydata-book/ch06/ex6.csv',chunksize=1000)
# tot = Series([])
# for piece in af:
#     tot = tot.add(piece['key'].value_counts(),fill_value=0)
# tot = tot.sort_index(ascending=False)
# print(tot[:50])
# df=pd.read_csv('E:/self/python/IPC/IPCStudy/ATest.csv')
# print(df)
cf=pd.read_table('E:/self/python/IPC/IPCStudy/ATest2.csv',sep = ',')
sf = cf[cf['PLCNO']=='PLC_02']
print(sf)