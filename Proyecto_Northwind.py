# First Data Analysis Project – The goal of this project is to practice combining tools for data analysis using Python and SQLite.
# The database used for this project is Northwind, which contains real-world product sales and purchase data.


# Importing libraries
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connecting to the database file
conn = sqlite3.connect("c:\\SQlite_aprendizaje\\ejercicios DALTO\\northwind.db")

# ----------------------------------------------------------------------------------------------------------------
# Cursor to allow executing SQLite commands within Python
# 1) Which customers placed the most orders? 
cursor = conn.cursor()
ejecucion = cursor.execute('''
SELECT CustomerName,count(*) as total_vendido FROM Customers c
JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY CustomerName
ORDER BY total_vendido DESC
LIMIT 5
''')

# Store the query in a variable
results = cursor.fetchall()
# Save the results in a DataFrame and assign column names
results_df = pd.DataFrame(results,columns=["CustomerName", "total_vendido"])
# Print the results to verify before generating the bar chart
print(results_df)

# Set the values for the X and Y axes in the chart
results_df.plot(x="CustomerName",y="total_vendido",kind="bar",figsize=(10,5),legend=False)

# Use matplotlib for data visualization
plt.title("Top 5 customers by number of orders.")
plt.xlabel("Customers")
plt.ylabel("Orders")
plt.xticks(rotation = 45)
plt.show()




# ----------------------------------------------------------------------------------------------------------------
# 1.2) Which customers generated the most revenue?

ejecucion1_2 = cursor.execute('''
SELECT c.CustomerName, SUM(p.price * od.Quantity) as total_revenue
FROM Customers c
JOIN Orders o ON c.CustomerID=o.CustomerID
JOIN OrderDetails od ON o.OrderID=od.OrderID
JOIN Products p ON od.ProductID=p.ProductID
GROUP BY CustomerName
ORDER BY total_revenue DESC
LIMIT 5
''')

results1_2 = cursor.fetchall()

results_df1_2 = pd.DataFrame(results1_2,columns=["CustomerName", "total_revenue"])

print(results_df1_2)

results_df1_2.plot(x="CustomerName",y="total_revenue",kind="bar",figsize=(10,5),legend=False)

plt.title("Top 5 customers by total revenue generated.")
plt.xlabel("Customers")
plt.ylabel("Total Revenue")
plt.xticks(rotation = 45)
plt.show()



# ----------------------------------------------------------------------------------------------------------------
# 2) What are the best-selling products?

ejecucion2 = cursor.execute('''
SELECT ProductName,SUM(Price*Quantity) as cantidad FROM Products as p
JOIN OrderDetails as od 
ON p.ProductID=od.ProductID
GROUP BY ProductName
ORDER BY cantidad DESC
LIMIT 5
''')

results2 = cursor.fetchall()

results_df2 = pd.DataFrame(results2,columns=["ProductName", "cantidad_total"])

print(results_df2)

results_df2.plot(x="ProductName",y="cantidad_total",kind="bar",figsize=(10,5),legend=False)

plt.title("Top 5 best-selling products by total dollar amount.")
plt.xlabel("Products")
plt.ylabel("Total sold")
plt.xticks(rotation = 45)
plt.show()


# ----------------------------------------------------------------------------------------------------------------
# 3) Which employees generated the most revenue?

ejecucion3 = cursor.execute('''
SELECT 
	e.FirstName||' '||e.LastName as EmployeeName,
    SUM(od.Quantity*p.Price) as total_revenue 
FROM Employees e
JOIN Orders o ON e.EmployeeID=o.EmployeeID
JOIN OrderDetails od ON o.OrderID=od.OrderID
JOIN Products p ON od.ProductID=p.ProductID
GROUP BY e.EmployeeID
ORDER BY total_revenue DESC
LIMIT 4
''')

results3 = cursor.fetchall()

results_df3 = pd.DataFrame(results3,columns=["EmployeeName", "total_revenue"])

print(results_df3)

results_df3.plot(x="EmployeeName",y="total_revenue",kind="bar",figsize=(10,5),legend=False)

plt.title("Top 4 employees by total revenue generated.")
plt.xlabel("Employee")
plt.ylabel("Total revenue")
plt.xticks(rotation = 45)
plt.show()



# ----------------------------------------------------------------------------------------------------------------
# 4) Which employees generated the least revenue?

ejecucion4 = cursor.execute('''
SELECT 
	e.FirstName||' '||e.LastName as EmployeeName,
    SUM(od.Quantity*p.Price) as total_revenue 
FROM Employees e
JOIN Orders o ON e.EmployeeID=o.EmployeeID
JOIN OrderDetails od ON o.OrderID=od.OrderID
JOIN Products p ON od.ProductID=p.ProductID
GROUP BY e.EmployeeID
ORDER BY total_revenue 
LIMIT 3
''')

results4 = cursor.fetchall()

results_df4 = pd.DataFrame(results4,columns=["EmployeeName", "total_revenue"])

print(results_df4)

results_df4.plot(x="EmployeeName",y="total_revenue",kind="bar",figsize=(10,5),legend=False)

plt.title("Top 4 employees with the lowest revenue generated.")
plt.xlabel("Employee")
plt.ylabel("Total revenue")
plt.xticks(rotation = 45)
plt.show()


# ----------------------------------------------------------------------------------------------------------------
# 5) Which countries generate the most revenue? 

ejecucion5 = cursor.execute('''
SELECT c.Country, SUM(od.Quantity * p.Price) as total_revenue
FROM Customers c
JOIN Orders o ON c.CustomerID=o.CustomerID
JOIN OrderDetails od ON o.OrderID=od.OrderID
JOIN Products p ON od.ProductID=p.ProductID
GROUP BY Country
ORDER BY total_revenue DESC
''')

results5 = cursor.fetchall()
results5_df = pd.DataFrame(results5,columns=["country","Quantity_revenue"])
print(results5_df)

results5_df.plot(x="country",y="Quantity_revenue",kind="bar",figsize=(10,5),legend=False)

plt.title("List of all countries and total revenue.")
plt.xlabel("Countries")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()



# ----------------------------------------------------------------------------------------------------------------
# 6) How have sales changed month by month or year by year?

ejecucion6 = cursor.execute('''
SELECT strftime('%Y-%m', o.OrderDate) AS Mes, 
    SUM(p.Price*od.Quantity) as total_revenue
FROM Orders o
JOIN OrderDetails od ON o.OrderID=od.OrderID
JOIN Products p ON od.ProductID=p.ProductID
GROUP BY Mes
ORDER BY Mes ASC
''')

results6= cursor.fetchall()
results_df6 = pd.DataFrame(results6,columns=["Date","Quantity_Revenue"])
print(results_df6)

results_df6.plot(x="Date",y="Quantity_Revenue",kind="line",figsize=(10,5),legend=False)

plt.title("How have sales changed month by month or year over year?")
plt.xlabel("Date")
plt.ylabel("Quantity Revenue")
plt.xticks(rotation=45)
plt.show()



























