import json
import os

class ChurchMember:
    def __init__(self, name, age, contact, membership_date):
        self.name = name
        self.age = age
        self.contact = contact
        self.membership_date = membership_date

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "contact": self.contact,
            "membership_date": self.membership_date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["contact"], data["membership_date"])

class ChurchManager:
    def __init__(self, data_file="church_members.json"):
        self.data_file = data_file
        self.members = self.load_members()

    def load_members(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
                return [ChurchMember.from_dict(member) for member in data]
        return []

    def save_members(self):
        with open(self.data_file, "w") as f:
            json.dump([member.to_dict() for member in self.members], f, indent=4)

    def add_member(self, name, age, contact, membership_date):
        member = ChurchMember(name, age, contact, membership_date)
        self.members.append(member)
        self.save_members()
        print(f"Added member: {name}")

    def list_members(self):
        if not self.members:
            print("No members found.")
            return
        for member in self.members:
            print(f"Name: {member.name}, Age: {member.age}, Contact: {member.contact}, Membership Date: {member.membership_date}")

    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                print(f"Found: Name: {member.name}, Age: {member.age}, Contact: {member.contact}, Membership Date: {member.membership_date}")
                return
        print("Member not found.")

def main():
    manager = ChurchManager()
    while True:
        print("\nChurch Member Management App")
        print("1. Add Member")
        print("2. List Members")
        print("3. Find Member")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            contact = input("Contact: ")
            membership_date = input("Membership Date (YYYY-MM-DD): ")
            manager.add_member(name, age, contact, membership_date)
        elif choice == "2":
            manager.list_members()
        elif choice == "3":
            name = input("Name to find: ")
            manager.find_member(name)
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()