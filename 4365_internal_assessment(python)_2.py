# -*- coding: utf-8 -*-
"""4365- Internal Assessment(Python) --2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IoUZSCIC2yi7fraoe-AKcBCzoU7Rfbyy
"""

#1

import pandas as pd
import numpy as np

data = np.random.randint(50, size=(1,5,10))
print('data', data)

min = np.min(data)
print('min', min)

max = np.max(data)
print('max', max)

sum = np.sum(data)
print('sum', sum)

mean = np.mean(data)
print('mean', mean)

std = np.std(data)
print('Standard_deviation', std)

#2

health_data = np.array([[160, 70, 30],   # height, weight, age for individual 1
                        [165, 65, 35],   # height, weight, age for individual 2
                        [170, 75, 40]])  # height, weight, age for individual 3


import numpy as np

def normalize_data(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    normalized_data = (data - mean) / std
    return normalized_data
normalized_health_data = normalize_data(health_data)
print(normalized_health_data)

#3
import pandas as pd
import numpy as np

dt = pd.read_csv('/Q15_student_grades.csv')
dt

#dt(['StudentID'],['subjects']).groupby(dt['StudentID']).mean()
dt['Average_score'] = dt['Grade'].groupby(dt['StudentID']).mean()
dt.replace('NaN', 'Not Available')
dt

#4
start_temp = 15
end_temp = 25

num_measurements = 24
temperature_readings = np.linspace(start_temp, end_temp, num_measurements)

print(temperature_readings)

#5
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
window_size = 5

import numpy as np
import pandas as pd

def moving_average(data, window_size):
    df = pd.DataFrame(data, columns=['Closing Price'])
    rolling_mean = df['Closing Price'].rolling(window=window_size).mean()
    return rolling_mean
daily_closing_prices = np.array([100, 102, 98, 105, 107, 110, 108, 112, 115, 118, 120])
window_size = 5
moving_avg_pandas = moving_average(daily_closing_prices, window_size)

print(moving_avg_pandas)

weights = np.ones(window_size) / window_size
moving_avg_numpy = np.convolve(daily_closing_prices, weights, mode='valid')

print(moving_avg_numpy)

#6
matrixtor = [0, 0]
cov_matrix = [[1, 0.5], [0.5, 2]]
samples = np.random.multivariate_normal(matrix, cov_matrix, 100)

df_samples = pd.DataFrame(samples, columns=['Feature1', 'Feature2'])

print(df_samples.head(10))

df_samples.to_csv('synthetic_data.csv')

#7
properties_matrix = np.array([[1, 2,3],
                      [4, 5,6],
                      [7, 8, 9]])

determinant = np.linalg.det(properties-matrix)
print(determinant)

#8
matrix = np.random.randint(1, 11, size=(3, 3))
filtered_matrix = matrix[matrix > 5]

print("Original matrix:")
print(matrix)
print('Conditional_matrix(greater than 5) --->',filtered_matrix)

#9

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}

dt = pd.DataFrame(data)
dt
dt.groupby('Name')['City'](dt['Age']>45)

# 10

data = {'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
'Sales': [70000, 50000, 30000, 40000, 60000]}

df = pd.DataFrame(data)

average_sales = df.groupby('Department')['Sales'].mean().reset_index()

average_sales['Rank'] = average_sales['Sales'].rank(ascending=False)
average_sales = average_sales.sort_values('Rank')
print(average_sales)

#11
data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}

df = pd.DataFrame(data)

fruit_df = df[df['Category'] == 'Fruit']
average_price = fruit_df['Price'].mean()

potential_promotions = fruit_df[(fruit_df['Price'] > average_price) & (~fruit_df['Promotion'])]

print(potential_promotions[['Product', 'Price']])

#13

#14

#15