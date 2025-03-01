# SQL Cheat Sheet

## 1. Introduction to SQL

**Definition**:  
SQL (**Structured Query Language**) is a standardized language for managing relational databases. You can **create** and **modify** tables (DDL), **retrieve** and **manipulate** data (DML), and **control** access and concurrency (DCL, TCL).

**Example**:  
A typical relational database might have tables such as `employees`, `departments`, and `projects`. Each table has columns, like `employee_id`, `first_name`, `last_name`, etc. Using SQL statements, you can query and manage these tables.

---

## 2. Setting the Stage: Sample Tables

Here’s a minimal scenario with two tables: **`employees`** and **`departments`**.

### 2.1. `departments` Table

| department_id | department_name |
|---------------|-----------------|
| 1             | IT             |
| 2             | HR             |
| 3             | Finance        |

### 2.2. `employees` Table

| employee_id | first_name | last_name | department_id | salary   |
|-------------|------------|-----------|---------------|----------|
| 1001        | Alice      | Smith     | 1             | 75000.00 |
| 1002        | Bob        | Johnson   | 2             | 50000.00 |
| 1003        | Carol      | White     | 2             | 52000.00 |
| 1004        | Dave       | Green     | 3             | 96000.00 |

We’ll refer to these tables in the examples and show you the expected outputs after running SQL commands against them.

---

## 3. SQL Data Definition Language (DDL)

**Definition**:  
DDL statements define and manage the structure of the database. Common commands include `CREATE`, `ALTER`, and `DROP`.

### 3.1. Creating a Database

```sql
CREATE DATABASE my_database;
```
> This creates a new database named `my_database`.  
> (Some SQL environments might require you to run `USE my_database;` or similar to select it.)

### 3.2. Creating the Sample Tables

```sql
CREATE TABLE departments (
    department_id   INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    employee_id   INT PRIMARY KEY,
    first_name    VARCHAR(50),
    last_name     VARCHAR(50),
    department_id INT,
    salary        DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
```
> **Explanation**:  
> - `PRIMARY KEY` ensures each row in the table can be uniquely identified by that column.  
> - `FOREIGN KEY` enforces referential integrity between `employees` and `departments`.

**Inserting sample data** (to replicate our example scenario):

```sql
INSERT INTO departments (department_id, department_name)
VALUES 
(1, 'IT'),
(2, 'HR'),
(3, 'Finance');

INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
VALUES
(1001, 'Alice', 'Smith',   1, 75000.00),
(1002, 'Bob',   'Johnson', 2, 50000.00),
(1003, 'Carol', 'White',   2, 52000.00),
(1004, 'Dave',  'Green',   3, 96000.00);
```
> **Output** (if your environment shows success messages):
> ```
> Query OK, 3 rows affected
> Query OK, 4 rows affected
> ```

---

## 4. SQL Data Manipulation Language (DML)

**Definition**:  
DML statements manipulate the data itself. Examples: `INSERT`, `UPDATE`, `DELETE`.

### 4.1. Inserting Data

```sql
INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
VALUES (1005, 'Eve', 'Davis', 1, 63000.00);
```
> **Output**:
> ```
> Query OK, 1 row affected
> ```

### 4.2. Updating Data

```sql
UPDATE employees
SET salary = 80000.00
WHERE employee_id = 1003;
```
> **Explanation**:  
> This raises Carol’s salary to 80,000.00.  

**Result** (looking at the `employees` table afterward):

| employee_id | first_name | last_name | department_id | salary   |
|-------------|------------|-----------|---------------|----------|
| 1001        | Alice      | Smith     | 1             | 75000.00 |
| 1002        | Bob        | Johnson   | 2             | 50000.00 |
| **1003**    | Carol      | White     | 2             | **80000.00** |
| 1004        | Dave       | Green     | 3             | 96000.00 |
| 1005        | Eve        | Davis     | 1             | 63000.00 |

### 4.3. Deleting Data

```sql
DELETE FROM employees
WHERE employee_id = 1002;
```
> **Explanation**: Removes Bob from the `employees` table.  
> **Output**:
> ```
> Query OK, 1 row affected
> ```

**`employees`** table after deletion:

| employee_id | first_name | last_name | department_id | salary   |
|-------------|------------|-----------|---------------|----------|
| 1001        | Alice      | Smith     | 1             | 75000.00 |
| 1003        | Carol      | White     | 2             | 80000.00 |
| 1004        | Dave       | Green     | 3             | 96000.00 |
| 1005        | Eve        | Davis     | 1             | 63000.00 |

---

## 5. Querying Data

### 5.1. Basic SELECT

**Definition**:  
`SELECT` retrieves data from the database. You can choose specific columns or use `*` for all columns.

```sql
SELECT * 
FROM employees;
```
> **Example output** (based on current data):

| employee_id | first_name | last_name | department_id | salary   |
|-------------|------------|-----------|---------------|----------|
| 1001        | Alice      | Smith     | 1             | 75000.00 |
| 1003        | Carol      | White     | 2             | 80000.00 |
| 1004        | Dave       | Green     | 3             | 96000.00 |
| 1005        | Eve        | Davis     | 1             | 63000.00 |

### 5.2. DISTINCT

**Definition**:  
`DISTINCT` returns only unique values from the specified column(s).

```sql
SELECT DISTINCT department_id
FROM employees;
```
> **Output** might be:
> ```
> department_id
> 1
> 2
> 3
> ```

### 5.3. WHERE

**Definition**:  
Used to filter rows based on a specified condition.

```sql
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 70000;
```
> **Output**:
>
>| first_name | last_name | salary   |
>|------------|-----------|----------|
>| Alice      | Smith     | 75000.00 |
>| Carol      | White     | 80000.00 |
>| Dave       | Green     | 96000.00 |

### 5.4. LIMIT / FETCH

**Definition**:  
Restricts the number of rows returned.

```sql
SELECT * 
FROM employees
LIMIT 2;
```
> **Example output** (the first 2 rows that the database finds; depends on the default order):
>
>| employee_id | first_name | last_name | department_id | salary   |
>|-------------|------------|-----------|---------------|----------|
>| 1001        | Alice      | Smith     | 1             | 75000.00 |
>| 1003        | Carol      | White     | 2             | 80000.00 |

*(In some RDBMS, you use `FETCH FIRST 2 ROWS ONLY`.)*

---

## 6. Filtering Data

### 6.1. LIKE

**Definition**:  
Matches text with a pattern (often `%` wildcard).

```sql
SELECT first_name, last_name
FROM employees
WHERE first_name LIKE 'A%';
```
> **Output** (employees whose first_name starts with 'A'):
>
>| first_name | last_name |
>|------------|-----------|
>| Alice      | Smith     |

### 6.2. IN

**Definition**:  
Checks if a column matches any value in a list.

```sql
SELECT first_name, department_id
FROM employees
WHERE department_id IN (1, 3);
```
> **Output** (employees in departments 1 or 3):
>
>| first_name | department_id |
>|------------|---------------|
>| Alice      | 1             |
>| Dave       | 3             |
>| Eve        | 1             |

### 6.3. BETWEEN

**Definition**:  
Checks if a value is within a specified range (inclusive).

```sql
SELECT first_name, salary
FROM employees
WHERE salary BETWEEN 60000 AND 80000;
```
> **Output**:
>
>| first_name | salary   |
>|------------|----------|
>| Alice      | 75000.00 |
>| Eve        | 63000.00 |

### 6.4. IS NULL

**Definition**:  
Checks if a column is `NULL`.

```sql
SELECT first_name, last_name
FROM employees
WHERE department_id IS NULL;
```
> **Output**:  
> (Based on our sample data, likely no rows, unless a department_id is missing.)

---

## 7. SQL Operators (AND, OR, NOT, ORDER BY, GROUP BY)

### 7.1. AND / OR / NOT

**Definition**:  
- `AND`: Both conditions must be true.  
- `OR`: At least one condition is true.  
- `NOT`: Negates a condition.

```sql
SELECT first_name, salary
FROM employees
WHERE department_id = 1 AND salary > 70000;
```
> **Output**: Potentially no rows in our example, because Alice = 75000 (matches), Eve = 63000 (does not). Actually, wait, yes, it would show:
>
>| first_name | salary   |
>|------------|----------|
>| Alice      | 75000.00 |

### 7.2. ORDER BY

**Definition**:  
Sorts the result set in ascending (`ASC`) or descending (`DESC`) order.

```sql
SELECT employee_id, salary
FROM employees
ORDER BY salary DESC;
```
> **Output** (descending salary):
>
>| employee_id | salary   |
>|-------------|----------|
>| 1004        | 96000.00 |
>| 1003        | 80000.00 |
>| 1001        | 75000.00 |
>| 1005        | 63000.00 |

### 7.3. GROUP BY & HAVING

**Definition**:  
- `GROUP BY` arranges rows that share column values into groups.  
- `HAVING` is like `WHERE` but for grouped data.

```sql
SELECT department_id, COUNT(*) AS total_employees
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 1;
```
> **Output** (only departments with more than 1 employee):
>
>| department_id | total_employees |
>|---------------|-----------------|
>| 1             | 2               |

---

## 8. Aggregation Functions (COUNT, SUM, AVG, MIN, MAX)

### 8.1. COUNT

```sql
SELECT COUNT(*) AS total_employees
FROM employees;
```
> **Output**:
>
>| total_employees |
>|-----------------|
>| 4               |

### 8.2. SUM

```sql
SELECT SUM(salary) AS total_salary
FROM employees;
```
> **Output**:
>
>| total_salary |
>|-------------:|
>| 314000.00    |

### 8.3. AVG

```sql
SELECT AVG(salary) AS avg_salary
FROM employees;
```
> **Output**:
>
>| avg_salary  |
>|------------:|
>| 78500.0000  |  
>(Calculated from 75000 + 80000 + 96000 + 63000 = 314000 / 4)

### 8.4. MIN / MAX

```sql
SELECT MIN(salary) AS min_salary, MAX(salary) AS max_salary
FROM employees;
```
> **Output**:
>
>| min_salary | max_salary |
>|-----------:|-----------:|
>| 63000.00   | 96000.00   |

---

## 9. Joins in SQL

**Definition**:  
Joins combine rows from two or more tables based on related columns.

### 9.1. INNER JOIN

**Definition**:  
Returns records that have matching values in both tables.

```sql
SELECT e.first_name, d.department_name
FROM employees e
INNER JOIN departments d 
       ON e.department_id = d.department_id;
```
> **Output**:
>
>| first_name | department_name |
>|------------|-----------------|
>| Alice      | IT             |
>| Carol      | HR             |
>| Dave       | Finance        |
>| Eve        | IT             |

### 9.2. LEFT JOIN

**Definition**:  
Returns all rows from the left table, plus the matching rows from the right table.

```sql
SELECT e.first_name, d.department_name
FROM employees e
LEFT JOIN departments d
       ON e.department_id = d.department_id;
```
> If every `department_id` in `employees` has a match in `departments`, you’ll see the same result as the `INNER JOIN`. If any row in `employees` had a department_id not found in `departments`, it would appear in full with `NULL` for `department_name`.

### 9.3. RIGHT JOIN

**Definition**:  
Returns all rows from the right table, plus the matching rows from the left table.

```sql
SELECT e.first_name, d.department_name
FROM employees e
RIGHT JOIN departments d
       ON e.department_id = d.department_id;
```
> If a `department_id` in `departments` has no matching employees, that `department_name` will appear with `NULL` values for `e.first_name`.

### 9.4. FULL OUTER JOIN

**Definition**:  
Returns all rows where there is a match in either left or right table.  
> **Note**: MySQL doesn’t support `FULL OUTER JOIN` directly. PostgreSQL, Oracle, and MS SQL Server do.

### 9.5. CROSS JOIN

**Definition**:  
Returns the Cartesian product (every row in the first table paired with every row in the second table).

```sql
SELECT e.first_name, d.department_name
FROM employees e
CROSS JOIN departments d;
```
> With 4 employees and 3 departments, this would generate 12 rows total.

---

## 10. Subqueries

**Definition**:  
A subquery is a query nested inside another SQL statement. Often used in `SELECT`, `FROM`, or `WHERE` clauses.

**Example**:  
Find employees whose salary is above the **average** salary of all employees.

```sql
SELECT first_name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
```
> **Output** (above average, which was 78,500):
>
>| first_name | salary   |
>|------------|----------|
>| Carol      | 80000.00 |
>| Dave       | 96000.00 |

---

## 11. Set Operators (UNION, UNION ALL, INTERSECT, EXCEPT)

These commands combine results from multiple `SELECT` statements.

### 11.1. UNION

**Definition**:  
Combines results from two `SELECT` statements, removing duplicates.

```sql
SELECT first_name FROM employees
UNION
SELECT department_name FROM departments;
```
> Merges all the `first_name` and `department_name` values into a single set, removing duplicates.

### 11.2. UNION ALL

**Definition**:  
Same as `UNION` but **includes** duplicates.

### 11.3. INTERSECT

**Definition**:  
Returns rows common to both queries.  
> **Note**: Not supported by MySQL.

### 11.4. EXCEPT / MINUS

**Definition**:  
Returns rows from the first query that are **not** in the second query.  
> **Syntax** differs among RDBMS. In Oracle, you have `MINUS`; in PostgreSQL or SQL Server, you have `EXCEPT`.

---

## 12. Indexes

**Definition**:  
Indexes speed up data retrieval at the cost of slower writes (INSERT/UPDATE/DELETE).

### 12.1. CREATE INDEX

```sql
CREATE INDEX idx_salary
ON employees (salary);
```
> Improves search performance when querying by `salary`.

### 12.2. DROP INDEX

```sql
DROP INDEX idx_salary;
```
> Removes the index.

---

## 13. Transactions

**Definition**:  
A transaction is a set of operations that succeed or fail as one unit.

### 13.1. BEGIN TRANSACTION

```sql
BEGIN TRANSACTION;
```
(*Varies by system; MySQL often uses `START TRANSACTION;`.*)

### 13.2. COMMIT

```sql
COMMIT;
```
> Saves all changes made during the transaction.

### 13.3. ROLLBACK

```sql
ROLLBACK;
```
> Undoes all changes since the start of the transaction.

**Example**:

```sql
START TRANSACTION;
UPDATE employees
SET salary = 100000
WHERE employee_id = 1005;

ROLLBACK; -- undo that update
```
> After `ROLLBACK`, Eve’s salary remains 63000.

---

## 14. Views

**Definition**:  
A **view** is a virtual table derived from a query. It can simplify complex queries or limit data exposure.

### 14.1. CREATE VIEW

```sql
CREATE VIEW high_earners AS
SELECT first_name, last_name, salary
FROM employees
WHERE salary > 70000;
```

### 14.2. SELECT from a View

```sql
SELECT *
FROM high_earners;
```
> Shows all employees earning more than 70,000.

### 14.3. DROP VIEW

```sql
DROP VIEW IF EXISTS high_earners;
```

---

## 15. Stored Procedures & Functions (Overview)

> **Note**: Syntax varies by database (MySQL vs. PostgreSQL vs. SQL Server).

### 15.1. Stored Procedure (MySQL Example)

```sql
DELIMITER //
CREATE PROCEDURE GetEmployeeCountByDept(IN dept INT, OUT empCount INT)
BEGIN
    SELECT COUNT(*)
    INTO empCount
    FROM employees
    WHERE department_id = dept;
END //
DELIMITER ;
```
> Now you can call it:
> ```sql
> CALL GetEmployeeCountByDept(1, @count);
> SELECT @count; -- shows how many employees in department 1
> ```

### 15.2. Stored Function (MySQL Example)

```sql
DELIMITER //
CREATE FUNCTION GetTotalSalaryByDept(dept INT)
RETURNS DECIMAL(10,2)
BEGIN
    DECLARE total DECIMAL(10,2);
    SELECT SUM(salary)
    INTO total
    FROM employees
    WHERE department_id = dept;
    RETURN total;
END //
DELIMITER ;
```
> Usage:
> ```sql
> SELECT GetTotalSalaryByDept(1);
> ```
> This returns the sum of salaries in department 1.

---

## 16. Basic Security & Permissions

**Definition**:  
Control who can do what within the database.

- **GRANT**: Give privileges.
- **REVOKE**: Remove privileges.

**Example** (MySQL/MariaDB style):

```sql
GRANT SELECT, INSERT ON my_database.employees
TO 'username'@'localhost';

REVOKE INSERT ON my_database.employees
FROM 'username'@'localhost';
```

---

## 17. Example Putting It All Together

Below is a quick demonstration. Assume we have no tables yet, and we want to build them:

```sql
-- 1. Create a new database (some RDBMS may skip this step if already in a DB)
CREATE DATABASE company_db;
USE company_db;

-- 2. Create tables
CREATE TABLE departments (
    department_id   INT PRIMARY KEY,
    department_name VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- 3. Insert data
INSERT INTO departments (department_id, department_name)
VALUES (1, 'IT'), (2, 'HR'), (3, 'Finance');

INSERT INTO employees (employee_id, first_name, last_name, department_id, salary)
VALUES 
(1001, 'Alice', 'Smith', 1, 75000),
(1002, 'Bob', 'Johnson', 2, 50000),
(1003, 'Carol', 'White', 2, 52000),
(1004, 'Dave', 'Green', 3, 96000);

-- 4. A join query
SELECT e.first_name, d.department_name, e.salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
ORDER BY e.salary DESC;

-- 5. Aggregation example
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id;
```

**Example Output** from step 4 (JOIN + ORDER BY):

| first_name | department_name | salary   |
|------------|-----------------|----------|
| Dave       | Finance         | 96000.00 |
| Alice      | IT              | 75000.00 |
| Carol      | HR              | 52000.00 |
| Bob        | HR              | 50000.00 |

---

## 18. Final Tips & Best Practices

1. **Backup** your database before large changes.  
2. Use **EXPLAIN** to understand query execution plans.  
3. Balance **normalization** and **performance** needs.  
4. Avoid *selecting `*`* in production queries—explicitly name columns for clarity and efficiency.  
5. Keep queries readable (proper indentation, aliases) and comment your code.

---

## Conclusion

This **SQL Cheat Sheet** brings together the core topics:  
- **Creating/Altering** tables (DDL).  
- **Inserting/Updating/Deleting** data (DML).  
- **Querying** (SELECT, WHERE, JOIN, GROUP BY, HAVING).  
- **Transactions, Indexes, Views, Stored Procedures**.  

---
# **19. SQL Interview Questions & Answers**

This section covers **important SQL interview questions** along with their solutions.

---

## **Basic SQL Interview Questions**

### **1. What is the difference between SQL and NoSQL?**
| Feature      | SQL (Relational) | NoSQL (Non-Relational) |
|-------------|-----------------|----------------------|
| Structure   | Tables with rows & columns | Key-Value, Document, Column, Graph-based |
| Schema      | Fixed schema (strict structure) | Dynamic schema (flexible structure) |
| Scalability | Vertical (scale-up by adding more power to one server) | Horizontal (scale-out by adding more servers) |
| ACID        | Supports ACID transactions | Some NoSQL databases provide eventual consistency |
| Best for    | Structured data & transactions | Unstructured, semi-structured, or rapidly changing data |

> **Example:** SQL databases include MySQL, PostgreSQL, SQL Server; NoSQL databases include MongoDB, Cassandra.

---

### **2. What is the difference between DELETE, TRUNCATE, and DROP?**
| Command   | Deletes Rows? | Deletes Structure? | Rollback Possible? | Performance |
|-----------|--------------|--------------------|---------------------|-------------|
| DELETE   | Yes (specific rows via `WHERE`) | No | Yes (inside transactions) | Slow (logs each row) |
| TRUNCATE | Yes (all rows) | No | No | Faster than DELETE |
| DROP     | Yes (all rows) | Yes (removes table completely) | No | Fastest (removes table entirely) |

> **Example:**  
```sql
DELETE FROM employees WHERE employee_id = 1001; -- Deletes one row  
TRUNCATE TABLE employees;  -- Deletes all rows but keeps the structure  
DROP TABLE employees;  -- Deletes the entire table including structure  
```

---

### **3. What is the difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN, and CROSS JOIN?**
| Join Type         | Description |
|------------------|-------------|
| **INNER JOIN**   | Returns rows where there is a match in both tables. |
| **LEFT JOIN**    | Returns all rows from the left table and matching rows from the right. |
| **RIGHT JOIN**   | Returns all rows from the right table and matching rows from the left. |
| **FULL JOIN**    | Returns all rows when there is a match in **either** table. |
| **CROSS JOIN**   | Returns the Cartesian product of the two tables (every row in table A with every row in table B). |

**Example Query:**
```sql
SELECT e.first_name, d.department_name 
FROM employees e
INNER JOIN departments d 
ON e.department_id = d.department_id;
```
> **Output (from our sample data)**:
> ```
> first_name | department_name
> ---------- | ---------------
> Alice      | IT
> Carol      | HR
> Dave       | Finance
> ```

---

## **Intermediate SQL Interview Questions**

### **4. How to find the **3rd highest salary** in a table?**
Finding the **Nth highest salary** is a common interview question.

#### **Method 1: Using `LIMIT` with `OFFSET` (MySQL, PostgreSQL)**
```sql
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;
```
> **Explanation:**  
> - `ORDER BY salary DESC` sorts the salaries in descending order.  
> - `LIMIT 1 OFFSET 2` skips the first two highest salaries and fetches the 3rd one.

---

#### **Method 2: Using `DISTINCT` and `ORDER BY` with `LIMIT` (Alternative)**
```sql
SELECT salary 
FROM (
    SELECT DISTINCT salary 
    FROM employees 
    ORDER BY salary DESC 
    LIMIT 3
) AS temp 
ORDER BY salary ASC
LIMIT 1;
```
> **Explanation:**  
> - The inner query selects the **top 3 distinct salaries**.  
> - The outer query sorts them in ascending order and picks the first row.

---

#### **Method 3: Using Subquery with `MAX()`**
```sql
SELECT MAX(salary) AS third_highest_salary
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (
        SELECT MAX(salary)
        FROM employees
    )
);
```
> **Explanation:**  
> - First, find the highest salary.  
> - Then, find the **second highest** salary using `< MAX(salary)`.  
> - Finally, find the **third highest** salary.

---

#### **Method 4: Using `DENSE_RANK()` (Best for SQL Server, PostgreSQL, Oracle)**
```sql
SELECT salary 
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
    FROM employees
) AS ranked
WHERE rank = 3;
```
> **Explanation:**  
> - `DENSE_RANK()` assigns a rank to each salary, handling duplicates properly.  
> - The outer query filters for `rank = 3`.

---

## **Advanced SQL Interview Questions**

### **5. How do you find duplicate records in a table?**
```sql
SELECT first_name, last_name, COUNT(*) 
FROM employees
GROUP BY first_name, last_name
HAVING COUNT(*) > 1;
```
> **Explanation:**  
> - Groups by `first_name` and `last_name`.  
> - `HAVING COUNT(*) > 1` filters duplicates.

---

### **6. How do you delete duplicate records but keep one?**
```sql
DELETE FROM employees 
WHERE employee_id NOT IN (
    SELECT MIN(employee_id) 
    FROM employees 
    GROUP BY first_name, last_name
);
```
> **Explanation:**  
> - Keeps only the **earliest inserted record** (`MIN(employee_id)`).  
> - Deletes all other duplicates.

---

### **7. What is the difference between RANK(), DENSE_RANK(), and ROW_NUMBER()?**
| Function     | Handles Duplicates? | Gaps in Ranking? | Example |
|-------------|---------------------|------------------|---------|
| `RANK()`    | Yes                 | Yes (skips next rank) | 1, 2, 2, 4 |
| `DENSE_RANK()` | Yes              | No (no skipping) | 1, 2, 2, 3 |
| `ROW_NUMBER()` | No               | No (unique for every row) | 1, 2, 3, 4 |

```sql
SELECT first_name, salary,
    RANK() OVER (ORDER BY salary DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;
```

---

### **8. What are window functions?**
**Definition:** Window functions **perform calculations across a set of table rows** that are related to the current row.

#### **Example: Running Total using `SUM()`**
```sql
SELECT first_name, salary,
    SUM(salary) OVER (PARTITION BY department_id ORDER BY salary DESC) AS running_total
FROM employees;
```
> **Explanation:**  
> - `PARTITION BY department_id` resets the total per department.  
> - `ORDER BY salary DESC` accumulates salaries in descending order.

---

### **9. What is a self-join?**
A **self-join** joins a table with itself.

#### **Example: Finding Employees with the Same Salary**
```sql
SELECT A.first_name AS emp1, B.first_name AS emp2, A.salary
FROM employees A
JOIN employees B
ON A.salary = B.salary AND A.employee_id <> B.employee_id;
```
> **Explanation:**  
> - Joins the `employees` table with itself.  
> - Ensures `employee_id` is different to avoid self-matching.

---

## **Conclusion**
This section covered **common SQL interview questions** along with **concept explanations, queries, and outputs**. These will help you **crack SQL-based interviews** and handle **real-world data scenarios** confidently.

---