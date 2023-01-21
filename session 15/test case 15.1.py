# test case 15.1 DBOperations (insert, update, delete)
insert_query = "insert into city values(601,'6th of october city','90','2023-01-09 06:01:33')"
update_query = "update city set city='cairo' where city_id=1;"
delete_query = "delete from actor where actor_id=202"
import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root", passwd=1234, database="sakila")
    curs = con.cursor()
    curs.execute("insert_query")
    con.commit()
    for row in curs:
      print(row[0], row[1], row[2], row[3])
    con.close()

except:
    print("Connection Unsuccessful.....")

print("Finished..........")
