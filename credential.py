
def createCredential(mydb, username, password, email):
    mycursor = mydb.cursor()
    sql = "INSERT INTO CREDENTIAL (UserName, Password, Email) VALUES (%s, %s, %s)"
    val = (username, password, email)

    mycursor.execute(sql, val)
    mydb.commit()

#change the password of the user
def changePassword(mydb, username, newPassword):
    mycuursor = mydb.cursor()
    sql = "UPDATE CREDENTIAL SET Password = %s WHERE UserName = %s"
    val = (newPassword, username)

    mycuursor.execute(sql, val)
    mydb.commit()

#change the email of the user
def changeEmail(mydb, username, newEmail):
    mycuursor = mydb.cursor()
    sql = "UPDATE CREDENTIAL SET Email = %s WHERE UserName = %s"
    val = (newEmail, username)

    mycuursor.execute(sql, val)
    mydb.commit()


