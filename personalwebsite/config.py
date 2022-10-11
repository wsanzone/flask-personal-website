import os




class Config:
    SECRET_KEY = os.environ.get('SECRETKEY')
    
    MAIL_SERVER = 'smtp.googlemail.com'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAILUSERNAME')
    MAIL_PASSWORD = os.environ.get('EMAILKEY')