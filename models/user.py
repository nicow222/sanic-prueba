from bson.objectid import ObjectId
from validate_email import validate_email

class User:
    def __init__(self, email, password, name=None):
        self._id = ObjectId()
        self.email = email
        self.password = password
        self.name = name

    @classmethod
    def from_dict(cls, user_dict):
        user = cls(user_dict["email"], user_dict["password"], user_dict["name"])
        user._id = ObjectId(user_dict["_id"])
        return user

    def to_dict(self):
        return {
            '_id': str(self._id),
            'email': self.email,
            'password': self.password,
            'name': self.name
        }

    def validate(self):
        errors = {}
        if not self.email:
            errors['email'] = 'El Campo es requerido'
        elif not validate_email(self.email):
            errors['email'] = 'Formato invalido'
        if not self.password:
            errors['password'] = 'El Campo es requerido'
        
        return errors