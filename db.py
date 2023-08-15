import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'bfd4f4fd',
    password = 'Cab#22se',
    database = 'bfd4f4fd'
)

#creating connection
with connection.cursor() as cursor:
    # Test the database connection by executing a simple query
    cursor.execute("select * from ecommerce")
    result = cursor.fetchone()
    print("Connection to the db successful!")
    print("Result: ", result)

    # Check if the 'ecommerce' table exists
    cursor.execute("show tables like 'ecommerce'")
    table_exists = bool(cursor.fetchone())
    if table_exists:
        print("'ecommerce' table exists!")
    else:
        print("'ecommerce' table does not exist!!")
connection.commit()
connection.close()
