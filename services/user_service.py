from repositories.user_repository import (create_user, read_users, read_user,
                                           update_user, delete_user, read_user_email)
from models.user import User


def create_new_user(name, email, password):
    new_user = User(name, email, password)
    return create_user(new_user)


def get_all_users():
    return read_users()


def get_user_by_email(user_id):
    return read_user_email(user_id)

def get_user_by_id(user_id):
    return read_user(user_id)


def update_user_by_id(user_id, name, email, password):
    updated_user = User(email, password, name)
    return update_user(user_id, updated_user)


def delete_user_by_id(user_id):
    return delete_user(user_id)