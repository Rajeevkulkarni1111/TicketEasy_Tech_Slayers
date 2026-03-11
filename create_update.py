from app import app, db
from models import Ticket, User


def create_ticket():
    title = input("Enter ticket title: ")
    description = input("Enter ticket description: ")
    status = input("Enter ticket status: ")

    new_ticket = Ticket(title=title, description=description, status=status)

    db.session.add(new_ticket)
    db.session.commit()

    print("Ticket created successfully.")


def create_user():
    username = input("Enter username: ")
    email = input("Enter email: ")

    new_user = User(username=username, email=email)

    db.session.add(new_user)
    db.session.commit()

    print("User created successfully.")


def update_ticket():
    ticket_id = int(input("Enter Ticket ID to update: "))
    ticket = Ticket.query.get(ticket_id)

    if ticket:
        new_status = input("Enter new status: ")
        ticket.status = new_status

        db.session.commit()
        print("Ticket updated successfully.")
    else:
        print("Ticket not found.")


def update_user():
    user_id = int(input("Enter User ID to update: "))
    user = User.query.get(user_id)

    if user:
        new_email = input("Enter new email: ")
        user.email = new_email

        db.session.commit()
        print("User updated successfully.")
    else:
        print("User not found.")


with app.app_context():

    print("\nChoose Operation")
    print("1. Create Ticket")
    print("2. Create User")
    print("3. Update Ticket")
    print("4. Update User")

    choice = input("Enter choice: ")

    if choice == "1":
        create_ticket()

    elif choice == "2":
        create_user()

    elif choice == "3":
        update_ticket()

    elif choice == "4":
        update_user()

    else:
        print("Invalid choice")