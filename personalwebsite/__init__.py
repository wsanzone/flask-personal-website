from flask import Flask
from flask_mail import Mail # this package allows us to send an email when the contact form is filled out
from flask_sqlalchemy import SQLAlchemy # Package for our database ORM
from personalwebsite.config import Config # Imports the config class from the config.py file
from flask_migrate import Migrate
import psycopg2, os




# Instantiate/Create the database
db = SQLAlchemy()
mail = Mail() # Instantiate our Mail object
migrate = Migrate() # Instantiate our migrate object, this is not really used

def create_app(config_class=Config):
    app = Flask(__name__) # Instantiate the app
    app.config.from_object(Config) # Imports our environment variables
    # Imports all routes from the routes.py file
    url = os.environ.get('DATABASE') # Gets the database connection string from the environment variable
    conn = psycopg2.connect(url) # Connecting to the database
    db.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        db.create_all()

    # Importing the routes for the website #
    from personalwebsite.contact.routes import contacts 
    from personalwebsite.main.routes import main
    from personalwebsite.projects.routes import projects
    from personalwebsite.resume.routes import resume

    # Registering the blueprints for the app #
    app.register_blueprint(contacts)
    app.register_blueprint(main)
    app.register_blueprint(projects)
    app.register_blueprint(resume)

    return app