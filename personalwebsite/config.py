import os



# A class to store all of our environment variables #
class Config:
    SECRET_KEY = os.environ.get('SECRETKEY')
    
    MAIL_SERVER = 'smtp.googlemail.com' # Gmail server
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE') # DigitalOcean PostgreSQL database connection string
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Removes errors when running the app locally
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAILUSERNAME') # email username for contact requests to be sent to
    MAIL_PASSWORD = os.environ.get('EMAILKEY') # email key so the contact messages can be sent