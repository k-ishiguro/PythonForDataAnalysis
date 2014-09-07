# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# <codecell>

names1880 = pd.read_csv('pydata-book/ch02/names/yob1880.txt', names=['name','sex','births'])
names1880

# <codecell>

names1880.groupby('sex').births.sum()

# <codecell>

years = range(1880, 2010)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = 'pydata-book/ch02/names/yob%d.txt' % year # this is how to insert integers?
    frame = pd.read_csv(path, names=columns)
    
    frame['year'] = year
    pieces.append(frame)
# end years-for

names = pd.concat(pieces, ignore_index=True) # concatenate list of frames into one frame
names

# <codecell>

total_births = names.pivot_table('births', rows='year', cols='sex', aggfunc=sum) # sum up 'births' values, for each (year, sex) pair
total_births.tail()

# <codecell>

total_births.plot(title='Total births by sex and year') # row (year) --> x axis, column (sex) --> lines, entries (birth sum) --> y axis. also automtically imports attribute names.

# <codecell>

def add_prop(group):
    births = group.births.astype(float) # type cat for frame entries?
    group['prop'] = births / births.sum()
    return group
# end add_prop-def
names = names.groupby(['year', 'sex']).apply(add_prop)
names

# <codecell>

np.allclose(names.groupby(['year', 'sex']).prop.sum(), 1) # I still don't understand the groupby func....

# <codecell>

def get_top1000(group):
    return group.sort_index(by='births', ascending=False)[:1000]
# end get_top1000-def

grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
top1000

# <codecell>

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']
total_births = top1000.pivot_table('births', rows='year', cols='name', aggfunc=sum)
total_births

# <codecell>

subset = total_births[['John', 'Harry', 'Mary','Marilyn']]
subset.plot(subplots=True, figsize=(12,10), grid=False, title="Number of births per year")

# <codecell>

table = top1000.pivot_table('prop', rows='year', cols='sex', aggfunc=sum) # create a new table, row index is year, column index is sec, each entry is a sum of proportaions
table.plot(title="Sum of table1000.prop by year and sex", yticks=np.linspace(0,1.2,13), xticks=range(1880,2020,10))

# <codecell>

df = boys[boys.year == 2009]
type(df)

# <codecell>

df

# <codecell>

df_sorted = df.sort_index(by='prop', ascending=False)
df_sorted

# <codecell>

prop_cumsum = df_sorted.prop.cumsum()
prop_cumsum[:5]

# <codecell>


# <codecell>


# <codecell>

# This is called anonymous function by lambda
get_last_letter = lambda x: x[-1] # works as like def-function
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'
table = names.pivot_table('births', rows=last_letters, cols=['sex', 'year'], aggfunc=sum)

# <codecell>

last_letters.head(5)

# <codecell>

last_letters.tail(5)

# <codecell>

subtable=table.reindex(columns=[1910, 1960, 2009], level='year')
subtable.head()

# <codecell>

letter_prop = subtable / subtable.sum().astype(float)

# <codecell>

fig, axes = plt.subplots(2, 1, figsize=(10,8))
letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)
# hmm, we see that many boys' name end with 'n' rapidly increase these days!

# <codecell>

letter_prop = table / table.sum().astype(float)
dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M']
dny_ts.head() 
# note that rows and  columns are inverted with Python textbook!!

# <codecell>

dny_ts.T.plot(style={'d':'-.', 'n':'-', 'y':':'}) # this is convenient! pandas.plot() is really smart!

# <codecell>

all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
lesley_like

# <codecell>

filtered = top1000[top1000.name.isin(lesley_like)]

# <codecell>

filtered.groupby('name').births.sum()

# <codecell>

table = filtered.pivot_table('births', rows='year', cols='sex', aggfunc=sum)

# <codecell>

table = table.div(table.sum(1), axis=0) # normalized sum to one
table.tail()

# <codecell>

table.head()

# <codecell>

table.plot(style={'M':'b-', 'F':'r--'})

# <codecell>


