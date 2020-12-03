

def createAccount(mydb,username, Fname, Lname, Gender, DBirth, DateCreated):
    mycursor = mydb.cursor()
    sql = "INSERT INTO USER (username, Fname, Lname, Gender, DBirth, DateCreated) VALUES (%s, %s, %s, %s, %s, %s)"

    val = (username, Fname, Lname, Gender, DBirth, DateCreated)

    mycursor.execute(sql, val)
    mydb.commit()
