
def createCredential(mydb, username, password, email):
    mycursor = mydb.cursor()
    sql = "INSERT INTO CREDENTIAL (UserName, Password, Email) VALUES (%s, %s, %s)"
    val = (username, password, email)

    mycursor.execute(sql, val)
    mydb.commit()



