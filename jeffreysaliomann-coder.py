name = input("Enter your name:")
username = "Jeffrey Salioman"
password = "jeff321"
while True:
     print("\n{_______________________}")
     print("    LOGIN TO THE APP")
     print("--------------------------")
     print(f"Welcome, {name}!")
     print("1. Login")
     print("2. Change Password")
     print("3. Exit")
   

     choice = input("Enter your choice: ")

     if choice == "1":
        user = input("Username: ")
        passw = input("Password: ")
        if user == username and passw == password:
            print(f"Login Successful! Welcome, {name}!")
        else:
            print("Invalid Username or Password.")
     elif choice == "2":
        user = input("Enter Username: ")
        oldpass = input("Current Password: ")
        if user == username and oldpass == password:
            password = input("Enter New Password: ")
            print("Password Changed Successfully!")
        else:
            print("Incorrect Username or Password.")
     elif choice == "3":
        print(f"Goodbye, {name}! Thank you for using the app.")
        break
     else:
        print("Invalid Choice.")
