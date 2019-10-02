from flask_restful import Resource
from models.store import StoreModel
# models.store is the path to the store model class


# A folder is a package in python, here resource folder. That requires a __init__ file to tell python it is a package
# In python 3.5 __init__ i s not needed but older versions require an init file
# A resource are things that the api responds with when requested by a client
# An api deals with resources much like object oriented programming

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
