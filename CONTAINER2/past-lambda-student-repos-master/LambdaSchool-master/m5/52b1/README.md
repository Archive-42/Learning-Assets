# java-sql

A student that completes this project shows that they can:

- Query data from a single table
- Query data from multiple tables
- Create a new database using PostgreSQL

## Introduction

Working with SQL

## Instructions

ReImport the Northwind database into PostgreSQL using pgAdmin. This is the same data we used during the guided project.

- [x] **_pgAdmin data refresh_**

- [x] Select the northwind database created during the guided project.

- [x] Tools -> Query Tool

  - [x] Open file northwind.sql (you used this script during the guided project)
  - [x] Execute

- [x] Look under

  - [x] northwind -> Schemas -> public -> tables

- [x] Clear query windows

### Answer the following data queries. Keep track of the SQL you write by pasting it into this document under its appropriate header below in the provided SLQ code block. You will be submitting that through the regular fork, change, pull process.

- [x] **_find all customers that live in London. Returns 6 records_**

```SQL
SELECT * FROM Customers WHERE City='London';
```

- [x] **_find all customers with postal code 1010. Returns 3 customers_**

```SQL
SELECT *
FROM Customers
WHERE PostalCode='1010';
```

- [x] **_find the phone number for the supplier with the id 11. Should be (010) 9984510_**

```SQL
SELECT Phone
FROM Suppliers
WHERE id='11';
```

- [x] **_list orders descending by the order date. The order with date 1998-05-06 should be at the top_**

```SQL
SELECT *
FROM ORDERS
ORDER BY OrderDate DESC;
```

- [x] **_find all suppliers who have names longer than 20 characters. Returns 11 records_**

```SQL
SELECT *
FROM Suppliers
WHERE length(SupplierName) > 20;
```

- [x] **_find all customers that include the word 'MARKET' in the contact title. Should return 19 records_**

```SQL
SELECT *
FROM Customers
WHERE Customers.CustomerName LIKE '%MARKET%';
```

- [x] **_add a customer record for_**

```SQL
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('The Shire', 'Bilbo Baggins', '1 Hobbit-Hole', 'Bag End', '111', 'Middle Earth');
```

- [x] **_update *Bilbo Baggins* record so that the postal code changes to *"11122"*_**

```SQL
UPDATE Customers
SET PostalCode = '11122'
WHERE Customers.ContactName = 'Bilbo Baggins';
```

- [x] **_list orders grouped and ordered by customer company name showing the number of orders per customer company name. *Rattlesnake Canyon Grocery* should have 18 orders_**

  - This can be done with SELECT, COUNT, JOIN and GROUP BY clauses. Your count should focus on a field in the Orders table, not the Customer table
  - There is more information about the COUNT clause on [W3 Schools](https://www.w3schools.com/sql/sql_count_avg_sum.asp)

```SQL
SELECT Customers.CustomerName, Count(Orders.CustomerID)
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID
GROUP BY Customers.CustomerName
ORDER BY Customers.CustomerName;
```

- [x] **_list customers by contact name and the number of orders per contact name. Sort the list by number of orders in descending order. *Jose Pavarotti* should be at the top with 31 orders followed by *Roland Mendal* with 30 orders. Last should be *Francisco Chang* with 1 order_**

  - This can be done by adding an ORDER BY clause to the previous answer and changing the group by field

```SQL
SELECT Customers.CustomerName, Count(Orders.CustomerID)
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID
ORDER BY Count(Orders.CustomerID) DESC;
```

- [ ] **_list orders grouped by customer's city showing number of orders per city. Returns 69 Records with *Aachen* showing 6 orders and *Albuquerque* showing 18 orders_**

  - This is very similar to the previous two queries, however, it focuses on the City rather than the Customer Names

```SQL
SELECT Customers.City, Count(Orders.CustomerID)
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID
GROUP BY Customers.City
ORDER BY Customers.City;
```

## Data Normalization

Note: This step does not use PostgreSQL!

- [x] **_Take the following data and normalize it into a 3NF database_**

| Person Name | Pet Name | Pet Type | Pet Name 2 | Pet Type 2 | Pet Name 3 | Pet Type 3 | Fenced Yard | City Dweller |
| ----------- | -------- | -------- | ---------- | ---------- | ---------- | ---------- | ----------- | ------------ |
| Jane        | Ellie    | Dog      | Tiger      | Cat        | Toby       | Turtle     | No          | Yes          |
| Bob         | Joe      | Horse    |            |            |            |            | No          | No           |
| Sam         | Ginger   | Dog      | Miss Kitty | Cat        | Bubble     | Fish       | Yes         | No           |

Below are some empty tables to be used to normalize the database

- Not all of the cells will contain data in the final solution
- Feel free to edit these tables as necessary

Table Name:

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |

Table Name:

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |

Table Name:

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |

Table Name:

|     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |

---

### Stretch Goals

- [x] **_delete all customers that have no orders. Should delete 2 (or 3 if you haven't deleted the record added) records_**

```SQL
DELETE FROM Customers
LEFT JOIN  Orders ON Customers.CustomerID = Orders.CustomerID
WHERE      Orders.CustomerID IS NULL;
```

- [x] **_Create Database and Table: After creating the database, tables, columns, and constraint, generate the script necessary to recreate the database. This script is what you will submit for review_**

- use pgAdmin to create a database, naming it `budget`.
- add an `accounts` table with the following _schema_:

  - `id`, numeric value with no decimal places that should autoincrement.
  - `name`, string, add whatever is necessary to make searching by name faster.
  - `budget` numeric value.

- constraints
  - the `id` should be the primary key for the table.
  - account `name` should be unique.
  - account `budget` is required.

```SQL

```

To see the script

- Right Click on the database name
  - Select Backup...
    - Set a filename
      - To put the file backup.sql in your home directory, you could use `backup.sql`
    - Set format to `Plain`
- The script you want is now in the text file named above.
  - Copy the script from the text file into the SQL code block above!

![Database Script](assets/jx-12-m3-script.gif)
