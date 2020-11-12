

def createAccount(mydb,username, Fname, Lname, Gender, DBirth, DateCreated):
    mycursor = mydb.cursor()
    sql = "INSERT INTO USER (username, Fname, Lname, Gender, DBirth, DateCreated) VALUES (%s, %s)"
