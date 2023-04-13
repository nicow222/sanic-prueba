from bson.objectid import ObjectId
from validate_email import validate_email

class Monguito:
    def __init__(self, name):
        self._id = ObjectId()
        self.name = name

    @classmethod
    def from_dict(cls, user_dict):
        user = cls(
            user_dict["name"])
        user._id = ObjectId(user_dict["_id"])
        return user

    def to_dict(self):
        return {
            '_id': str(self._id),
            'name': self.name
        }
    
    def validate(self):
        errors = {}
        if not self.name:
            errors['name'] = 'El Campo es requerido'
        
        return errors