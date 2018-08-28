from flask import Blueprint, session, request, redirect
from app import oauth2

bp = Blueprint ('auth', __name__, url_prefix = '/auth')

@bp.route ('/login', methods = ('GET', 'POST',))
@oauth2.required
def login ():
    return 'Login.'

@bp.route ('/logout', methods = ('GET',))
def logout ():
    if 'profile' in session:
        del session['profile']
        session.modified = True

    oauth2.storage.delete ()

    return redirect (request.referrer or '/')
