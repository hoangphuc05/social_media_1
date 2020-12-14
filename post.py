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
    sql = "SELECT A.PostID, A.UserName FROM ACTION as A WHERE A.ActionDescription = 'like post' AND A.PostID = %s"
    val = (PostID,)

    mycursor.execute(sql,val)

    myresult = mycursor.fetchall()
    for likes in myresult:
        print (likes)
    print(len(myresult))
        

def getFollowerPosts(mydb, username, index = 0):
    # SELECT * from POST P
    # WHERE P.UserName IN
    # 	(SELECT FollowerID FROM FOLLOWER as F
    # 	WHERE F.AuthorFollowID = 'nhatminh')
    # LIMIT 0,1;
    mycursor = mydb.cursor()
    sql = '''
        SELECT * from POST P
        WHERE P.UserName IN
            (SELECT FollowerID FROM FOLLOWER as F
            WHERE F.AuthorFollowID = %s)
        LIMIT %s,1;
        '''
    val = (username,index)

    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return myresult[0]

    
