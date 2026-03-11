from app import app
from extensions import db
from models import User

def create_super_admin():
    with app.app_context():
        email = "rajeevkulkarni1111@gmail.com"
        user = User.query.filter_by(email=email).first()
        if user:
            print("Super Admin already exists.")
            return

        super_admin = User(email=email, name="CEO Super Admin", role="super_admin", verified=True)
        super_admin.set_password("321")
        
        db.session.add(super_admin)
        db.session.commit()
        print(f"SUCCESS: Super Admin created: {email}")

if __name__ == "__main__":
    create_super_admin()