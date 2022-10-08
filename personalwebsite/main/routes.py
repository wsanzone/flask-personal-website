from flask import render_template
#from personalwebsite.models import Contact
#from personalwebsite.forms import ContactMeForm
from flask import Blueprint, current_app

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home") # SETTING THE HOME ROUTE
def home():
    return render_template('home.html') # RETURNS THE home.html TEMPLATE


@main.route("/about") # ROUTE FOR THE ABOUT PAGE
def about():
    return render_template('about.html', title='About') # RENDERS THE about.html TEMPLATE IN THE tempaltes folder