from flask import Flask, session
from oauth2client.contrib.flask_util import UserOAuth2
oauth2 = UserOAuth2 ()

import httplib2
import json

def create_app (config = 'config'):
    app = Flask (__name__, instance_relative_config = True)
    app.config.from_object (config)

    oauth2.init_app (app, scopes = ['email', 'profile'], authorize_callback = _callback)

    from app.models import db
    db.init_app (app)

    # Blueprints
    from app.aut import bp as aut; app.register_blueprint (aut)
    from app.tdb import bp as tdb; app.register_blueprint (tdb)

    # Default
    app.add_url_rule ('/', endpoint = 'auth.login')

    # Additional routes ...
    @app.route ('/hello')
    def hello ():
        return 'Hello Mike!'

    @app.route ('/session-dump')
    def session_dump ():
        if 'profile' in session.keys ():
            return json.dumps (session.get ('profile'))
        else:
            return 'Dump!'

    return app

def _callback (credentials):
    http = httplib2.Http ()
    credentials.authorize (http)
    resp, content = http.request ('https://www.googleapis.com/plus/v1/people/me')

    if resp.status != 200:
        return None
    else:
        session['profile'] = json.loads (content.decode ('utf-8'))

