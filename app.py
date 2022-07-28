from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, email


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET KEY'


#make the Form class
class UserForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    gender = StringField('gender')
    speciality = StringField('gender')
    submit = SubmitField('submit')



@app.route('/form', methods=['GET', 'POST'])
def form():
#the form will be submitted to the same route 
    form = UserForm()
    '''
    make the variables to None if you want to use it in the html 
    if name
        desplay somethin
    else
        display the form to put the name
    '''
    name=None
    email=None
    password=None
    gender=None
    speciality=None
#when the form submitted --> redirect to another route
    if form.validate_on_submit():
    
        name=form.name.data
        email=form.email.data
        password=form.password.data
        gender=form.gender.data
        speciality=form.speciality.data
        
        return redirect(url_for('somewhere'))

    return render_template('form.html', form=form, name=name, email=email)

@app.route('/somewhere')
def somewhere():

    return render_template('somewhere.html')