from app import app
from extensions import db
from models import User

def fix_roles():
    with app.app_context():
        print("--- Updating Existing User Roles ---")

        # 1. CONVERT 'software_admin' TO AGENT (Worker)
        # As per your request: "change that software admin to software agent"
        worker = User.query.filter_by(email='shadowzone4200@gmail.com').first()
        if worker:
            worker.role = 'agent'
            worker.name = "Software Agent"
            print(f"✅ Converted {worker.email} to AGENT")
        else:
            print("⚠️ Could not find software_admin@admin.com")

        # 2. ENSURE THERE IS A MANAGER (Boss)
        # You need at least one manager to see "All Tickets"
        manager = User.query.filter_by(email='software_manager@admin.com').first()
        if manager:
            manager.role = 'manager'
            print(f"✅ ensured {manager.email} is MANAGER")
        else:
            print("ℹ️ No software_manager found. You might need to register one manually or use an existing admin email.")

        db.session.commit()
        print("--- Update Complete ---")

if __name__ == "__main__":
    fix_roles()