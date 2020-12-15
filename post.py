import action


def createPost(mydb,username,content):
    mycursor = mydb.cursor()
    sql = "INSERT INTO POST (username,content) VALUES (%s,%s)"
    val = (username,content)

    mycursor.execute(sql,val)
    mydb.commit()

    postID =  mycursor.lastrowid
    action.createPost(mydb, username, postID)


def getAllUserPost(mydb, username):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM POST WHERE UserName = %s"
    val = (username, )

    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    return myresult

#Count Likes
def countLikes(mydb, PostID, ActionID):
    mycursor = mydb.cursor()
    sql = "SELECT COUNT(A.PostID) FROM ACTION as A WHERE A.ActionDescription = 'like post' AND A.PostID = %s"
    val = (PostID,)

    mycursor.execute(sql,val)

    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return 0
    else:
        return myresult[0][0]
        

def getFollowerPosts(mydb, username, index = 0):
    # SELECT * from POST P
    # WHERE P.UserName IN
    # 	(SELECT FollowerID FROM FOLLOWER as F
    # 	WHERE F.AuthorFollowID = 'nhatminh')
    # LIMIT 0,1;
    mycursor = mydb.cursor()
    sql = '''SELECT * from POST P
        WHERE P.UserName IN
            (SELECT FollowerID FROM FOLLOWER as F
            WHERE F.AuthorFollowID = %s)
        LIMIT %s,1;
        '''
    val = (username,index)

    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return (0,0,0)
    else:
        return myresult[0]

def countVisiblePost(mydb, username):
    mycursor = mydb.cursor()
    sql = '''SELECT COUNT(P.ID) from POST P
        WHERE P.UserName IN
            (SELECT FollowerID FROM FOLLOWER as F
            WHERE F.AuthorFollowID = %s);
        '''
    val = (username,)

    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return 0
    else:
        return myresult[0][0]

    
