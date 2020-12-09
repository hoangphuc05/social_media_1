def savePost(mydb,UserId,PostID,ActionID,Time):
    import mysql.connector
    mydb = mysql.connector.connect(
        host="api.hphucs.me",
        user="cs300",
        password="Whitworth000",
        database="FinalProject"
    )
    from datetime import datetime, date
    now = datetime.now()



    sql = "INSERT INTO ACTION (ActionID,UserName,PostID,Time,ActionDescription) VALUES (%s,%s,%s,%s,'saved post')"
    val = (ActionID,"1",PostID,now)
    mycursor = mydb.cursor()
    mycursor.execute(sql,val)
    mydb.commit()

savePost(0,0,"0","0",0)