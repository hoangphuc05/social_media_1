from datetime import date

def createAccount(mydb,username, Fname, Lname, Gender, DBirth):
    #dateCreate = date.today()
    mycursor = mydb.cursor()
    sql = "INSERT INTO USER (username, Fname, Lname, Gender, DBirth) VALUES (%s, %s, %s, %s, '2000-1-1')"

    val = (username, Fname, Lname, Gender)

    mycursor.execute(sql, val)
    mydb.commit()
