from flask import Flask
from flask_mail import Mail # this package allows us to send an email when the contact form is filled out
from flask_sqlalchemy import SQLAlchemy # Package for our database ORM
from personalwebsite.config import Config


#app.config['SECRET_KEY'] = os.environ.get('SECRETKEY')
# Configure our database as a local file in the relative path called site.db
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# Instantiate/Create the database
db = SQLAlchemy()


#app.config['MAIL_SERVER'] = 'smtp.googlemail.com' # Setting the mail server to be gmail
#app.config['MAIL_PORT'] = 587 # Port for the mail server, got this from a video
#app.config['MAIL_USE_TLS'] = True # Not sure what this does, also from a tutorial
#app.config['MAIL_USERNAME'] = os.environ.get('EMAILUSERNAME') # Mail username to use, taken from environment variable for security
#app.config['MAIL_PASSWORD'] = os.environ.get('EMAILKEY') # Mail password for the email account, also used for security purposes
mail = Mail() # Instantiate our Mail object

def create_app(config_class=Config):
    app = Flask(__name__) # Instantiate the app
    app.config.from_object(Config)
    # Imports all routes from the routes.py file

    db.init_app(app)
    mail.init_app(app)

    from personalwebsite.contact.routes import contacts
    from personalwebsite.main.routes import main
    from personalwebsite.projects.routes import projects
    from personalwebsite.resume.routes import resume

    app.register_blueprint(contacts)
    app.register_blueprint(main)
    app.register_blueprint(projects)
    app.register_blueprint(resume)

    return app