# 🚀 Handling Missing Data in PySpark DataFrames

![Databricks](https://img.shields.io/badge/Platform-Databricks%20Free%20Edition-red)
![PySpark](https://img.shields.io/badge/PySpark-3.x-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)

⬅️ [Back to Reading CSV](./02_Reading_CSV.md)

# 📚 Table of Contents

- Overview
- Learning Objectives
- Prerequisites
- Sample Dataset
- Load CSV File
- Display DataFrame
- Find NULL Values
- Count NULL Values
- Drop NULL Values
  - Drop Rows with Any NULL Values
  - Drop Rows with All NULL Values
  - Drop NULL Values from Selected Columns
- Fill NULL Values
  - Fill All NULL Values
  - Fill Selected Columns
- Statistical Imputation
  - Calculate Mean
  - Calculate Median
  - Calculate Mode
  - Fill NULL Values Using Mean, Median, and Mode
- Expected Outputs
- Missing Value Handling Summary
- Real-World Use Cases
- Performance Tips
- Common Mistakes
- PySpark Interview Questions
- Best Practices
- Key Takeaways

---

## 📘 Overview

Missing or null values are common in real-world datasets. PySpark provides several built-in functions to identify, count, remove, and replace null values efficiently across distributed datasets.

This guide demonstrates how to work with missing values using the PySpark DataFrame API.

---

# 🎯 Learning Objectives

After completing this guide, you will be able to:

* Read CSV files into a Spark DataFrame
* Detect null values
* Count missing values in columns
* Drop rows containing null values
* Replace null values with fixed values
* Fill missing values using statistical measures
* Calculate Mean, Median, and Mode in PySpark

---

# 🏗 Workflow

```text
Read CSV
     │
     ▼
Detect Null Values
     │
     ▼
Count Missing Values
     │
     ▼
Drop Null Rows
     │
     ▼
Fill with Constant Values
     │
     ▼
Calculate Mean / Median / Mode
     │
     ▼
Fill Missing Values
     │
     ▼
Clean Dataset Ready
```

---

# 📂 Dataset

```
/Volumes/workspace/default/raw_data/weather_data.csv
```

Example Columns

| Column      | Description   |
| ----------- | ------------- |
| day         | Date          |
| temperature | Temperature   |
| windspeed   | Wind Speed    |
| event       | Weather Event |

---

# 📥 Read CSV File

```python
df = spark.read.csv(
    "/Volumes/workspace/default/raw_data/weather_data.csv",
    header=True,
    inferSchema=True
)

display(df)
```

Sample Output

| day       | temperature | windspeed | event  |
| --------- | ----------- | --------- | ------ |
| 1/1/2017  | 32.0        | 6.0       | Rain   |
| 1/4/2017  | NULL        | 9.0       | Sunny  |
| 1/5/2017  | 28.0        | NULL      | Snow   |
| 1/6/2017  | NULL        | 7.0       | NULL   |
| 1/7/2017  | 32.0        | NULL      | Rain   |
| 1/8/2017  | NULL        | NULL      | Sunny  |
| 1/9/2017  | NULL        | NULL      | NULL   |
| 1/10/2017 | 34.1        | 8.1       | Cloudy |
| 1/11/2017 | 40.0        | 12.0      | Sunny  |

---

# 🔍 Find Rows with Null Values

Using the PySpark Functions API

```python
from pyspark.sql import functions as F

new_df = df.filter(F.col("temperature").isNull())

new_df.show()
```

Sample Output

| day      | temperature | windspeed | event |
| -------- | ----------- | --------- | ----- |
| 1/4/2017 | NULL        | 9.0       | Sunny |
| 1/6/2017 | NULL        | 7.0       | NULL  |
| 1/8/2017 | NULL        | NULL      | Sunny |
| 1/9/2017 | NULL        | NULL      | NULL  |

Using DataFrame Syntax

```python
df.filter(df.temperature.isNull()).count()
```

Sample Output
4

---

# 📊 Count Missing Values

Count null values in a single column.

```python
temp_nulls_sum = df.select(
    F.sum(F.col("temperature").isNull().cast("int"))
    .alias("temperature")
)

temp_nulls_sum.show()
```

Sample Output

| temperature |
| ----------- |
| 4           |

---

# 📊 Count Null Values for Every Column

```python
null_count = df.select(
    [
        F.sum(F.col(c).isNull().cast("int")).alias(c)
        for c in df.columns
    ]
)

null_count.show()
```

Sample Output

| day | temperature | windspeed | event |
| --- | ----------: | --------: | ----: |
| 0   |           3 |         2 |     1 |

---

# 🗑 Drop Rows with Null Values

Remove rows containing at least one null value.

```python
drop_null = df.na.drop(how="any")

drop_null.show()
```

Shortcut

```python
df.na.drop(how="any").show()
```

Sample Output

| day       | temperature | windspeed | event  |
| --------- | ----------- | --------- | ------ |
| 1/1/2017  | 32.0        | 6.0       | Rain   |
| 1/10/2017 | 34.1        | 8.1       | Cloudy |
| 1/11/2017 | 40.0        | 12.0      | Sunny  |

---

# 🗑 Drop Rows Where All Values are Null

```python
df.na.drop(how="all").show()
```

Sample Output

| day       | temperature | windspeed | event  |
| --------- | ----------- | --------- | ------ |
| 1/1/2017  | 32.0        | 6.0       | Rain   |
| 1/4/2017  | NULL        | 9.0       | Sunny  |
| 1/5/2017  | 28.0        | NULL      | Snow   |
| 1/6/2017  | NULL        | 7.0       | NULL   |
| 1/7/2017  | 32.0        | NULL      | Rain   |
| 1/8/2017  | NULL        | NULL      | Sunny  |
| 1/9/2017  | NULL        | NULL      | NULL   |
| 1/10/2017 | 34.1        | 8.1       | Cloudy |
| 1/11/2017 | 40.0        | 12.0      | Sunny  |

---

# 🗑 Drop Rows Based on Specific Columns

Remove rows only if the specified columns contain null values.

```python
df.na.drop(
    how="all",
    subset=["temperature", "windspeed"]
).show()
```

Sample Output

| day       | temperature | windspeed | event  |
| --------- | ----------- | --------- | ------ |
| 1/1/2017  | 32.0        | 6.0       | Rain   |
| 1/4/2017  | NULL        | 9.0       | Sunny  |
| 1/5/2017  | 28.0        | NULL      | Snow   |
| 1/6/2017  | NULL        | 7.0       | NULL   |
| 1/7/2017  | 32.0        | NULL      | Rain   |
| 1/10/2017 | 34.1        | 8.1       | Cloudy |
| 1/11/2017 | 40.0        | 12.0      | Sunny  |

---

# 🔄 Fill Missing Values with a Constant

Replace every null value with  **0** .

```python
df.fillna(0).show()
```

Sample Output

| day       | temperature | windspeed | event  |
| --------- | ----------- | --------- | ------ |
| 1/1/2017  | 32.0        | 6.0       | Rain   |
| 1/4/2017  | 0.0         | 9.0       | Sunny  |
| 1/5/2017  | 28.0        | 0.0       | Snow   |
| 1/6/2017  | 0.0         | 7.0       | NULL   |
| 1/7/2017  | 32.0        | 0.0       | Rain   |
| 1/8/2017  | 0.0         | 0.0       | Sunny  |
| 1/9/2017  | 0.0         | 0.0       | NULL   |
| 1/10/2017 | 34.1        | 8.1       | Cloudy |
| 1/11/2017 | 40.0        | 12.0      | Sunny  |

---

# 🔄 Fill Individual Columns

```python
df.fillna(
    {
        "temperature": 0,
        "windspeed": 10
    }
).show()
```

Sample Output

| day       | temperature | windspeed | event  |
| --------- | ----------- | --------- | ------ |
| 1/1/2017  | 32.0        | 6.0       | Rain   |
| 1/4/2017  | 0.0         | 9.0       | Sunny  |
| 1/5/2017  | 28.0        | 10.0      | Snow   |
| 1/6/2017  | 0.0         | 7.0       | NULL   |
| 1/7/2017  | 32.0        | 10.0      | Rain   |
| 1/8/2017  | 0.0         | 10.0      | Sunny  |
| 1/9/2017  | 0.0         | 10.0      | NULL   |
| 1/10/2017 | 34.1        | 8.1       | Cloudy |
| 1/11/2017 | 40.0        | 12.0      | Sunny  |

---

# 📈 Calculate Mean

Using **Average**

```python
avg_temp = df.select(
    F.avg(F.col("temperature"))
).collect()[0][0]

print(avg_temp)
```

Using **Mean**

```python
avg_temp_1 = df.select(
    F.mean(F.col("temperature"))
    .alias("avg_temp")
)
```

Sample Output

33.22

```python
avg_temp_1.show()
```

Sample Output

| avg_temp |
| -------- |
| 33.22    |

Using Aggregation

```python
avg_temp_3 = df.agg(
    F.mean("temperature")
).first()[0]
```

Sample Output

33.22

---

# 📊 Calculate Mean, Median and Mode

```python
# Average temperature
temp_mean = df.select(
    F.mean("temperature")
).first()[0] 

# Meddle Value
wind_median = df.select(
    F.median("windspeed")
).first()[0] 

# Most Common Value
event_mode = df.select(
    F.mode("event")
).first()[0]
```

Result

```python
(temp_mean, wind_median, event_mode)
```

Sample Output

(33.22, 8.1, 'Sunny')

---

# ✅ Fill Missing Values Using Statistics

Replace missing values using statistical measures.

```python
df.na.fill(
    {
        "temperature": temp_mean,
        "windspeed": wind_median,
        "event": event_mode
    }
).show()
```

Sample Output

| day       | temperature | windspeed | event  |
| --------- | ----------: | --------: | ------ |
| 1/1/2017  |          32 |         6 | Rain   |
| 1/4/2017  |       33.22 |         9 | Sunny  |
| 1/5/2017  |          28 |       8.1 | Snow   |
| 1/6/2017  |       33.22 |         7 | Sunny  |
| 1/7/2017  |          32 |       8.1 | Rain   |
| 1/8/2017  |       33.22 |       8.1 | Sunny  |
| 1/9/2017  |       33.22 |       8.1 | Sunny  |
| 1/10/2017 |        34.1 |       8.1 | Cloudy |
| 1/11/2017 |          40 |        12 | Sunny  |

---

# 📊 Missing Value Handling Summary

| Technique     | Description                  | Best Use Case         |
| ------------- | ---------------------------- | --------------------- |
| `isNull()`  | Detect missing values        | Data validation       |
| `count()`   | Count null rows              | Data quality checks   |
| `na.drop()` | Remove rows with nulls       | Cleaning datasets     |
| `fillna()`  | Replace nulls with constants | Default values        |
| Mean          | Average value                | Numerical columns     |
| Median        | Middle value                 | Skewed numerical data |
| Mode          | Most frequent value          | Categorical columns   |

---

# 🎤 Interview Questions

## 1. What is a null value in PySpark?

A null value represents missing or unknown data in a DataFrame.

---

## 2. How do you check whether a column contains null values?

```python
df.filter(df.temperature.isNull())
```

---

## 3. How do you count null values in a column?

```python
F.sum(F.col("temperature").isNull().cast("int"))
```

---

## 4. What is the difference between `isNull()` and `isNotNull()`?

| isNull()                        | isNotNull()                         |
| ------------------------------- | ----------------------------------- |
| Returns rows having null values | Returns rows having non-null values |

---

## 5. How do you remove rows containing null values?

```python
df.na.drop()
```

---

## 6. Difference between `how="any"` and `how="all"`?

| any                             | all                                             |
| ------------------------------- | ----------------------------------------------- |
| Drops row if any column is null | Drops row only if every selected column is null |

---

## 7. How do you replace null values?

```python
df.na.fill(0)
```

---

## 8. How do you replace null values for specific columns?

```python
df.na.fill({
    "temperature":0,
    "windspeed":10
})
```

---

## 9. Which statistical values are commonly used for imputation?

* Mean
* Median
* Mode

---

## 10. When should you use Mean instead of Median?

**Mean**

* Normally distributed numerical data.

**Median**

* Skewed data or data containing outliers.

---

## 11. Why is Mode used for categorical columns?

Because categorical values cannot be averaged. Mode returns the most frequently occurring value.

---

## 12. What is the difference between `fillna()` and `na.drop()`?

| fillna()                | na.drop()                        |
| ----------------------- | -------------------------------- |
| Replaces missing values | Removes rows with missing values |

---

## 13. Which approach is better: dropping or filling null values?

It depends on the business requirement.

* Few missing rows → `drop()`
* Important dataset → `fillna()`
* ML preprocessing → Statistical imputation (Mean/Median/Mode)

---

## 14. How do you calculate Mean in PySpark?

```python
F.mean("temperature")
```

---

## 15. How do you calculate Median in PySpark?

```python
F.median("windspeed")
```

---

## 16. How do you calculate Mode in PySpark?

```python
F.mode("event")
```

---

## 17. Why should missing values be handled before Machine Learning?

Because many ML algorithms cannot process null values, leading to errors or inaccurate predictions.

---

# 💡 Best Practices

* Always inspect missing values before cleaning.
* Use **Me04_an** for normally distributed numerical data.
* Use **Median** for skewed numerical data.
* Use **Mode** for categorical columns.
* Avoid dropping rows unless necessary, as it may result in data loss.
* Validate the cleaned DataFrame before performing transformations or machine learning tasks.

---

# 🎯 Key Takeaways

* Loaded CSV data into a Spark DataFrame.
* Detected and counted missing values.
* Removed rows containing null values.
* Filled null values using constants.
* Calculated Mean, Median, and Mode.
* Replaced missing values using statistical techniques.
* Prepared a clean dataset for downstream analytics and ETL pipelines.

---

# 🚀 Next Steps

➡️ [SQL In Spark](04_SQL_in_Spark.md)