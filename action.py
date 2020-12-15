
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
def savePost(mydb,UserId,PostID):

    mycursor = mydb.cursor()
    Time = datetime.now()
    sql = "INSERT INTO ACTION (UserName,PostID,Time,ActionDescription) VALUES (%s,%s,%s,'saved post')"
    val = (UserId,PostID,Time)

    mycursor.execute(sql,val)
    mydb.commit()

def checkSave(mydb, UserID, PostID):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM ACTION WHERE UserName = %s and PostID = %s and ActionDescription = 'saved post'"
    val = (UserID, PostID)
    mycursor.execute(sql, val)
    
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        return True
    else:
        return False

def unsave(mydb, UserID, PostID):
    mycursor = mydb.cursor()
    sql = "DELETE FROM ACTION WHERE UserName = %s and PostID = %s and ActionDescription = 'saved post'"
    val = (UserID,PostID)

    mycursor.execute(sql,val)
    mydb.commit()
    return True 

#Like a Post
def likePost(mydb, UserID, PostID):
    mycursor = mydb.cursor()
    Time = datetime.now()
    sql = "INSERT INTO ACTION (UserName,PostID,Time,ActionDescription) VALUES (%s,%s,%s,'like post')"
    val = (UserID,PostID,Time)

    mycursor.execute(sql,val)
    mydb.commit()

def checkLike(mydb, UserID, PostID):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM ACTION WHERE UserName = %s and PostID = %s and ActionDescription = 'like post'"
    val = (UserID, PostID)
    mycursor.execute(sql, val)
    
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        return True
    else:
        return False

def unlike(mydb, UserID, PostID):
    mycursor = mydb.cursor()
    Time = datetime.now()
    sql = "DELETE FROM ACTION WHERE UserName = %s and PostID = %s and ActionDescription = 'like post'"
    val = (UserID,PostID)

    mycursor.execute(sql,val)
    mydb.commit()
    return True 


def createPost(mydb, UserID, PostID):
    createAction(mydb, UserID, PostID, "Create post")





