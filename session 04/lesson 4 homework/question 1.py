def accept_login(user,username,password):
    if username in user and user[username] == password:
        return True
    else:
        return False



users = {"user1":"password1","user2":"password2","user3":"password3"}
if accept_login(users,input("nhap username "),input("nhap password ")):
    print("login successful!")
else:
    print("login failed...")

