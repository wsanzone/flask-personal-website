#from datetime import datetime
from personalwebsite import db

class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    subject = db.Column(db.String(40), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def __repr__(self):
        return f"Event {subject}"