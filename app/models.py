from app import db


class Register(db.Model):
    """Register Model"""
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), index=True, unique=True)
    lastname = db.Column(db.String(100), index=True, unique=True)
    middlename = db.Column(db.String(100), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    mobile = db.Column(db.Integer, unique=True)
    alias = db.Column(db.String(80), index=True, unique=True)

    def __repr__(self):
        """String representation of Register"""
        return f"FirstName: {self.firstname}"



