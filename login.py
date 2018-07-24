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

def signIn(uname, passwd, userType):
    returnValue = False
    sql = "select name from users where uname='"+uname+"' and password = '"+ passwd +"' and usertype = '" +userType+"'" 
    cursor.execute(sql)
    data = cursor.fetchone()
    if data != None:
        print(data)
        returnValue = True
    else:
        print("Wrong Credentials!")
        returnValue = False
    return returnValue