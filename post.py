
def createPost(mydb,postid,username,content):
    mycursor = mydb.cursor()
    sql = "INSERT INTO POST (postid,username,content) VALUES (%s,%s,%s)"
    val = (postid,username,content)

    mycursor.execute(sql,val)
    mydb.commit()

