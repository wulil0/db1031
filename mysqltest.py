import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="312145Aa!",
    # database = "mydb"
)
mydb.database = "mydb"
cursor = mydb.cursor()
# cursor.execute("SHOW DATABASES")

# create_table_query = """
# CREATE TABLE IF NOT EXISTS mydb (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     project VARCHAR(255),
#     station VARCHAR(255),
#     station_path VARCHAR(255),
#     data_format VARCHAR(255),
#     host_ip VARCHAR(15),
#     username VARCHAR(255),
#     password VARCHAR(255)
# )
# """
# create_table_query = """SELECT * FROM mydb;"""

# 执行 SQL 语句来创建表格

# tables = cursor.fetchall()

# 打印表格列表

create_table_query = """
CREATE TABLE IF NOT EXISTS test_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    test_time DATETIME,
    project VARCHAR(255),
    station VARCHAR(255),
    file_name VARCHAR(255),
    test_result VARCHAR(50),
    fail_row_count INT,
    fail_content TEXT,
    sn_number VARCHAR(255),
    fixture_number VARCHAR(255),
    fail_module VARCHAR(255),
    fail_function VARCHAR(255),
    detailed_content TEXT
)
"""

# cursor.execute("SELECT * FROM mydb")
cursor.execute(create_table_query)
result = cursor.fetchall()
for table in result:
    print(table)
# 提交更改到数据库
mydb.commit()
# cursor.execute("CREATE DATABASE mydb")
cursor.close()
mydb.close()
