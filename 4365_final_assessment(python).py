# -*- coding: utf-8 -*-
"""4365_Final Assessment(python)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1D7ICQfcY52bYE6z4CQscnvqPcb4jF_oY
"""

#1 --> a
import pandas as pd
import numpy as np

dt = pd.read_csv("/content/Final Dataset - IPL.csv")
dt.head(6)

dt.info()

#1 -->b

dt.shape
# 74 rows and 20 columns

#2
dt.isnull().sum()

# There are no missing values in the data
# No duplicates found

dt['venue'].value_counts()

#3
dt.describe()

import matplotlib.pyplot as plt
import seaborn as sns

#4
from matplotlib import pyplot as plt
import seaborn as sns
_df_4.groupby('date').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

sns.displot(dt['margin'], kde= True, color = 'r')

dt.plot(x='match_winner', y=['first_ings_score','second_ings_score'], kind = 'bar', grid =True)

# This is an insight of first innings
from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['match_id']
  ys = series['first_ings_score']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = _df_12.sort_values('match_id', ascending=True)
for i, (series_name, series) in enumerate(df_sorted.groupby('date')):
  _plot_series(series, series_name, i)
  fig.legend(title='date', bbox_to_anchor=(1, 1), loc='upper left')
sns.despine(fig=fig, ax=ax)
plt.xlabel('match_id')
_ = plt.ylabel('first_ings_score')

dt['best_bowling'].unique()

Players = ['Dwayne Bravo', 'Kuldeep Yadav', 'Mohammed Siraj',
       'Mohammed Shami', 'Yuzvendra Chahal', 'Wanindu Hasaranga',
       'Ravi Bishnoi', 'Umesh Yadav', 'Jasprit Bumrah', 'Lockie Ferguson',
       'Rahul Chahar', 'Avesh Khan', 'Murugan Ashwin', 'Rashid Khan',
       'Washington Sundar', 'Harshal Patel', 'T Natarajan',
       'Maheesh Theekshana', 'Odean Smith', 'Josh Hazlewood',
       'Umran Malik', 'Axar Patel', 'Daniel Sams', 'Prasidh Krishna',
       'Andre Russell', 'Krunal Pandya', 'Kagiso Rabada', 'Kuldeep Sen',
       'Pradeep Sangwan', 'Rilley Meredith', 'Mohsin Khan',
       'Mukesh Choudhary', 'Tim Southee', 'Khaleel Ahmed', 'Moeen Ali',
       'Chetan Sakariya', 'Trent Boult', 'Shardul Takur',
       'Ramandeep Singh', 'Prashant Solanki', 'Harpreet Brar',
       'Hardik Pandya']

x =dt['best_bowling'].value_counts()
plt.pie(x, labels= Players)
plt.show()

dt['venue'].value_counts()

from matplotlib import pyplot as plt
_df_10.plot(kind='scatter', x='first_ings_wkts', y='second_ings_score', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

#5

#2
import seaborn as sns
import matplotlib.pyplot as plt
#flights = sns.load_dataset("flights")
#a = dt.pivot("toss_winner","match_winner", "margin")
aa = dt[dt['']]
sns.heatmap(a, annot=True, fmt="d", cmap="YlGnBu")
plt.show()

sns.heatmap(data= dt.corr(), annot= True, cmap= 'Dark2')

from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['team2'].value_counts()
    for x_label, grp in _df_22.groupby('team1')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('team1')
_ = plt.ylabel('team2')

b = dt[["match_winner","toss_winner"]]
plt.scatter(b["match_winner"],b["toss_winner"])
plt.show()

#6

# finding the outliers

sns.boxenplot(data= dt, x= 'toss_winner', y ='highscore', hue = 'toss_decision')
plt.title("Finding outliers using box plot")
plt.show()

# the rounded of scircle away fro the vertical line in tbe plot are the outliers

dt['toss_winner'].value_counts()

dt['match_winner'].value_counts()

rct = dt.groupby(["match_winner"]).highscore.count()
sns.boxplot(rct,color="g")

#7

dt1 = dt.groupby('match_winner')['player_of_the_match'].sum()
plt.figure(figsize=(8,4))
dt1.plot(kind='barh', color='skyblue')
plt.title('Total Sales by Category')
plt.xlabel('Index')
plt.ylabel('Sales')
plt.show()

dt['player_of_the_match'].value_counts().sort_values()

# Player Kuldeep yadav has become the player of the match maong all the match follwed by jos buttler and hardik pandya

# 8

dt['best_bowling'].unique()

player = dt.groupby('best_bowling')['first_ings_wkts'].sum()
player

df3 = dt[dt["best_bowling"]=="Axar Patel"]
sns.countplot(df3["first_ings_wkts"])
plt.show()

# Axar Patel, T Natarajan, Umesh Yadav,Umran Malik,Daniel Sams are the best bowlers among all the matches by taking 10 wickets in one innings

man_of_the_match =dt.groupby('top_scorer')['highscore'].sum()
man_of_the_match

man_of_the_match.sort_values()

sns.scatterplot(data= dt,x= 'highscore', y='margin' )

from matplotlib import pyplot as plt
_df_37['second_ings_score'].plot(kind='line', figsize=(8, 4), title='first_innigs_score')
plt.gca().spines[['top', 'right']].set_visible(False)

# 9
#    INSIGHT DESCRIPTION

'''
MOST MATCH HAPPENING VENUES

Wankhede Stadium, Mumbai                      -  21
Dr DY Patil Sports Academy, Mumbai            -  20
Brabourne Stadium, Mumbai                     -  16
Maharashtra Cricket Association Stadium,Pune  -  13
Eden Gardens, Kolkata                         -   2
Narendra Modi Stadium, Ahmedabad              -   2


toss_winner
Gujarat      10
Hyderabad    10
Mumbai        9
Kolkata       8
Delhi         8
Banglore      8
Lucknow       7
Chennai       6
Punjab        4
Rajasthan     4

There is a correlation between toss wining and match winning.
The teams which won the toss had won the most the matches.

match_winner
Gujarat      12
Rajasthan    10
Banglore      9
Lucknow       9
Delhi         7
Punjab        7
Kolkata       6
Hyderabad     6
Chennai       4
Mumbai        4




Player Kuldeep yadav has become the player of the match maong all the match follwed by jos buttler and hardik pandya

Axar Patel, T Natarajan, Umesh Yadav,Umran Malik,Daniel Sams are the best bowlers among all the matches by taking 10 wickets in one innings

'''







