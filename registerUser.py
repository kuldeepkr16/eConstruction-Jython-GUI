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

def registerUserfunc(name, uname, passwd, usertype):
    bit = False
    #execute SQL query using execute method
    sql = "INSERT INTO users VALUES('"+name+"','"+uname+"','"+passwd+"','"+usertype+"')"
    try:
        cursor.execute(sql)
        mysqlConn.commit()
        bit = True
    except:
        mysqlConn.rollback()
        bit = False
    return bit