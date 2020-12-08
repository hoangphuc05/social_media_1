
#create a action
def createAction(mydb,ActionID,UserID,PostID,Time,ActionDescr):
    mycursor = mydb.cursor()
    sql = "INSERT INTO ACTION (ActionID,UserID,PostID,Time,ActionDescr) VALUES (%s,%s,%s,%s,%s)"
    val = (ActionID,UserID,PostID,Time,ActionDescr)

    mycursor.execute(sql,val)
    mydb.commit()

#Save a Post
def savePost(mydb,UserId,PostID,ActionID,Time)
    mycursor = my.cursor()
    sql = "INSERT INTO ACTION (ActionID,UserID,PostID,Time,ActionDescr) VALUES (%s,%s,%s,%s,'saved post')"
    val = (ActionID,UserID,PostID,Time,ActionDescr)

    mycursor.execute(sql,val)
    mydb.commit()



