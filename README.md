# 🍬 Candy Sales Analysis Project

This project explores and analyzes a dataset of candy sales using Python for data preprocessing, statistical analysis, and insightful visualizations. It is aimed at uncovering trends, patterns, and performance metrics across various dimensions like time, region, and product divisions.

---

## 📁 Dataset

- **Source**: [Maven Analytics Data Playground](https://mavenanalytics.io/data-playground)
- **File**: `Candy_Sales.csv`

---

## 🔧 Technologies Used

- **Python** 
- **Data Visualization**: Matplotlib, Seaborn
- **Numpy**: For Numerical Values
- **Pandas**: For Data Handling

---

## ✅ Project Objectives

### 🧹 Objective 0: Data Preprocessing and Cleaning

- Convert date columns (`Order Date`, `Ship Date`) to datetime objects.
- Handle missing values:
  - Replace missing `Postal Code` with `"Unknown"`.
  - Replace missing `Sales` with the **mean** of the column.
- Remove duplicates.
- Print dataset info and preview the data.

---

### 📊 Objective 1: Revenue Statistics

- **Total Revenue**: Sum of all sales.
- **Average Revenue per Order**: Mean of the `Sales` column.
- **Standard Deviation** of Sales.

---

### 📦 Objective 2: Orders and Performance by State

- Total number of orders.
- Total units sold.
- State/Province with the highest total sales.

---

### 📈 Objective 3: Sales Performance & Profitability Visualizations

- **Line Plot**: Sales trends over time.
- **Grouped Bar Chart**: Sales and Gross Profit by Country/Region and Division.
- **Histogram**: Distribution of Sales and Cost.
- **Correlation Heatmap**: Sales, Cost, and Gross Profit relationships.

---

### 🚨 Objective 4: Outlier Detection

- Detect outliers in:
  - `Sales`
  - `Gross Profit`
- Use Interquartile Range (IQR) method.
- Visualize with Box Plots.

---

### 📊 Objective 5: Graphical Analysis

- **Pie Chart**: Sales distribution by region.
- **Heatmap**: Correlation between numerical features.
- **Horizontal Bar Chart**: Sales by region.
- **Donut Chart**: Region-wise sales share.
- **Scatter Plot**: Sales vs. Gross Profit.

---

### 📆 Objective 6: Seasonal Sales Trends

- **Line Chart**: Monthly sales trend over time.
- **Area Chart**: Seasonal pattern in monthly candy sales.

---

## 📌 Insights & Benefits

This analysis helps to:
- Understand which regions and divisions are most profitable.
- Spot seasonal patterns for better planning.
- Detect outliers which may indicate errors or exceptional cases.
- Visualize relationships between key financial metrics.

---

## 📎 Notes

Make sure the dataset `Candy_Sales.csv` is in your working directory, and required libraries are installed before running the script.

---

## 📬 Contact

For questions or feedback, feel free to reach out!

---

**Happy Analyzing! 🍭**
