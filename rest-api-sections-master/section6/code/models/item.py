from db import db
# A model is our internal representation of an entity(object), where as a resourse is an external representation of an entity


class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))    # stores = table name and .id is the column
    store = db.relationship('StoreModel')   # Only one store related to an item

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    # @classmethod is a way to accept request independant of the class object, by this the method could be called
    # without specifying the user object but rather the class object which makes it easier/generic calling the method
    # This classmethod makes us independant of the class name in the method (here ItemModel)
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()   # same as SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):                               # Insert or updating db
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
