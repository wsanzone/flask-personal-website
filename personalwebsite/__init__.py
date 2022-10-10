from flask import Flask
from flask_mail import Mail # this package allows us to send an email when the contact form is filled out
from flask_sqlalchemy import SQLAlchemy # Package for our database ORM
from personalwebsite.config import Config
from flask_migrate import Migrate
import psycopg2, os



# Configure our database as a local file in the relative path called site.db

# Instantiate/Create the database
db = SQLAlchemy()
mail = Mail() # Instantiate our Mail object
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__) # Instantiate the app
    app.config.from_object(Config)
    # Imports all routes from the routes.py file
    url = os.environ.get('DATABASE')
    connection = psycopg2.connect(url, host='/tmp/')
    db.init_app(app)
    mail.init_app(app)
    #migrate.init_app(migrate)
    with app.app_context():
        db.create_all()

    from personalwebsite.contact.routes import contacts
    from personalwebsite.main.routes import main
    from personalwebsite.projects.routes import projects
    from personalwebsite.resume.routes import resume

    app.register_blueprint(contacts)
    app.register_blueprint(main)
    app.register_blueprint(projects)
    app.register_blueprint(resume)

    return app