contacts = []

while True:
    print("\n📒 Contact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    # ➕ Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")

        contact = {"name": name, "phone": phone}
        contacts.append(contact)

        print("✅ Contact added!")

    # 📜 View Contacts
    elif choice == "2":
        if not contacts:
            print("No contacts found.")
        else:
            for c in contacts:
                print(f"{c['name']} - {c['phone']}")

    # 🔍 Search Contact
    elif choice == "3":
        search = input("Enter name to search: ")
        found = False

        for c in contacts:
            if c["name"].lower() == search.lower():
                print(f"Found: {c['name']} - {c['phone']}")
                found = True

        if not found:
            print("❌ Contact not found")

    # ❌ Delete Contact
    elif choice == "4":
        name = input("Enter name to delete: ")

        for c in contacts:
            if c["name"].lower() == name.lower():
                contacts.remove(c)
                print("🗑️ Contact deleted!")
                break
        else:
            print("❌ Contact not found")

    # 🚪 Exit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")