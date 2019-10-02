from db import db
# A model is our internal representation of an entity(object), where as a resourse is an external representation of an entity

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):     # id not used since it is created automatically incrementally
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # @classmethod is a way to accept request independant of the class object, by this the method could be called
    # without specifying the user object but rather the class object which makes it easier/generic calling the methd
    # This classmethod makes us independant of the class name in the method (here UserModel)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
