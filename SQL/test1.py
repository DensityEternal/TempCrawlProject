import pymysql
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="density",
    database="curvespace"
)
cursor=connection.cursor()
# sqlQuery = "select *from studentsystem"
# try:
#     cursor.execute(sqlQuery)
#     result = cursor.fetchall()
#     for record in result:
#         print(record)
# except Exception as e:
#     print("Excetion error:",e)
query = "update studentsystem set name='kristina' where id=1 "
try:
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    for record in result:
        print(record)
except Exception as e:
    print("Excetion error:",e)