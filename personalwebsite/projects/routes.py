from flask import render_template
#from personalwebsite.models import Contact
#from personalwebsite.forms import ContactMeForm
from flask import Blueprint

projects = Blueprint('projects', __name__)

@projects.route('/projects', methods=['GET', 'POST']) # Route for a projects page
def projects_display():
    return render_template('projects.html', title='My Projects')

@projects.route('/airbnb_project', methods=['GET'])
def airbnb_project():
    return render_template('airbnb.html')