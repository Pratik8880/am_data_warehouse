from app import app
from models import db

with app.app_context():
    db.create_all()         # to create all tables from models.py
    print("✅ Tables created successfully in the database.")