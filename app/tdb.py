from flask import Blueprint, json, session, abort
from app.models import (
    db,
    Parent,
    Child,
)

bp = Blueprint ('tdb', __name__)

@bp.route ('/', methods = ('GET',))
def index ():
    p = Parent.query.first ()
    if p:
        p.ema = 'updated@somewhere.com'

        try:
            db.session.commit ()
            return json.jsonify (p.serialize ())

        except Exception as e:
            logging.error (e.__class__.__name__)
            db.session.rollback ()
            abort (500, 'Error. Something bad happened.')

    else:
        p = Parent (ema = 'a@somewhere.com', nam = 'Andy Testing Parent')
        p.children.append (Child (nam = 'Mary Testing Child'))
        p.children.append (Child (nam = 'Jane Testing Child'))
        p.children.append (Child (nam = 'Sara Testing Child'))

        try:
            db.session.add (p)
            db.session.commit ()
            return json.jsonify (p.serialize ())

        except Exception as e:
            logging.error (e.__class__.__name__)
            db.session.rollback ()
            abort (500, 'Error. Something bad happened.')


@bp.route ('/del', methods = ('GET',))
def dd ():
    p = Parent.query.first ()
    if p:
        try:
            db.session.delete (p)
            db.session.commit ()
            return 'Done.'

        except Exception as e:
            print (e)
            logging.error (e.__class__.__name__)
            db.session.rollback ()
            abort (500, 'Error. Something bad happened.')
    else:
        return 'N/A'

@bp.route ('/rst', methods = ('GET',))
def reset ():
    session['k'] = None
    db.drop_all ()
    db.create_all ()
    return 'Ok.'

@bp.route ('/ss', methods = ('GET',))
def ss ():
    session['k'] = 'v'
    return session['k']

@bp.route ('/sg', methods = ('GET',))
def sg ():
    return session.get ('k', 'Err.')



