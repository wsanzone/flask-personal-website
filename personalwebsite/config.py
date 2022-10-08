import os




class Config:
    SECRET_KEY = os.environ.get('SECRETKEY')
    
  #  SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAILUSERNAME')
    MAIL_PASSWORD = os.environ.get('EMAILKEY')