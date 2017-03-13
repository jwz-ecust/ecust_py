import json
import matplotlib.pyplot
from pandas import DataFrame, Series
import numpy as np

record = [json.loads(i) for i in open('./usagov_bitly_data2012-03-16-1331923249.txt')]
frame = DataFrame(record)
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz=='']='zhangjiawei'
tz_counts=clean_tz.value_counts()
tz_counts[:10].plot(kind='barh',rot=0)


cframe = frame[frame.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')

by_tz_os = cframe.groupby(['tz',operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
print indexer[-10:]