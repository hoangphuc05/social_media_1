
def createPost(mydb,username,content):
    mycursor = mydb.cursor()
    sql = "INSERT INTO POST (username,content) VALUES (%s,%s)"
    val = (username,content)

    mycursor.execute(sql,val)
    mydb.commit()

