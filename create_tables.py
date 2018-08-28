from app import create_app
app = create_app ()

from app.models import db

if __name__ == '__main__':
    with app.app_context ():
        db.drop_all ()
        db.create_all ()
