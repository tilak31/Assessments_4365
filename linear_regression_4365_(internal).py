# -*- coding: utf-8 -*-
"""Linear Regression_4365 (internal)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XJBBgArF46uM7NbvGGDB8PdW9kh-cGaN
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score,mean_squared_error

df = pd.read_csv("/content/expenses.csv")
df

df.describe(include='all')

df.info()

df.isnull().sum()

df.duplicated().sum()

df = df.drop_duplicates()

df.duplicated().sum()

# Plot bar charts for categorical columns
for column in df.select_dtypes(include=['object']).columns:
    plt.figure(figsize=(10, 5))
    df[column].value_counts().plot(kind='bar')
    plt.title(f'Bar Chart of {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.show()

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numerical_columns].corr()
print("Correlation matrix:\n", correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
plt.show()

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
for i in range(len(numerical_columns)):
    for j in range(i + 1, len(numerical_columns)):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x=numerical_columns[i], y=numerical_columns[j])
        plt.title(f'Scatter Plot between {numerical_columns[i]} and {numerical_columns[j]}')
        plt.show()

# dummies

df1 = pd.get_dummies(df)
df1

# Handling Outliers

numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns

# Create a box plot for each numerical column
for column in numerical_columns:
    plt.figure(figsize=(15, 4))
    sns.boxplot(x=df[column])
    plt.title(f'Box Plot of {column}')
    plt.xlabel(column)
    plt.show()

Q1 = df['bmi'].quantile(0.25) #first quarter
Q3 = df['bmi'].quantile(0.75) #rest 3 quarters
iqr = Q3-Q1
lower_bound = Q1-1.5*iqr
upper_bound = Q3+1.5*iqr
df_proper= df[(df['bmi']>lower_bound) & (df['bmi']<upper_bound)]
df_proper

Q1 = df['charges'].quantile(0.25) #first quarter
Q3 = df['charges'].quantile(0.75) #rest 3 quarters
iqr = Q3-Q1
lower_bound = Q1-1.5*iqr
upper_bound = Q3+1.5*iqr
df_proper= df[(df['charges']>lower_bound) & (df['charges']<upper_bound)]
df_proper

encoded_df = pd.get_dummies(df)
encoded_df

df.dropna(axis= 0, inplace=True)

linear_reg = LinearRegression()
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['bmi'] = pd.to_numeric(df['bmi'], errors='coerce')
x = df.age.values.reshape(-1,1)
y = df['bmi'].values.reshape(-1,1)

linear_reg.fit(x,y)

b0 = linear_reg.predict(([[10000]]))
print("b0: ", b0)

b1 = linear_reg.coef_
print("b1: ", b1)

x_array = np.arange(min(df.age),max(df.age)).reshape(-1,1)  # this for information about the line to be predicted

plt.scatter(x,y)
y_head = linear_reg.predict(x_array)                                 # this is predict percentage of expenditure
plt.plot(x_array,y_head,color="red")
plt.show()

from sklearn import metrics
print("Mean Absolute Error: ", metrics.mean_absolute_error(x_array,y_head))
print("Mean Squared Error: ", metrics.mean_squared_error(x_array,y_head))
print("Root Mean Squared Error: ", np.sqrt(metrics.mean_squared_error(x_array, y_head)))

