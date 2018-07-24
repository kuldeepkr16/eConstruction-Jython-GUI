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

#function to check user details
def chkUser(name):
    ls =[]
    sql = "SELECT * FROM users where uname = '"+name+"'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        i = 1
        for row in results:
            ls.append(str(i)+".")
            ls.append("name")
            ls.append(str(row[0]))
            ls.append("username")
            ls.append(str(row[1]))
            ls.append("userType")
            ls.append(str(row[3]))
            i+=1
    except:
        print("unable to fetch data")
    return ls

#function to return all users
def allUsers():
    ls = []
    sql = "SELECT * FROM users"
    try:
        cursor.execute(sql)
        results = list(cursor.fetchall())
        i = 1
        for row in results:
            ls.append(str(i)+".")
            ls.append("name")
            ls.append(str(row[0]))
            ls.append("username")
            ls.append(str(row[1]))
            ls.append("userType")
            ls.append(str(row[3]))
            i+=1
    except:
        print("unable to fetch data")  
    return ls