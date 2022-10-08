from flask import render_template
#from personalwebsite.models import Contact
#from personalwebsite.forms import ContactMeForm
from flask import Blueprint

resume = Blueprint('resume', __name__)

# ADDING A ROUTE FOR THE RESUME PAGE #
@resume.route('/resume', methods=['GET'])
def resume_display():
    return render_template('resume.html') # RETURNS THE RESUME.HTML FILE IN THE WEBSITE