from db import db
# A model is our internal representation of an entity(object), where as a resourse is an external representation of an entity


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')       # relationship with ItemModel.
    # List of items since many items can belong to the same store
    # lazy=dynamic implies that the items object contains all items

    def __init__(self, name):
        self.name = name

    def json(self):
        # The self.items.all() retrieves all items in the table (initialized above with the lazy part)
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

    # @classmethod is a way to accept request independant of the class object, by this the method could be called
    # without specifying the user object but rather the class object which makes it easier/generic calling the method
    # This classmethod makes us independant of the class name in the method (here StoreModel)
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
