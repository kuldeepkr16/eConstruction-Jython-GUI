from com.ziclix.python.sql import zxJDBC
import os
import sys
from java.util import Properties

#add jar to your class path, then import it
sys.path.append('/root/Desktop/mysql-connector-java-5.1.42.jar')
import com.mysql.jdbc.Driver as Driver
props = Properties()
props.put('user','root')
props.put('password','redhat')
mysqlConn = zxJDBC.connect(Driver().connect('jdbc:mysql://localhost/construction',props))
cursor = mysqlConn.cursor()

def updateDetails(name, itemName, stock, price):
    bit = False
    #execute SQL query using execute method
    sql = "INSERT INTO dealer VALUES('"+name+"','"+itemName+"','"+stock+"','"+price+"')"
    try:
        cursor.execute(sql)
        mysqlConn.commit()
        bit = True
    except:
        mysqlConn.rollback()
        bit = False
    return bit

def dispAllItems():
    #function to display all items
    sql = "SELECT * FROM dealer"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        count = 0
        for row in results:
            count+=1
            name = row[0]
            itemName = row[1]
            stock = row[2]
            price = row[3]
            print(str(count)+" : name=%s, item name=%s, stock=%s, price=%s" % (name,itemName,stock,price))
    except:
        print("unable to fetch data")
