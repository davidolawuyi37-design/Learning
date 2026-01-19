import json
import os
from datetime import datetime


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
        return cls(
            data["name"],
            data["age"],
            data["contact"],
            data["membership_date"]
        )


class ChurchManager:
    def __init__(self, data_file="church_members.json"):
        self.data_file = data_file
        self.members = self.load_members()

    def load_members(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    return [ChurchMember.from_dict(m) for m in data]
            except json.JSONDecodeError:
                return []
        return []

    def save_members(self):
        with open(self.data_file, "w") as f:
            json.dump([m.to_dict() for m in self.members], f, indent=4)

    def add_member(self, name, age, contact, membership_date):
        # Phone number must be unique
        for member in self.members:
            if member.contact == contact:
                print("❌ A member with this phone number already exists.")
                return

        self.members.append(
            ChurchMember(name, age, contact, membership_date)
        )
        self.save_members()
        print("✅ Member added successfully.")

    def list_members(self):
        if not self.members:
            print("No members found.")
            return

        for i, member in enumerate(self.members, start=1):
            print(
                f"{i}. Name: {member.name}, "
                f"Age: {member.age}, "
                f"Phone: {member.contact}, "
                f"Membership Date: {member.membership_date}"
            )

    def find_member(self, name):
        found = False
        for member in self.members:
            if member.name.lower() == name.lower():
                print(
                    f"Name: {member.name}, "
                    f"Age: {member.age}, "
                    f"Phone: {member.contact}, "
                    f"Membership Date: {member.membership_date}"
                )
                found = True

        if not found:
            print("❌ No member found with that name.")


def main():
    manager = ChurchManager()

    while True:
        print("\nChurch Member Management App")
        print("1. Add Member")
        print("2. List Members")
        print("3. Find Member (by name)")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")

            try:
                age = int(input("Age: "))
            except ValueError:
                print("❌ Age must be a number.")
                continue

            contact = input("Phone Number: ")

            membership_date = input("Membership Date (YYYY-MM-DD): ")
            try:
                datetime.strptime(membership_date, "%Y-%m-%d")
            except ValueError:
                print("❌ Date format must be YYYY-MM-DD.")
                continue

            manager.add_member(name, age, contact, membership_date)

        elif choice == "2":
            manager.list_members()

        elif choice == "3":
            name = input("Enter name to search: ")
            manager.find_member(name)

        elif choice == "4":
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()
