import hashlib

def signup():
    user_name = input("enter username: ")
    password = input("creat password: ")
    confirming_password = input("Confirm your password: ")
    if confirming_password == password:
        i = confirming_password.encode()
        hash1 = hashlib.md5(i).hexdigest()
        with open("credentials.txt", "w") as c:
             c.write(user_name + "\n")
             c.write(hash1)
        c.close()
        print("You have registered successfully!")
    else:
        print("Oops somethings wrong! \n")


def login():
    user_name = input("Enter username: ")
    password = input("Enter password: ")
    auth = password.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if user_name == stored_email and auth_hash == stored_pwd:
         print("Logged in Successfully!")
         print("~"*30)
    else:
         print("Login failed! \n")


while 1:
    print("********** Welcome **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("****** please fill the following: ******")
        signup()
        print("******thanks****** \n please login next")
    elif choice == 2:
        print("****** welcome back ******")
        login()
        import theGame
        
    elif choice == 3:
        print("******** goodbye ********")
        break
    else:
        print("Wrong Choice!")
