from app import db, app
from app.models import User

with app.app_context():
    db.create_all()

