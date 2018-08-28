from flask import Blueprint
from app import oauth2

bp = Blueprint ('auth', __name__, url_prefix = '/auth')

@bp.route ('/login', methods = ('GET', 'POST',))
def login ():
    return 'Login.'

@bp.route ('/logout', methods = ('GET',))
@oauth2.required
def logout ():
    return 'Logout.'
