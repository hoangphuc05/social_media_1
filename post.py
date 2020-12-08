
def createPost(mydb,username,content):
    mycursor = mydb.cursor()
    sql = "INSERT INTO POST (username,content) VALUES (%s,%s)"
    val = (username,content)

    mycursor.execute(sql,val)
    mydb.commit()

def getAllUserPost(mydb, username):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM POST WHERE UserName = %s"
    val = (username, )

    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    return myresult
