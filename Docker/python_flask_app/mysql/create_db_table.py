import mysql.connector

web_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="web_db",
    autocommit=True,
    # can_consume_results=True

)

cursor = web_db.cursor()
cursor.execute("SELECT COUNT(DISTINCT `TABLE_NAME`) AS anyAliasName FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `table_schema` = 'web_db'")
for x in cursor:
    if 0 in x:
        print("no tables, creating...")
        cursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


cursor.execute("SHOW TABLES")
for x in cursor:
    print("creating audit log table")
    cursor.execute("CREATE TABLE audit_log (id INT AUTO_INCREMENT PRIMARY KEY, ip_source VARCHAR(255))")