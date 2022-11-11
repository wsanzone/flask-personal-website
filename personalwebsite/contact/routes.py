from flask import render_template, url_for, flash, redirect, current_app
from personalwebsite import mail, db
from personalwebsite.models import Contact
from personalwebsite.contact.forms import ContactMeForm
from flask_mail import Message
from flask import Blueprint

contacts = Blueprint('contact', __name__)

@contacts.route('/contactme', methods=['GET', 'POST']) # ROUTE FOR CONTACT ME PAGE AND SUBSEQUENT FORM
def contactme():
    form = ContactMeForm() # INSTANTIATES THE FORM FROM forms.py
    if form.validate_on_submit(): # IF THE FORM IS VALIDATED WHEN SUBMITTED (NO ERRORS)

        # CREATING AN INSTANCE OF OUR Contact class from models.py, setting variables to the form data
        contact_data = Contact(name=form.name.data, email=form.email.data, subject=form.subject.data,
                                message=form.message.data)
        db.session.add(contact_data) # ADDS OUR CLASS INFORMATION TO THE DATABASE
        db.session.commit() # COMMITS THIS DATA TO THE DATABASE
    
        def send_email(input): # FUNCTION TO SEND AN EMAIL WHEN THE CONTACT FORM IS FILLED OUT

            # MSG VARIABLE THAT HOLDS A GENERIC TITLE AND SENDER/RECIPIENT
            msg = Message('Someone has Contacted You', sender='wsanzoneds@gmail.com', recipients=['wsanzoneds@gmail.com'])
            msg.body = f'''
Name: {input.name}
Email: {input.email}
Subject: {input.subject}
Message: {input.message}
'''
            mail.send(msg)
        send_email(contact_data)
        flash('Thanks for contacting me!', 'success') # MESSAGE TO DISPLAY ONLY WHEN SUCCESSFUL
        return redirect(url_for('main.home')) # BRINGS YOU BACK TO THE HOMEPAGE
    else: # IF THE FORM SUBMISSION WAS NOT SUCCESSFUL
        return render_template('contact.html', form=form) # BRINGS YOU BACK TO THE SAME PAGE
        flash('Something went wrong, please try again.', 'warning') # WARNING MESSAGE THAT IS SHOWN IF CONDITION IS MET