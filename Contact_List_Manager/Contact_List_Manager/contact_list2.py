contacts = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    contacts[name] = number
    print("✅ Contact added successfully\n")

def view_contacts():
    if not contacts:
        print("📭 No contacts found\n")
    else:
        print("📞 Contact List:")
        for name, number in contacts.items():
            print(f"Name: {name}, Phone: {number}")
        print()

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        new_number = input("Enter new phone number: ")
        contacts[name] = new_number
        print("✏️ Contact updated successfully\n")
    else:
        print("❌ Contact not found\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("🗑️ Contact deleted successfully\n")
    else:
        print("❌ Contact not found\n")

while True:
    print("📱 CONTACT MANAGER")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("👋 Goodbye!")
        break
    else:
        print("⚠️ Invalid choice\n")