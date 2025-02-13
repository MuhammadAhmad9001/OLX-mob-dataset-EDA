
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("C:/Users/Al Rehman Computers/Desktop/olxproject/_OLX_mob_dataset.csv")

# Remove duplicates
data = data.drop_duplicates()

# Standardize column names (lowercase, strip spaces)
data.columns = data.columns.str.strip().str.lower()
print("Columns in dataset:", data.columns)

# 📌 1️⃣ Basic Summary of Data
print("\n🔹 First 5 rows of the dataset:")
print(data.head())

print("\n🔹 Data Info:")
print(data.info())

print("\n🔹 Missing Values in Each Column:")
print(data.isnull().sum())

print("\n🔹 Summary Statistics:")
print(data.describe())

# 📌 2️⃣ Count of Unique Brands
print("\n🔹 Unique Brands Count:", data['brand'].nunique())

print("\n🔹 Top 10 Brands by Total Listings:")
print(data['brand'].value_counts().head(10))

# 📌 3️⃣ Distribution of Total Phones per Brand
plt.figure(figsize=(12, 5))
sns.barplot(x=data['brand'].value_counts().index[:10], y=data['brand'].value_counts().values[:10])
plt.xticks(rotation=45)
plt.title("Top 10 Brands by Total Listings")
plt.xlabel("Brand")
plt.ylabel("Number of Listings")
plt.show()

# 📌 4️⃣ Distribution of Conditions (New, Used, For Parts)
plt.figure(figsize=(8, 5))
condition_cols = ['used', 'new', 'open-box', 'for parts', 'refurbished']
condition_sums = data[condition_cols].sum()
sns.barplot(x=condition_sums.index, y=condition_sums.values, palette="coolwarm")
plt.title("Distribution of Phone Conditions")
plt.xlabel("Condition")
plt.ylabel("Count")
plt.show()

# 📌 5️⃣ Correlation Between Numeric Columns
plt.figure(figsize=(8, 6))
sns.heatmap(data[condition_cols].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Between Different Conditions of Phones")
plt.show()

# 📌 6️⃣ Outlier Detection using Box Plot
plt.figure(figsize=(10, 5))
sns.boxplot(data=data[['used', 'new', 'open-box', 'for parts', 'refurbished']])
plt.title("Outlier Detection in Phone Conditions")
plt.show()


