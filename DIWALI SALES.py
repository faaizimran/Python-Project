# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 20:43:14 2024

@author: faaiz
"""

# Install required libraries (use command line or Anaconda prompt)
# pip install seaborn
# pip install matplotlib
# pip install pandas
# pip install numpy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure plots appear inline in Jupyter; in Spyder, use plt.show() after each plot for display
# %matplotlib inline  # Remove or replace this with plt.show() in Spyder

# Load dataset
df = pd.read_csv(r'C:\Users\faaiz\Downloads\Python_Diwali_Sales_Analysis-main\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv', encoding='unicode_escape')

# Initial data inspection
print(df.shape)
print(df.head())
print(df.info())

# Drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# Check for null values and drop them
print(pd.isnull(df).sum())
df.dropna(inplace=True)

# Change data type
df['Amount'] = df['Amount'].astype('int')
print(df['Amount'].dtypes)

# Rename column
df.rename(columns={'Marital_Status': 'Shaadi'}, inplace=True)

# Data description
print(df.describe())
print(df[['Age', 'Orders', 'Amount']].describe())

# Bar chart for Gender and its count
ax = sns.countplot(x='Gender', data=df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Grouped bar chart for Gender vs total Amount
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Gender', y='Amount', data=sales_gen)
plt.show()

# Bar chart for Age Group and Gender
ax = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sales_age)
plt.show()

# Top 10 states by number of orders
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize': (15, 5)})
sns.barplot(data=sales_state, x='State', y='Orders')
plt.show()

# Top 10 states by total amount
sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize': (15, 5)})
sns.barplot(data=sales_state, x='State', y='Amount')
plt.show()

# Bar chart for Marital Status count
ax = sns.countplot(data=df, x='Marital_Status')
sns.set(rc={'figure.figsize': (7, 5)})
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Marital Status vs total Amount by Gender
sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.set(rc={'figure.figsize': (6, 5)})
sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender')
plt.show()

# Bar chart for Occupation count
sns.set(rc={'figure.figsize': (20, 5)})
ax = sns.countplot(data=df, x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Total Amount by Occupation
sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data=sales_state, x='Occupation', y='Amount')
plt.show()

# Bar chart for Product Category count
sns.set(rc={'figure.figsize': (20, 5)})
ax = sns.countplot(data=df, x='Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)
plt.show()

# Total Amount by Product Category
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data=sales_state, x='Product_Category', y='Amount')
plt.show()

# Top 10 products by number of orders
sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.barplot(data=sales_state, x='Product_ID', y='Orders')
plt.show()

# Top 10 most sold products (bar plot)
fig1, ax1 = plt.subplots(figsize=(12, 7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
plt.show()