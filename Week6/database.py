import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='website'
)
mycursor= mydb.cursor()
#註冊
def db_insert(**data):
    sql=("INSERT INTO member"
         "(name,username,password)"
         "VALUES (%(name)s,%(username)s,%(password)s)")

    mycursor.execute(sql,data)
    mydb.commit()
   
#搜尋username是否有重複   
def db_select(**data):
    query = ("SELECT * FROM member WHERE username=%(username)s")
    mycursor.execute(query,data)
    result =mycursor.fetchone() #fetchone沒有值返回None,fetchall則返回()
    return result


#檢查帳號(username)密碼(password)是否有重複  
def db_check(**data):
    query = ("SELECT * FROM member WHERE username=%(username)s AND password=%(password)s")
    mycursor.execute(query,data)
    result =mycursor.fetchone()
    return result

 


