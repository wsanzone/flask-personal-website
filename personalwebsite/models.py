#from datetime import datetime
from personalwebsite import db

class Contact(db.Model): #Creating a database model for the Contact form
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True) # Creating column for the ID
    name = db.Column(db.String(25), nullable=False) # Creating column for the person's name
    email = db.Column(db.String(120), unique=False, nullable=False) # Creating a column for the person's email
    subject = db.Column(db.String(40), nullable=False) # Creating a column for the subject line
    message = db.Column(db.Text, nullable=False) # Creating a column for the message

    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message

    def __repr__(self):
        return f"Event {subject}"