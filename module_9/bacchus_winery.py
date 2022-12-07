<html>
<head>
<title>bacchus_winery.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6a8759;}
.s3 { color: #808080;}
.s4 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
bacchus_winery.py</font>
</center></td></tr></table>
<pre><span class="s0">from </span><span class="s1">__future__ </span><span class="s0">import </span><span class="s1">print_function</span>
<span class="s0">import </span><span class="s1">mysql.connector</span>
<span class="s0">from </span><span class="s1">mysql.connector </span><span class="s0">import </span><span class="s1">errorcode</span>

<span class="s1">config = {</span>
    <span class="s2">'port'</span><span class="s1">: </span><span class="s2">'3006'</span><span class="s0">,</span>
    <span class="s2">'user'</span><span class="s1">: </span><span class="s2">'root'</span><span class="s0">,</span>
    <span class="s2">'password'</span><span class="s1">: </span><span class="s2">'Yodapop311!'</span><span class="s0">,</span>
    <span class="s2">'host'</span><span class="s1">: </span><span class="s2">'localhost'</span><span class="s0">,</span>
    <span class="s2">'database'</span><span class="s1">: </span><span class="s2">'bacchus_winery'</span><span class="s0">,</span>
    <span class="s2">'raise_on_warnings'</span><span class="s1">: </span><span class="s0">True</span>
<span class="s1">}</span>
<span class="s0">try</span><span class="s1">:</span>
    <span class="s1">mydb = mysql.connector.connect(**config)</span>

    <span class="s1">print(</span><span class="s2">&quot;</span><span class="s0">\n </span><span class="s2">Database user {} connected to MySQL on host {} with database {}&quot;</span><span class="s1">.format(</span>
        <span class="s1">config[</span><span class="s2">&quot;user&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">config[</span><span class="s2">&quot;host&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">config[</span><span class="s2">&quot;database&quot;</span><span class="s1">]))</span>
    <span class="s1">input(</span><span class="s2">&quot;</span><span class="s0">\n\n </span><span class="s2">Press any key to continue...</span><span class="s0">\n</span><span class="s2">&quot;</span><span class="s1">)</span>

<span class="s0">except </span><span class="s1">mysql.connector.Error </span><span class="s0">as </span><span class="s1">err:</span>
    <span class="s0">if </span><span class="s1">err.errno == errorcode.ER_ACCESS_DENIED_ERROR:</span>
        <span class="s1">print(</span><span class="s2">&quot; The supplied username or password are invalid&quot;</span><span class="s1">)</span>
    <span class="s0">elif </span><span class="s1">err.errno == errorcode.ER_BAD_DB_ERROR:</span>
        <span class="s1">print(</span><span class="s2">&quot; The specified database does not exist&quot;</span><span class="s1">)</span>
    <span class="s0">else</span><span class="s1">:</span>
        <span class="s1">print(err)</span>

<span class="s1">DB_NAME = </span><span class="s2">'bacchus_winery'</span>

<span class="s1">myCursor = mydb.cursor()</span>


<span class="s3"># Function to erase tables if they exist to start with a clean database</span>
<span class="s0">def </span><span class="s1">drop_tables(myCursor):</span>
    <span class="s1">tables = </span><span class="s2">&quot;DROP TABLE wine&quot;</span>
    <span class="s1">myCursor.execute(tables)</span>
    <span class="s1">mydb.commit()</span>


<span class="s1">drop_tables(myCursor)</span>


<span class="s1">TABLES = {}</span>
<span class="s1">TABLES[</span><span class="s2">'wine'</span><span class="s1">] = (</span>
    <span class="s2">&quot;CREATE TABLE wine&quot;</span>
    <span class="s2">&quot;  (wine_id int NOT NULL AUTO_INCREMENT KEY,&quot;</span>
    <span class="s2">&quot;  wine_name varchar(25) NOT NULL,&quot;</span>
    <span class="s2">&quot;  units int NOT NULL,&quot;</span>
    <span class="s2">&quot;  batch_month varchar(25) NOT NULL )&quot;</span><span class="s1">)</span>

<span class="s1">TABLES[</span><span class="s2">'orders'</span><span class="s1">] = (</span>
    <span class="s2">&quot;CREATE TABLE orders&quot;</span>
    <span class="s2">&quot;  (order_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,&quot;</span>
    <span class="s2">&quot;  units int NOT NULL,&quot;</span>
    <span class="s2">&quot;  wine_name varchar(25) NOT NULL)&quot;</span><span class="s1">)</span>


<span class="s1">TABLES[</span><span class="s2">'distributors'</span><span class="s1">] = (</span>
    <span class="s2">&quot;CREATE TABLE distributors&quot;</span>
    <span class="s2">&quot;  (distributor_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,&quot;</span>
    <span class="s2">&quot;  distributor_name varchar(25) NOT NULL,&quot;</span>
    <span class="s2">&quot;  order_id int NOT NULL)&quot;</span><span class="s1">)</span>


<span class="s1">TABLES[</span><span class="s2">'suppliers'</span><span class="s1">] = (</span>
    <span class="s2">&quot;CREATE TABLE suppliers&quot;</span>
    <span class="s2">&quot;  (supplier_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,&quot;</span>
    <span class="s2">&quot;  supplier_name varchar(25) NOT NULL,&quot;</span>
    <span class="s2">&quot;  expected_delivery_date DATE NOT NULL,&quot;</span>
    <span class="s2">&quot;  actual_delivery_date DATE NOT NULL,&quot;</span>
    <span class="s2">&quot;  supply_name varchar(25) NOT NULL)&quot;</span><span class="s1">)</span>

<span class="s1">TABLES[</span><span class="s2">'deliveries'</span><span class="s1">] = (</span>
    <span class="s2">&quot;CREATE TABLE deliveries&quot;</span>
    <span class="s2">&quot;  (delivery_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,&quot;</span>
    <span class="s2">&quot;  supplier_id int NOT NULL,&quot;</span>
    <span class="s2">&quot;  inventory int NOT NULL)&quot;</span><span class="s1">)</span>

<span class="s1">TABLES[</span><span class="s2">'supplies'</span><span class="s1">] = (</span>
    <span class="s2">&quot;CREATE TABLE supplies&quot;</span>
    <span class="s2">&quot;  (supply_id int NOT NULL PRIMARY KEY,&quot;</span>
    <span class="s2">&quot;  supply_name varchar(25) NOT NULL,&quot;</span>
    <span class="s2">&quot;  inventory int NOT NULL)&quot;</span><span class="s1">)</span>


<span class="s1">TABLES[</span><span class="s2">'employees'</span><span class="s1">] = (</span>
    <span class="s2">&quot;CREATE TABLE employees&quot;</span>
    <span class="s2">&quot;  (employee_id int NOT NULL AUTO_INCREMENT PRIMARY KEY,&quot;</span>
    <span class="s2">&quot;  first_name varchar(25) NOT NULL,&quot;</span>
    <span class="s2">&quot;  last_name varchar(25) NOT NULL,&quot;</span>
    <span class="s2">&quot;job_title varchar(25) NOT NULL)&quot;</span><span class="s1">)</span>


<span class="s1">TABLES[</span><span class="s2">'time_sheet'</span><span class="s1">] = (</span>
    <span class="s2">&quot;CREATE TABLE time_sheet&quot;</span>
    <span class="s2">&quot;  (week_id int NOT NULL PRIMARY KEY,&quot;</span>
    <span class="s2">&quot;  hours_worked_weekly int NOT NULL,&quot;</span>
    <span class="s2">&quot;  ot_worked_weekly int NOT NULL,&quot;</span>
    <span class="s2">&quot;  employee_id int NOT NULL)&quot;</span><span class="s1">)</span>


<span class="s0">for </span><span class="s1">table_name </span><span class="s0">in </span><span class="s1">TABLES:</span>
    <span class="s1">table_description = TABLES[table_name]</span>
    <span class="s0">try</span><span class="s1">:</span>
        <span class="s1">print(</span><span class="s2">&quot;Creating table {}: &quot;</span><span class="s1">.format(table_name)</span><span class="s0">, </span><span class="s1">end=</span><span class="s2">''</span><span class="s1">)</span>
        <span class="s1">myCursor.execute(table_description)</span>
    <span class="s0">except </span><span class="s1">mysql.connector.Error </span><span class="s0">as </span><span class="s1">err:</span>
        <span class="s0">if </span><span class="s1">err.errno == errorcode.ER_TABLE_EXISTS_ERROR:</span>
            <span class="s1">print(</span><span class="s2">&quot;already exists.&quot;</span><span class="s1">)</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s1">print(err.msg)</span>
    <span class="s0">else</span><span class="s1">:</span>
        <span class="s1">print(</span><span class="s2">&quot;OK</span><span class="s0">\n</span><span class="s2">&quot;</span><span class="s1">)</span>

<span class="s3"># Insert values into wine table</span>
<span class="s1">sql1 = </span><span class="s2">&quot;INSERT INTO wine (wine_name, units, batch_month) VALUE ('Merlot', 50, 'January')&quot;</span>
<span class="s1">sql2 = </span><span class="s2">&quot;INSERT INTO wine (wine_name, units, batch_month) VALUE ('Cabernet', 40, 'February')&quot;</span>
<span class="s1">sql3 = </span><span class="s2">&quot;INSERT INTO wine (wine_name, units, batch_month) VALUE ('Chablis', 60, 'April')&quot;</span>
<span class="s1">sql4 = </span><span class="s2">&quot;INSERT INTO wine (wine_name, units, batch_month) VALUE ('Chardonnay', 50, 'March')&quot;</span>
<span class="s1">myCursor.execute(sql1)</span>
<span class="s1">myCursor.execute(sql2)</span>
<span class="s1">myCursor.execute(sql3)</span>
<span class="s1">myCursor.execute(sql4)</span>
<span class="s1">mydb.commit()</span>

<span class="s3"># Print out values</span>
<span class="s1">print(</span><span class="s2">&quot;-Displaying Wine Records-&quot;</span><span class="s1">)</span>
<span class="s1">query1 = </span><span class="s2">&quot;SELECT wine_name, units, batch_month FROM wine&quot;</span>
<span class="s1">myCursor.execute(query1)</span>
<span class="s1">wines = myCursor.fetchall()</span>
<span class="s0">for </span><span class="s1">wine </span><span class="s0">in </span><span class="s1">wines:</span>
    <span class="s1">print(</span><span class="s2">&quot;Wine Name: {}</span><span class="s0">\n</span><span class="s2">Number of units: {}</span><span class="s0">\n</span><span class="s2">Batch Month: {}</span><span class="s0">\n</span><span class="s2">&quot;</span><span class="s1">.format(wine[</span><span class="s4">0</span><span class="s1">]</span><span class="s0">, </span><span class="s1">wine[</span><span class="s4">1</span><span class="s1">]</span><span class="s0">,</span>
                                                                         <span class="s1">wine[</span><span class="s4">2</span><span class="s1">]))</span>

<span class="s3"># Insert values into Orders table</span>
<span class="s1">orders1 = </span><span class="s2">&quot;INSERT INTO orders (units, wine_name) VALUE (10, 'Merlot')&quot;</span>
<span class="s1">orders2 = </span><span class="s2">&quot;INSERT INTO orders (units, wine_name) VALUE (15, 'Cabernet')&quot;</span>
<span class="s1">orders3 = </span><span class="s2">&quot;INSERT INTO orders (units, wine_name) VALUE (12, 'Chablis')&quot;</span>
<span class="s1">orders4 = </span><span class="s2">&quot;INSERT INTO orders (units, wine_name) VALUE (10, 'Chardonnay')&quot;</span>
<span class="s1">myCursor.execute(orders1)</span>
<span class="s1">myCursor.execute(orders2)</span>
<span class="s1">myCursor.execute(orders3)</span>
<span class="s1">myCursor.execute(orders4)</span>
<span class="s1">mydb.commit()</span>

<span class="s1">print(</span><span class="s2">&quot;-Displaying Orders-&quot;</span><span class="s1">)</span>
<span class="s1">query2 = </span><span class="s2">&quot;SELECT units, wine_name FROM orders&quot;</span>
<span class="s1">myCursor.execute(query2)</span>
<span class="s1">orders = myCursor.fetchall()</span>
<span class="s0">for </span><span class="s1">order </span><span class="s0">in </span><span class="s1">orders:</span>
    <span class="s1">print(</span><span class="s2">&quot;Number of units: {}</span><span class="s0">\n</span><span class="s2">Wine Name: {}</span><span class="s0">\n</span><span class="s2">&quot;</span><span class="s1">.format(order[</span><span class="s4">0</span><span class="s1">]</span><span class="s0">, </span><span class="s1">order[</span><span class="s4">1</span><span class="s1">]))</span>

<span class="s3"># Insert values into Distributors table</span>
<span class="s1">dis1 = </span><span class="s2">&quot;INSERT INTO distributors (distributor_name, order_id) VALUE ('Wines to GO', 2)&quot;</span>
<span class="s1">dis2 = </span><span class="s2">&quot;INSERT INTO distributors (distributor_name, order_id) VALUE ('Partners in Wine', 3)&quot;</span>
<span class="s1">dis3 = </span><span class="s2">&quot;INSERT INTO distributors (distributor_name, order_id) VALUE ('Sip Happens Co.', 1)&quot;</span>
<span class="s1">myCursor.execute(dis1)</span>
<span class="s1">myCursor.execute(dis2)</span>
<span class="s1">myCursor.execute(dis3)</span>
<span class="s1">mydb.commit()</span>

<span class="s1">print(</span><span class="s2">&quot;-Displaying Distributors-&quot;</span><span class="s1">)</span>
<span class="s1">query3 = </span><span class="s2">&quot;SELECT distributor_name, order_id FROM orders&quot;</span>
<span class="s1">myCursor.execute(query3)</span>
<span class="s1">distributors = myCursor.fetchall()</span>
<span class="s0">for </span><span class="s1">distributor </span><span class="s0">in </span><span class="s1">distributors:</span>
    <span class="s1">print(</span><span class="s2">&quot;Distributor Name: {}</span><span class="s0">\n</span><span class="s2">Order ID: {}</span><span class="s0">\n</span><span class="s2">&quot;</span><span class="s1">.format(distributor[</span><span class="s4">0</span><span class="s1">]</span><span class="s0">, </span><span class="s1">distributor[</span><span class="s4">1</span><span class="s1">]))</span>


<span class="s3"># Insert values into Suppliers table</span>
<span class="s1">sup1 = </span><span class="s2">&quot;INSERT INTO suppliers (supplier_name, expected_delivery_date, actual_delivery_date, supply_name)&quot; </span><span class="s1">\</span>
       <span class="s2">&quot;VALUE ('The New Corker', 20220110, 20220115, 'Corks')&quot;</span>
<span class="s1">sup2 = </span><span class="s2">&quot;INSERT INTO suppliers (supplier_name, expected_delivery_date, actual_delivery_date, supply_name)&quot; </span><span class="s1">\</span>
       <span class="s2">&quot;VALUE ('Boxes n Stuff', 20220215, 20220215, 'Boxes')&quot;</span>
<span class="s1">sup3 = </span><span class="s2">&quot;INSERT INTO suppliers (supplier_name, expected_delivery_date, actual_delivery_date, supply_name)&quot; </span><span class="s1">\</span>
       <span class="s2">&quot;VALUE ('Wine Supply', 20220320, 20220415, 'Tubing')&quot;</span>
<span class="s1">myCursor.execute(sup1)</span>
<span class="s1">myCursor.execute(sup2)</span>
<span class="s1">myCursor.execute(sup3)</span>
<span class="s1">mydb.commit()</span>

<span class="s3"># Print out values</span>
<span class="s1">print(</span><span class="s2">&quot;-Displaying Suppliers Records-&quot;</span><span class="s1">)</span>
<span class="s1">query4 = </span><span class="s2">&quot;SELECT supplier_name, expected_delivery_date, actual_delivery_date, supply_name FROM suppliers&quot;</span>
<span class="s1">myCursor.execute(query4)</span>
<span class="s1">suppliers = myCursor.fetchall()</span>
<span class="s0">for </span><span class="s1">supplier </span><span class="s0">in </span><span class="s1">suppliers:</span>
    <span class="s1">print(</span><span class="s2">&quot;supplier_name: {}</span><span class="s0">\n</span><span class="s2">expected_delivery_date: {}</span><span class="s0">\n</span><span class="s2">actual_delivery_date: {}</span><span class="s0">\n</span><span class="s2">supply_name: {}</span><span class="s0">\n</span><span class="s2">&quot;</span><span class="s1">.format(</span>
        <span class="s1">supplier[</span><span class="s4">0</span><span class="s1">]</span><span class="s0">, </span><span class="s1">supplier[</span><span class="s4">1</span><span class="s1">]</span><span class="s0">, </span><span class="s1">supplier[</span><span class="s4">2</span><span class="s1">]</span><span class="s0">, </span><span class="s1">supplier[</span><span class="s4">3</span><span class="s1">]))</span>

<span class="s3"># Insert values into deliveries table</span>
<span class="s1">del1 = </span><span class="s2">&quot;INSERT INTO deliveries (supplier_id, inventory) VALUE (1, 50)&quot;</span>
<span class="s1">del2 = </span><span class="s2">&quot;INSERT INTO deliveries (supplier_id, inventory) VALUE (2, 40)&quot;</span>
<span class="s1">del3 = </span><span class="s2">&quot;INSERT INTO deliveries (supplier_id, inventory) VALUE (3, 60)&quot;</span>
<span class="s1">myCursor.execute(del1)</span>
<span class="s1">myCursor.execute(del2)</span>
<span class="s1">myCursor.execute(del3)</span>
<span class="s1">mydb.commit()</span>

<span class="s3"># Print out values</span>
<span class="s1">print(</span><span class="s2">&quot;-Displaying deliveries Records-&quot;</span><span class="s1">)</span>
<span class="s1">query5 = </span><span class="s2">&quot;SELECT supplier_id, inventory FROM deliveries&quot;</span>
<span class="s1">myCursor.execute(query5)</span>
<span class="s1">deliveries = myCursor.fetchall()</span>
<span class="s0">for </span><span class="s1">delivery </span><span class="s0">in </span><span class="s1">deliveries:</span>
    <span class="s1">print(</span><span class="s2">&quot;Supplier ID: {}</span><span class="s0">\n</span><span class="s2">Inventory: {}</span><span class="s0">\n</span><span class="s2">&quot;</span><span class="s1">.format(delivery[</span><span class="s4">0</span><span class="s1">]</span><span class="s0">, </span><span class="s1">delivery[</span><span class="s4">1</span><span class="s1">]))</span>

<span class="s3"># Insert values into supplies table</span>
<span class="s1">spl1 = </span><span class="s2">&quot;INSERT INTO supplies (supply_name, inventory) VALUE ('Corks', 50)&quot;</span>
<span class="s1">spl2 = </span><span class="s2">&quot;INSERT INTO supplies (supply_name, inventory) VALUE ('Boxes', 40)&quot;</span>
<span class="s1">myCursor.execute(spl1)</span>
<span class="s1">myCursor.execute(spl2)</span>
<span class="s1">mydb.commit()</span>

<span class="s3"># Print out values</span>
<span class="s1">print(</span><span class="s2">&quot;-Displaying Supplies Records-&quot;</span><span class="s1">)</span>
<span class="s1">query6 = </span><span class="s2">&quot;SELECT supply_name, inventory FROM supplies&quot;</span>
<span class="s1">myCursor.execute(query6)</span>
<span class="s1">supplies = myCursor.fetchall()</span>
<span class="s0">for </span><span class="s1">supply </span><span class="s0">in </span><span class="s1">supplies:</span>
    <span class="s1">print(</span><span class="s2">&quot;Supply Name: {}</span><span class="s0">\n</span><span class="s2">Inventory: {}</span><span class="s0">\n</span><span class="s2">&quot;</span><span class="s1">.format(supply[</span><span class="s4">0</span><span class="s1">]</span><span class="s0">, </span><span class="s1">supply[</span><span class="s4">1</span><span class="s1">]))</span>

<span class="s3"># Insert values into employees table</span>
<span class="s1">emp1 = </span><span class="s2">&quot;INSERT INTO employees (first_name, last_name, job_title) VALUE ('Stan', 'Bacchus', 'Co-Owner')&quot;</span>
<span class="s1">emp2 = </span><span class="s2">&quot;INSERT INTO employees (first_name, last_name, job_title) VALUE ('Davis', 'Bacchus', 'Co-Owner')&quot;</span>
<span class="s1">emp3 = </span><span class="s2">&quot;INSERT INTO employees (first_name, last_name, job_title) VALUE ('Janet', 'Collins', 'Finances and Payroll')&quot;</span>
<span class="s1">emp4 = </span><span class="s2">&quot;INSERT INTO employees (first_name, last_name, job_title) VALUE ('Roz', 'Murphy', 'Marketing Department')&quot;</span>
<span class="s1">emp5 = </span><span class="s2">&quot;INSERT INTO employees (first_name, last_name, job_title) VALUE ('Henry', 'Doyle', 'Production Line')&quot;</span>
<span class="s1">emp6 = </span><span class="s2">&quot;INSERT INTO employees (first_name, last_name, job_title) VALUE ('Maria', 'Costanza', 'Distribution')&quot;</span>
<span class="s1">myCursor.execute(emp1)</span>
<span class="s1">myCursor.execute(emp2)</span>
<span class="s1">myCursor.execute(emp3)</span>
<span class="s1">myCursor.execute(emp4)</span>
<span class="s1">myCursor.execute(emp5)</span>
<span class="s1">myCursor.execute(emp6)</span>
<span class="s1">mydb.commit()</span>

<span class="s3"># Print out values</span>
<span class="s1">print(</span><span class="s2">&quot;-Displaying Employee Records-&quot;</span><span class="s1">)</span>
<span class="s1">query7 = </span><span class="s2">&quot;SELECT first_name, last_name, job_title FROM employees&quot;</span>
<span class="s1">myCursor.execute(query7)</span>
<span class="s1">employees = myCursor.fetchall()</span>
<span class="s0">for </span><span class="s1">employee </span><span class="s0">in </span><span class="s1">employees:</span>
    <span class="s1">print(</span><span class="s2">&quot;First Name: {}</span><span class="s0">\n</span><span class="s2">Last Name: {}</span><span class="s0">\n</span><span class="s2">Job Title: {}</span><span class="s0">\n</span><span class="s2">&quot;</span><span class="s1">.format(employee[</span><span class="s4">0</span><span class="s1">]</span><span class="s0">, </span><span class="s1">employee[</span><span class="s4">1</span><span class="s1">]</span><span class="s0">,</span>
                                                                  <span class="s1">employee[</span><span class="s4">2</span><span class="s1">]))</span>

<span class="s3"># Insert values into time sheet table</span>
<span class="s1">time1 = </span><span class="s2">&quot;INSERT INTO time_sheet (week_id, hours_worked_weekly, ot_worked_weekly, employee_id) VALUE (1,45, 5, 1)&quot;</span>
<span class="s1">time2 = </span><span class="s2">&quot;INSERT INTO time_sheet (week_id, hours_worked_weekly, ot_worked_weekly, employee_id) VALUE (2, 50, 10, 2)&quot;</span>
<span class="s1">time3 = </span><span class="s2">&quot;INSERT INTO time_sheet (week_id, hours_worked_weekly, ot_worked_weekly, employee_id) VALUE (3, 32, 0, 3)&quot;</span>
<span class="s1">time4 = </span><span class="s2">&quot;INSERT INTO time_sheet (week_id, hours_worked_weekly, ot_worked_weekly, employee_id) VALUE (4, 45, 5, 4)&quot;</span>
<span class="s1">time5 = </span><span class="s2">&quot;INSERT INTO time_sheet (week_id, hours_worked_weekly, ot_worked_weekly, employee_id) VALUE (5, 60, 20, 5)&quot;</span>
<span class="s1">time6 = </span><span class="s2">&quot;INSERT INTO time_sheet (week_id, hours_worked_weekly, ot_worked_weekly, employee_id) VALUE (6, 40, 0, 6)&quot;</span>
<span class="s1">myCursor.execute(time1)</span>
<span class="s1">myCursor.execute(time2)</span>
<span class="s1">myCursor.execute(time3)</span>
<span class="s1">myCursor.execute(time4)</span>
<span class="s1">myCursor.execute(time5)</span>
<span class="s1">myCursor.execute(time6)</span>
<span class="s1">mydb.commit()</span>

<span class="s3"># Print out values</span>
<span class="s1">print(</span><span class="s2">&quot;-Displaying Time Sheet Records-&quot;</span><span class="s1">)</span>
<span class="s1">query8 = </span><span class="s2">&quot;SELECT week_id, hours_worked_weekly, ot_worked_weekly, employee_id FROM time_sheet&quot;</span>
<span class="s1">myCursor.execute(query8)</span>
<span class="s1">time_sheet = myCursor.fetchall()</span>
<span class="s0">for </span><span class="s1">time </span><span class="s0">in </span><span class="s1">time_sheet:</span>
    <span class="s1">print(</span><span class="s2">&quot;Week ID: {}</span><span class="s0">\n</span><span class="s2">Hours worked weekly: {}</span><span class="s0">\n</span><span class="s2">OT hours worked weekly: {}</span><span class="s0">\n</span><span class="s2">employee ID: {}</span><span class="s0">\n</span><span class="s2">&quot;</span><span class="s1">.format(time[</span><span class="s4">0</span><span class="s1">]</span><span class="s0">, </span><span class="s1">time[</span><span class="s4">1</span><span class="s1">]</span><span class="s0">,</span>
                                                                                                       <span class="s1">time[</span><span class="s4">2</span><span class="s1">]</span><span class="s0">,</span>
                                                                                                       <span class="s1">time[</span><span class="s4">3</span><span class="s1">]))</span></pre>
</body>
</html>