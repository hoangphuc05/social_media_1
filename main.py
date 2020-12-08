import credential
import mysql.connector
import credential
import user
import post
import follower




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



# post.createPost(mydb, "pcai22","This is the first post")


# print(credential.checkCredential(mydb, "pcai22", "Whitworth123"))

### Testing main program
makeAccount = input("Do you want to make a new account?")
if makeAccount == "y":
    newUserName = input("Your new username: ")
    newPassWord = input("Your password")
    Email = input("Your email: ")
    Fname = input("Fname: ")
    Lname = input("Lname: ")
    Gender = input("Gender: ")

    #create a new credential
    credential.createCredential(mydb, newUserName, newPassWord, Email)

    #creat user profile
    user.createAccount(mydb, newUserName, Fname, Lname, Gender, 0)

#login part
print("Login information")
username = input("Your username: ")
password = input("Your password: ")

while not credential.checkCredential(mydb, username, password):
    print("Login Failed, please try again!")
    username = input("Your username: ")
    password = input("Your password: ")

print("Login success!")

#print all information
print("This is your account information")
user.getAccount(mydb, username)

#get all follower
print("This is the list of people you are following:")
#follower.

print("Please create a post")
postContent = input("Content in the post: ")
post.createPost(mydb, username, postContent)

# get all the post:
print("These are all post from you:")
print( post.getAllUserPost(mydb, username))

