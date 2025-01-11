# simple data that allow user to 1.clear , 2.update 3. print data and 4. exit data base
# let create a Dictionaries{key : value}

people = {"Luffy" : "Fighter" , "Zoro" : "Sword Man" , "Nami" : "Navigator" , "Sanji" : "Cook"}

# let's create a intro function 

def intro(): 
    print("Welcome to the Data Base\n")
    print("To get Access, Enter the Password")
    enter_password()
# for password

def enter_password():
    password = "Nepal@123#"

    entry1 = input("Enter the Password: ")

    while True:
        if entry1 == password:
            print("Access Granted!")
            data_base()
            break
        else:
            print("Access Denied!")
            entry1 = input("Try Again: ")

def data_base():
    x = int(input("Choose:\n1.Clear The data base.\n2.Update the data base.\n3. print the data.\n4. Exit data base.\n"))
    try:
        if x == 1:
            people.clear()
            print("Data base Clear.")
        elif x == 2:
            update_dictionaries()

        elif x == 3:
            for key , value in people.items():
                print(f"{key}: {value}")
        elif x == 4:
            print("Exiticing the databse")
        else:
            print("Invalid choice.Please selecrt 1 , 2 , 3 and 4 only")

    except ValueError:
        print("Invalid input.Please enter the number")
    return True

def update_dictionaries():
    n = int(input("Number of data you want to add in your database: "))
    for i in range(n):
        name = input("Enter your name: ")
        role = input("Enter you role: ")

        people[name] = role

        print(f"New Update: {name} --> {role}")


    for key , value in people.items():
        print(f"{key}: {value}")

intro()








