from flask import render_template
from app import app



@app.route('/')
def index():

    #seed

    users = [
        {
            'id': 1,
            'firstname': 'Maximus',
            'lastname': 'Cruz',
            'middlename': 'Santos',
            'alias': 'Max',
        }, 
        {
            'id': 2,
            'firstname': 'Cherry Mae',
            'lastname': 'Cruz',
            'middlename': 'Santos',
            'alias': 'Cherry',
        }, 
        {
            'id': 3,
            'firstname': 'Juan Manuel',
            'lastname': 'Caldero',
            'middlename': 'Simon',
            'alias': 'Juan',
        }
    ]


    return render_template('index.html', title='HOME', users=users)

