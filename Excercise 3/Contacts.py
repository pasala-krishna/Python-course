class Contact:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(f"Contact Found:\nName: {contact.name}\nEmail: {contact.email}\nPhone Number: {contact.phone_number}")
                return
        print(f"Contact {name} not found.")

# Example usage:
contact1 = Contact("Alice", "alice@example.com", "123-456-7890")
contact2 = Contact("Bob", "bob@example.com", "987-654-3210")

contact_list = ContactList()
contact_list.add_contact(contact1)
contact_list.add_contact(contact2)

contact_list.search_contact("Alice")
contact_list.search_contact("Eve")  # Searching for a non-existent contact

contact_list.delete_contact("Bob")
contact_list.search_contact("Bob")  # Searching for a deleted contact
