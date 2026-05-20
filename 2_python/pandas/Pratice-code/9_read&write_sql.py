"""
    1. read_sql - to read data from a SQL database into a DataFrame
    2. to_sql - to write a DataFrame to a SQL database
"""
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine("sqlite:///2_python/pandas/datasets/my_database.db", echo=True)


# Defining the database schema using SQLAlchemy ORM
Base = declarative_base()
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)

    orders = relationship("Order", back_populates="customer")

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Integer)
    customer_id = Column(Integer, ForeignKey("customers.id"))

    customer = relationship("Customer", back_populates="orders")

# Creating the tables in the database
Base.metadata.create_all(engine)

# Inserting sample data into the database
Session = sessionmaker(bind=engine)
session = Session()

# Customers
c1 = Customer(id=1, name="Donald", phone_number="7326784567")
c2 = Customer(id=2, name="Bill", phone_number="6573489999")
c3 = Customer(id=3, name="Modi", phone_number="4567895646")

# Orders
o1 = Order(id=1, name="Yoga Mat", amount=20, customer_id=2)
o2 = Order(id=2, name="Google Pixel", amount=950, customer_id=1)
o3 = Order(id=3, name="Fossil Watch", amount=120, customer_id=3)

session.add_all([c1, c2, c3, o1, o2, o3])
session.commit()

# 1. read_sql
# read_sql_table - to read an entire SQL table into a DataFrame
df = pd.read_sql_table("customers", con=engine)
print('Read SQL Table:\n', df)
"""
Read SQL Table:
    id    name phone_number
0   1  Donald   7326784567
1   2    Bill   6573489999
2   3    Modi   4567895646
"""

# read_sql_table - to read specific columns from a SQL table into a DataFrame
columns = ["id", "name"]
columns_df = pd.read_sql_table("customers", con=engine, columns=columns)
print('Read SQL Table (Filtered):\n', columns_df)
"""
Read SQL Table (Filtered):
    id    name
0   1  Donald
1   2    Bill
2   3    Modi
"""

# read_sql_query - to execute a SQL query and read the result into a DataFrame
query = """
SELECT customers.name AS customer_name, customers.phone_number AS phone_number, orders.name AS order_name, orders.amount
FROM customers
JOIN orders ON customers.id = orders.customer_id
"""
joined_table_df = pd.read_sql_query(query, engine)
print('Read SQL Query:\n', joined_table_df)
"""
Read SQL Query:
   customer_name phone_number    order_name  amount
0          Bill   6573489999      Yoga Mat      20
1        Donald   7326784567  Google Pixel     950
2          Modi   4567895646  Fossil Watch     120
"""

# read_sql - to read data from a SQL database using either a table name or a SQL query
read_sql_df = pd.read_sql('customers', con=engine, index_col='id')
print('Read SQL:\n', read_sql_df)

# 2. to_sql
# to_sql - to write a DataFrame to a SQL database (table will be created if it doesn't exist)
read_df = pd.read_csv("2_python/pandas/datasets/customers.csv")
# Renaming columns to match the database schema
read_df.rename(columns={
    "Customer Name": "name",
    "Customer Phone Number": "phone_number"
}, inplace=True)
# Writing the csv file data to the SQL database (appending to the existing table)
read_df.to_sql("customers", con=engine, if_exists="append", index=False)

# to_sql - to write a DataFrame to a SQL database (appending to an existing table)
new_df = pd.DataFrame({
    "name": ["Alice", "Bob"],
    "phone_number": ["1234567890", "0987654321"]
})
new_df.to_sql("customers", con=engine, if_exists="append", index=False)