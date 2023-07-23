from datetime import datetime
from gino import Gino

db = Gino()

class Data(db.Model):
    __tablename__ = 'data'

    name = db.Column(db.String())
    location = db.Column(db.String())
    contact_info = db.Column(db.String())
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

class Links(db.Model):
    __tablename__ = 'links'

    link = db.Column(db.String())
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)