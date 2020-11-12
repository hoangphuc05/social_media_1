import credential
import mysql.connector




mydb = mysql.connector.connect(
  host="api.hphucs.me",
  user="cs300",
  password="Whitworth000",
  database="FinalProject"
)


credential.createCredential(mydb,'user123','Usser123','user123@gmail.com')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM CREDENTIAL")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



