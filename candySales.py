# ================================ Data Preprocessing & Cleaning ===================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
sales_data = pd.read_csv("C:/CA2 Python Project\\Candy_Sales.csv")

# 1. Convert date columns to datetime
sales_data["Order Date"] = pd.to_datetime(sales_data["Order Date"])
sales_data["Ship Date"] = pd.to_datetime(sales_data["Ship Date"])

# 2. Check for missing values
print(sales_data.isnull().sum())

# 3. Handle Missing Values
sales_data.fillna({"Postal Code": "Unknown", "Sales": sales_data["Sales"].mean()}, inplace=True)

# 4. Remove Duplicates
sales_data.drop_duplicates(inplace=True)

# 5. Dataset Summary
print(sales_data.info())
print(sales_data.head())

# ================================ Exploratory Data Analysis (EDA) ================================

# 1. Summary Statistics
print("Summary stats-")
print(sales_data.describe())

# 2. Correlation & Covariance
print("Correlation Matrix")
print(sales_data[["Sales", "Units", "Gross Profit", "Cost"]].corr())

print("Covariance Matrix")
print(sales_data[["Sales", "Units", "Gross Profit", "Cost"]].cov())


# ================================ Objective 1: Revenue Stats ======================================

# Load dataset
sales_data = pd.read_csv("Candy_Sales.csv")
sales = np.array(sales_data["Sales"])

# Calculate total, average revenue and std deviation
total_revenue = np.sum(sales)
average_revenue = np.mean(sales)
std_dev_sales = np.std(sales)

print("Total Revenue:", total_revenue)
print("Average Revenue per Order:", average_revenue)
print("Standard Deviation of Sales:", std_dev_sales)

# ================================ Objective 2: Orders & State Performance ==========================

# Load dataset
sales_data = pd.read_csv("Candy_Sales.csv")

# Total orders, units, and top state
total_orders = sales_data.shape[0]
total_units = sales_data["Units"].sum()
state_highest_sale = sales_data.groupby("State/Province")["Sales"].sum().idxmax()

print("Total number of Orders:", total_orders)
print("Total Units sold:", total_units)
print("State with the highest Sales:", state_highest_sale)


# ================================ Objective 3: Sales & Profit Visuals ==============================

# 1. Sales Trends Over Time
plt.figure(figsize=(10, 6))
sns.lineplot(data=sales_data, x="Order Date", y="Sales")
plt.title("Sales Trends Over Time")
plt.xlabel("Order Date")
plt.ylabel("Total Sales")
plt.show()

# 2. Sales & Gross Profit Across Regions and Divisions
plt.figure(figsize=(10, 6))
region = sales_data.groupby(["Country/Region", "Division"])[["Sales", "Gross Profit"]].sum().reset_index()
melted_data = region.melt(id_vars=["Country/Region", "Division"], value_vars=["Sales", "Gross Profit"], var_name="Metric", value_name="Amount")
sns.barplot(data=melted_data, x="Country/Region", y="Amount", hue="Division", errorbar=None)
print(melted_data.head(10))
plt.title("Sales and Gross Profit by Regions and Divisions")
plt.xlabel("Region")
plt.ylabel("Total Amount")
plt.legend(title="Metric")
plt.grid(axis="y", linestyle="--")
plt.show()

# 3. Distribution of Sales and Costs
plt.figure(figsize=(8, 5))
sns.histplot(sales_data["Sales"], bins=30, color="b", label="Sales")
sns.histplot(sales_data["Cost"], bins=30, color="r", label="Cost")
plt.title("Distribution of Sales and Costs")
plt.xlabel("Metric")
plt.ylabel("Amount")
plt.legend()
plt.show()

# 4. Correlation Heatmap: Sales, Cost, Profit
data = sales_data[["Sales", "Cost", "Gross Profit"]]
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, fmt=".2f", linewidths=0.5, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ================================ Objective 4: Outlier Detection ==================================

# Outlier Detection Function
def detect_outliers(data, col):
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[col] < lower_bound) | (data[col] > upper_bound)]
    return outliers

# Detect outliers
sales_outlier = detect_outliers(sales_data, "Sales")
gross_profit_outlier = detect_outliers(sales_data, "Gross Profit")

print("Outliers in Sales:", sales_outlier)
print("Outliers in Gross Profit:", gross_profit_outlier)

# Box Plot of Sales and Gross Profit
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.boxplot(sales_data["Sales"], color="skyblue")
plt.title("Box Plot of Sales")

plt.subplot(1, 2, 2)
sns.boxplot(sales_data["Gross Profit"], color="lightcoral")
plt.title("Box Plot of Gross Profit")

plt.tight_layout()
plt.show()

# ================================ Objective 5: Graphical Analysis =================================

# 1. Pie Chart: Sales Distribution by Region
geo_col = 'Region'
sales_col = 'Sales'
region_sales = sales_data.groupby(geo_col)[sales_col].sum()

plt.figure(figsize=(8, 8))
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Set3.colors)
plt.title('Pie Chart: Sales Distribution by Region')
plt.axis('equal')
plt.tight_layout()
plt.show()

# 2. Correlation Heatmap
plt.figure(figsize=(8, 6))
correlation = sales_data.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Heatmap: Correlation Heatmap")
plt.show()

# 3. Horizontal Bar Plot: Sales by Region
plt.figure(figsize=(8, 10))
region_sales.sort_values().plot(kind='barh', color='teal')
plt.title('Horizontal Bar Plot: Sales by Region')
plt.xlabel('Total Sales')
plt.ylabel('Region')
plt.tight_layout()
plt.show()

# 4. Donut Chart: Sales Distribution by Region
geo_col = 'Region'
sales_col = 'Sales'
region_sales = sales_data.groupby(geo_col)[sales_col].sum()

plt.figure(figsize=(8, 8))
colors = plt.cm.Pastel1.colors
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops=dict(width=0.4))
plt.title("Donut Chart: Sales Distribution by Region")
plt.tight_layout()
plt.show()

# 5. Scatter Plot: Sales vs. Gross Profit
plt.figure(figsize=(10, 6))
plt.scatter(sales_data['Sales'], sales_data['Gross Profit'], alpha=0.6, color='pink', edgecolors='k')
plt.title('Scatter Chart: Sales vs. Gross Profit')
plt.xlabel('Sales ($)')
plt.ylabel('Gross Profit ($)')
plt.grid(True)
plt.tight_layout()
plt.show()


# ================================ Objective 6: Seasonal Sales Trends ==============================

# 1. Line Plot: Monthly Candy Sales Trend
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])
sales_data['YearMonth'] = sales_data['Order Date'].dt.to_period('M')
monthly_sales = sales_data.groupby('YearMonth')['Sales'].sum().reset_index()
monthly_sales['YearMonth'] = monthly_sales['YearMonth'].astype(str)

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['YearMonth'], monthly_sales['Sales'], marker='o', linestyle='-', color='green')
plt.title('Monthly Candy Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Seasonal Area Chart
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])
sales_data['Month'] = sales_data['Order Date'].dt.to_period('M').astype(str)
monthly_sales = sales_data.groupby('Month')['Sales'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.fill_between(monthly_sales['Month'], monthly_sales['Sales'], color='yellow', alpha=0.6)
plt.plot(monthly_sales['Month'], monthly_sales['Sales'], color='red', marker='o')
plt.xticks(rotation=45)
plt.title('Seasonal Candy Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()


