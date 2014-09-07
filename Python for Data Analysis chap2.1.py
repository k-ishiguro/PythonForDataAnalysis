# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json

# <codecell>

path = "pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt"
records = [json.loads(line) for line in open(path)] # open the "path" file and read lines by JSON loader

# <codecell>

records[0]

# <codecell>

records[0,tz] # you can use symbols as a index of arrays!!

# <codecell>

records[0,'tz'] # you know this is not numpy array. 

# <codecell>

records[0]['tz'] # a raw value

# <codecell>

print records[0]['tz'] # so print interpret the input as String

# <codecell>

time_zones = [rec['tz'] for rec in records] # for all elements in records, list 'tz' entries

# <codecell>

time_zones = [rec['tz'] for rec in records if 'tz' in rec ] # for all elements who has 'tz' entry, list 'tz' entries

# <codecell>

time_zones[:10]

# <codecell>

def get_counts(sequence):
    counts = []
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1 
    return conuts
# end get_counts

from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to -
    for x in sequence:
        counts[x] += 1
    # end for
    return counts
# end get_counts2

# <codecell>

counts = get_counts2(time_zones)
counts['America/New_York']

# <codecell>

len(time_zones)

# <codecell>

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:] # this is inverted
# end top_counts

top_counts(counts)

# <codecell>

top_counts(counts, 14)

# <codecell>

from collections import Counter # Ah, this is convenient counter class. 
counts = Counter(time_zones)
counts.most_common(10)

# <codecell>

from pandas import DataFrame, Series
frame = DataFrame(records) # Wow! what'a nice table! so 
frame

# <codecell>

frame['tz'][:10] # this is called Series

# <codecell>

tz_counts = frame['tz'].value_counts()
tz_counts[:10]

# <codecell>

clean_tz = frame['tz'].fillna('Missing') # fill all missing entries with "Missing"
clean_tz[clean_tz == ''] = 'Unknown' #
tz_counts = clean_tz.value_counts()
tz_counts[:10]

# <codecell>

tz_counts[:10].plot(kind='barh', rot=0)

# <codecell>

frame['a'][1]

# <codecell>

frame['a'][51]

# <codecell>

results=Series([x.split()[0] for x in frame.a.dropna()])
results[:5]

# <codecell>

print results.shape

# <codecell>

results.value_counts()[:10]

# <codecell>

cframe=frame[frame.a.notnull()] # note Frame is pandas strucure, but seemleslly Numpy
cframe.shape

# <codecell>

operating_system = np.where( cframe['a'].str.contains('Windows'),'windows','Not Windows' ) # contains might be a Frame function
operating_system[:5]

# <codecell>

by_tz_os = cframe.groupby(['tz', operating_system]) # panads.core.groupby.DataFrameGroupBy data

# <codecell>

type(by_tz_os)

# <codecell>

by_tz_os.size() # Ah, so return the unique sets and its frequency

# <codecell>

agg_counts = by_tz_os.size().unstack() # make it into 2-way relational data table

# <codecell>

by_tz_os.size().unstack().fillna(0) # and also replace NaN to 0

# <codecell>

indexer = agg_counts.sum(1).argsort() # so this is like piping in command shells. sum over 2nd index = OS

# <codecell>

indexer[:10]

# <codecell>

type(agg_counts)

# <codecell>

count_subset = agg_counts.take(indexer)[-10:]

# <codecell>

print count_subset

# <codecell>

count_subset = count_subset.fillna(0)
print count_subset=

# <codecell>

count_subset.plot(kind='bar', stacked=True) # might be a DataFrame method for plotting. What a nice "DATA ANALYSIS" library!!

# <codecell>

normed_subset = count_subset.div(count_subset.sum(1), axis=0) # so divide table elements for first axis, element-wise
normed_subset.plot(kind='bar', stacked=True)

# <codecell>


