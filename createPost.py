import post
import action
import mysql.connector


# def createPost(mydb, userID, postContent):
#     postID = post.createPost(mydb, userID, postContent)
#     action.createPost(mydb, userID, postID)




mydb = mysql.connector.connect(
    host="api.hphucs.me",
    user="cs300",
    password="Whitworth000",
    database="FinalProject"
)


post.createPost(mydb, "pcai22", "acb")