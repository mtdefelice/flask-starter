from flask_sqlalchemy import SQLAlchemy
import json
import datetime

db = SQLAlchemy ()

class Parent (db.Model):
    __tablename__ = 'parent'

    pid = db.Column (db.Integer, primary_key = True)
    ema = db.Column (db.String (255), nullable = False, unique = True)
    nam = db.Column (db.String (255), nullable = False)
    tim = db.Column (db.DateTime, default = db.func.now (), onupdate = db.func.now ())

    children = db.relationship ('Child', backref = 'parent', lazy = True, cascade = 'all, delete-orphan')

    def serialize (self):
        return {
            'pid': self.pid,
            'ema': self.ema,
            'nam': self.nam,
            'tim': int ((self.tim - datetime.datetime (1970, 1, 1)).total_seconds ()),
            'children': [ a.serialize () for a in self.children ],
        }

    def __repr__ (self):
        return f'<Parent {self.name!r}>'


class Child (db.Model):
    __tablename__ = 'child'

    cid = db.Column (db.Integer, primary_key = True)
    nam = db.Column (db.String (255), nullable = False)
    tim = db.Column (db.DateTime, default = db.func.now (), onupdate = db.func.now ())

    parent_pid = db.Column(db.Integer, db.ForeignKey ('parent.pid'), nullable = False)
    
    def serialize (self):
        return {
            'cid': self.cid,
            'nam': self.nam,
            'tim': int ((self.tim - datetime.datetime (1970, 1, 1)).total_seconds ()),
        }

    def __repr__ (self):
        return f'<Child {self.name!r}>'

