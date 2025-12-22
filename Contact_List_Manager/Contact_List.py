Contacts = {}

def Add_Contact():
    Name = input("Enter Name: ")
    Phone = input("Enter Phone Number: ")
    Contacts[Phone] = Name
    print("Contact added sucessfully\n")

def View_Contacts():
    if not Contacts:
        print("No Contacts Found\n")
    else:
        print("Contact List:")
        for Phone, Name in Contacts.items():
            print(f"Name: {Name}, Phone: {Phone}")
        print()

def Update_Contact():
    Phone = input("Enter Phone Number To Update: ")
    if Phone in Contacts:
        New_Name = input("Enter New Name: ")
        Contacts[Phone] = New_Name
        print("Contact Updated Sucessfully\n")
    else:
        print("Contact Not Found\n")

def Delete_Contact():
    Phone = input("Enter Phone Number To Delete: ")
    if Phone in Contacts:
        del Contacts[Phone]
        print("Contact Deleted Successfully\n")
    else:
        print("Contact Not Found")
                                
while True:
                                     
    print("  CONTACT MANAGER")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    Choice = input("Choose An Option (1-5): ")

    if Choice == "1":
        Add_Contact()
    elif Choice == "2":
        View_Contacts()
    elif Choice == "3":
        Update_Contact()
    elif Choice == "4":
        Delete_Contact()
    elif Choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid Selection")
            