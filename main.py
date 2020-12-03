import credential
import mysql.connector
import credential
import user




mydb = mysql.connector.connect(
  host="api.hphucs.me",
  user="cs300",
  password="Whitworth000",
  database="FinalProject"
)


#credential.createCredential(mydb,'user123','Usser123','user123@gmail.com')

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM CREDENTIAL")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# # test create account
# print("Creating a new account")
# while True:
#     username = input("Input new username: ")
#     password = input("New password: ")
#     email = input("Email: ")
#     #check if all 3 fields contain information
#     if username and password and email:
#         #exit while loop
#         break

# credential.createCredential(mydb, username, password, email)

# Test change password
# print("Creating a new account")
# while True:
#     username = input("Input username: ")
#     newPass = input("New password: ")
#     newEmail = input("New Email: ")
#     #check if all 3 fields contain information
#     if username and newPass and newEmail:
#         #exit while loop
#         break

# credential.changePassword(mydb, username, newPass)
# credential,credential.changeEmail(mydb, username, newEmail)



user.createAccount(mydb, "pcai225", "a", "b", "m", "a")


