def addFollowerToList(mydb, AuthorFollowID, FollowerID):
    mycursor = mydb.cursor()
    sql = "INSERT INTO FOLLOWER (AuthorFollowID, FollowerID) VALUES (%s, %s)"
    val = (AuthorFollowID, FollowerID)

    mycursor.execute(sql, val)
    mydb.commit()

def deleteFollower(mydb, FollowerID):
    mycursor = mydb.cursor()
    sql = "DELETE FROM FOLLOWER WHERE FollowerID = %s"
    FollowerID = 'radom'
    mycursor.execute(sql, (FollowerID,))
    
    mydb.commit()

    



