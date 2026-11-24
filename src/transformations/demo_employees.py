from pyspark import pipelines as dp

@dp.table(
    name="demo_employees",
    comment="Demo employee table created using DAB"
)
def demo_employees():

    data = [
        (1, "Arun", "IT", 60000),
        (2, "Priya", "HR", 50000),
        (3, "Kumar", "Finance", 70000),
        (4, "Divya", "IT", 65000)
    ]

    columns = ["emp_id", "name", "department", "salary"]

    return spark.createDataFrame(data, columns)