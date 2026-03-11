from app import app, db
from models import Ticket, User

def delete_ticket():
    ticket_id = int(input("Enter Ticket ID to delete: "))
    ticket = Ticket.query.get(ticket_id)

    if ticket:
        db.session.delete(ticket)
        db.session.commit()
        print("Ticket deleted successfully.")
    else:
        print("Ticket not found.")


def delete_user():
    user_id = int(input("Enter User ID to delete: "))
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        print("User deleted successfully.")
    else:
        print("User not found.")


def view_tickets():
    tickets = Ticket.query.all()
    for t in tickets:
        print(t.id, t.title, t.status)


def view_users():
    users = User.query.all()
    for u in users:
        print(u.id, u.username, u.email)


with app.app_context():

    print("\nChoose Operation")
    print("1. Delete Ticket")
    print("2. Delete User")
    print("3. View Tickets")
    print("4. View Users")

    choice = input("Enter choice: ")

    if choice == "1":
        delete_ticket()

    elif choice == "2":
        delete_user()

    elif choice == "3":
        view_tickets()

    elif choice == "4":
        view_users()

    else:
        print("Invalid choice")