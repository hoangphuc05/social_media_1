
from datetime import datetime
#create a action
def createAction(mydb,UserID,PostID,ActionDescr):
    mycursor = mydb.cursor()
    Time = datetime.now()
    sql = "INSERT INTO ACTION (UserName,PostID,Time,ActionDescription) VALUES (%s,%s,%s,%s)"
    val = (UserID,PostID,Time,ActionDescr)

    mycursor.execute(sql,val)
    mydb.commit()

#Save a Post
def savePost(mydb,UserId,PostID,ActionID):

    mycursor = mydb.cursor()
    Time = datetime.now()
    sql = "INSERT INTO ACTION (ActionID,UserName,PostID,Time,ActionDescription) VALUES (%s,%s,%s,%s,'saved post')"
    val = (ActionID,UserId,PostID,Time)

    mycursor.execute(sql,val)
    mydb.commit()

#Like a Post
def likePost(mydb, UserID, PostID):
    mycursor = mydb.cursor()
    Time = datetime.now()
    sql = "INSERT INTO ACTION (UserName,PostID,Time,ActionDescription) VALUES (%s,%s,%s,'like post')"
    val = (UserID,PostID,Time)

    mycursor.execute(sql,val)
    mydb.commit()

def createPost(mydb, UserID, PostID):
    createAction(mydb, UserID, PostID, "Create post")





