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


def dispContractorDetails():
    ls = []
    #function to display all items
    sql = "SELECT * FROM contractor"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        i = 1
        for row in results:
            ls.append(str(i)+".")
            ls.append("name")
            ls.append(str(row[0]))
            ls.append("house type")
            ls.append(str(row[1]))
            ls.append("locality")
            ls.append(str(row[2]))
            ls.append("price")
            ls.append(str(row[3]))
            i+=1
    except:
        print("unable to fetch data")
    return ls


def dispDealerDetails():
    ls =[]
    #function to display all items
    sql = "SELECT * FROM dealer"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        i = 1
        for row in results:
            ls.append(str(i)+".")
            ls.append("name")
            ls.append(str(row[0]))
            ls.append("item name")
            ls.append(str(row[1]))
            ls.append("stock")
            ls.append(str(row[2]))
            ls.append("price")
            ls.append(str(row[3]))
            i+=1
    except:
        print("unable to fetch data")
    return ls