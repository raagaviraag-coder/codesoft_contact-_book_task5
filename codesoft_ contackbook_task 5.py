import json
import os

FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add new contact
def add_contact(contacts):
    print("\n--- Add Contact ---")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!\n")

# View all contacts
def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.\n")
        return

    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")
    print()

# Search contact
def search_contact(contacts):
    print("\n--- Search Contact ---")
    query = input("Enter name or phone: ").lower()

    found = False
    for c in contacts:
        if query in c["name"].lower() or query in c["phone"]:
            print(f"\nName: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            found = True

    if not found:
        print("No matching contact found.\n")

# Update contact
def update_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to update: ")) - 1

        if 0 <= index < len(contacts):
            print("\nEnter new details (leave blank to keep old value):")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")

            if name:
                contacts[index]["name"] = name
            if phone:
                contacts[index]["phone"] = phone
            if email:
                contacts[index]["email"] = email
            if address:
                contacts[index]["address"] = address

            save_contacts(contacts)
            print("Contact updated successfully!\n")
        else:
            print("Invalid contact number!\n")
    except:
        print("Invalid input!\n")

# Delete contact
def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter contact number to delete: ")) - 1

        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            save_contacts(contacts)
            print(f"Deleted contact: {removed['name']}\n")
        else:
            print("Invalid contact number!\n")
    except:
        print("Invalid input!\n")

# Main menu
def main():
    contacts = load_contacts()

    while True:
        print("==== CONTACT MANAGEMENT ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

# Run program
if __name__ == "__main__":
    main()
