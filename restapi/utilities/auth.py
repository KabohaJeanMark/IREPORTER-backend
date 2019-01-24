from flask import jsonify
from functools import wraps
from flask_jwt_extended import get_jwt_identity
from restapi.models.user_models import Users


def admin_only(f):
    @wraps(f)
    def wrapper(*args, **kwargs):

        current_user = get_jwt_identity()
        user = Users().get_user(current_user['user_id'])
        admin = user['admin']
        if not admin:
            return jsonify({'message': 'Only the admin can access this route'}), 403
        return f(*args, **kwargs)

    return wrapper
