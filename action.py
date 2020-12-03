
def createAction(mydb,ActionID,UserID,PostID,Time,ActionDescr):
    mycursor = mydb.cursor()
    sql = "INSERT INTO ACTION (ActionID,UserID,PostID,Time,ActionDescr) VALUES (%s,%s,%s,%s,%s)"
    val = (ActionID,UserID,PostID,Time,ActionDescr)

    mycursor.execute(sql,val)
    mydb.commit()