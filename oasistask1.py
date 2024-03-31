# -*- coding: utf-8 -*-
"""OasisTask1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RYuCY_kXNxocW_4UUYgDXrVZLF2nyG6X

Exploratory Data Analysis (EDA) on Retail Sales Data
"""

import pandas as pd

!unzip "/content/archive (1).zip"

df = pd.read_csv("retail_sales_dataset.csv")
print(df.head())

# Summary statistics
summary_stats = df.describe()
print(summary_stats)

df["Date"] = pd.to_datetime(df["Date"])

# Set the Date column as the index
df.set_index("Date", inplace=True)

import matplotlib.pyplot as plt

# Plot daily sales
plt.figure(figsize=(10, 6))
df["Age"].plot()
plt.title("Retail Sales Trends")
plt.xlabel("Date")
plt.ylabel("Age")
plt.show()

# Example: Bar chart of product categories
category_counts = df["Product Category"].value_counts()
category_counts.plot(kind="bar", figsize=(8, 6))
plt.title("Product Categories")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()