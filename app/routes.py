from flask import render_template, redirect, flash, url_for,request
from app.forms import RegisterForm
from app import db
from app.models import Register
from app import app



@app.route('/')
@app.route('/index')
def index():

    users = Register.query.all()

    form = RegisterForm()

    #seed
    # users = [
    #     {
    #         'id': 1,
    #         'firstname': 'Maximus',
    #         'lastname': 'Cruz',
    #         'middlename': 'Santos',
    #         'alias': 'Max',
    #     }, 
    #     {
    #         'id': 2,
    #         'firstname': 'Cherry Mae',
    #         'lastname': 'Cruz',
    #         'middlename': 'Santos',
    #         'alias': 'Cherry',
    #     }, 
    #     {
    #         'id': 3,
    #         'firstname': 'Juan Manuel',
    #         'lastname': 'Caldero',
    #         'middlename': 'Simon',
    #         'alias': 'Juan',
    #     }
    # ]

    return render_template('index.html', title='HOME', users=users, form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()
    
    if form.validate_on_submit():

        resident = Register(firstname=form.firstname.data, lastname=form.lastname.data, middlename=form.middlename.data, email=form.email.data, mobile=form.mobile.data, alias=form.alias.data)
        
        db.session.add(resident)
        db.session.commit()
        flash("Created")
        return redirect(url_for('index'))


    return render_template('index.html', form=form)



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    error = None

    if request.method != 'POST':

        error = "Error unable to process"

    else:

        user = Register.query.get_or_404(id)

        form = RegisterForm()

        user.firstname = form.firstname.data
        user.lastname = form.lastname.data
        user.middlename = form.middlename.data
        user.email = form.email.data
        user.mobile = form.mobile.data
        user.alias = form.alias.data

        db.session.commit()
        flash("Successfully Updated")
        return redirect(url_for('index'))

    return render_template('index.html', error=error)
    



@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):

    user = Register.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()
    flash("Successfully Deleted!")
    return redirect(url_for('index'))