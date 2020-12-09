
#create a action
def createAction(mydb,ActionID,UserID,PostID,Time,ActionDescr):
    mycursor = mydb.cursor()
    sql = "INSERT INTO ACTION (ActionID,UserID,PostID,Time,ActionDescr) VALUES (%s,%s,%s,%s,%s)"
    val = (ActionID,UserID,PostID,Time,ActionDescr)

    mycursor.execute(sql,val)
    mydb.commit()

#Save a Post
def savePost(mydb,UserId,PostID,ActionID,Time):
    mycursor = mydb.cursor()
    sql = "INSERT INTO ACTION (ActionID,UserID,PostID,Time,ActionDescr) VALUES (%s,%s,%s,%s,'saved post')"
    val = (ActionID,UserID,PostID,Time,ActionDescr)

    mycursor.execute(sql,val)
    mydb.commit()

#Like a Post
def likePost(mydb, UserID, PostID, ActionID):
    mycursor = mydb.cursor()
    sql = "INSERT INTO ACTION (ActionID,UserID,PostID,Time,ActionDescr) VALUES (%s,%s,%s,%s,'like post')"
    val = (ActionID,UserID,PostID,Time)

    mycursor.execute(sql,val)
    mydb.commit()




