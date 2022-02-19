import mysql.connector
from mysql.connector import Error
from mysql.connector import pooling
try:

    connection_pool = mysql.connector.pooling.MySQLConnectionPool(
        pool_name="pynative_pool",
        pool_size=5,
        pool_reset_session=True,
        host='localhost',
        user='root',
        password='123456',
        database='website')
    # print("Printing connection pool properties ")
    # print("Connection Pool Name - ", connection_pool.pool_name)
    # print("Connection Pool Size - ", connection_pool.pool_size)
   # Get connection object from a pool
    connection_object = connection_pool.get_connection()
    if connection_object.is_connected():
        db_Info = connection_object.get_server_info()
        # print("Connected to MySQL database using connection pool ... MySQL Server version on ", db_Info)
        mycursor = connection_object.cursor()
        # mycursor.execute("select database();")
        # record = mycursor.fetchone()
        # print("Your connected to - ", record)
except Error as e:
    print("Error while connecting to MySQL using Connection pool ", e)


# 註冊
def db_insert(**data):
    sql = ("INSERT INTO member"
           "(name,username,password)"
           "VALUES (%(name)s,%(username)s,%(password)s)")

    mycursor.execute(sql, data)
    connection_object.commit()


# 搜尋username是否有重複
def db_select(**data):
    query = "SELECT * FROM member WHERE "
    for key in data:
        query += f"{key}='{data[key]}' and "
    query = query[:-5]
    print(query)
    print(data)
    mycursor.execute(query)
    result = mycursor.fetchone()
    if result:
        # zip()合併list o rtuple/dict()轉成字典
        result = dict(zip(mycursor.column_names, result))
        print(result)
        return result
    else:
        return None


def db_updateName(**data):

    update = "UPDATE  member SET name = %s WHERE username = %s"
    value = (data['name'], data['username'])
    mycursor.execute(update, value)
    print(mycursor)
    connection_object.commit()
