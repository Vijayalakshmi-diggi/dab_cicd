# Databricks notebook source

# Create sample employee data
data = [
    (1, "Arun", "IT", 60000),
    (2, "Priya", "HR", 50000),
    (3, "Kumar", "Finance", 70000),
    (4, "Divya", "IT", 65000)
]

columns = ["emp_id", "name", "department", "salary"]

# Create Spark DataFrame
df = spark.createDataFrame(data, columns)

# Display data
display(df)

# Print confirmation
print("Demo Job executed successfully!")
print("Total employees:", df.count())