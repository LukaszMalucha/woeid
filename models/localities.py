from db import db


class LocalitiesModel(db.Model):
    __tablename__ = 'localities'
    id = db.Column('id', db.Integer, primary_key=True)
    locality = db.Column('locality', db.Unicode)
    area = db.Column('area', db.Unicode)
    country = db.Column('country', db.Unicode)
    woeid = db.Column('woeid', db.Unicode)

    def __init__(self, locality, area, country, woeid):
        self.locality = locality
        self.area = area
        self.country = country
        self.woeid = woeid

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_columns(cls):
        return LocalitiesModel.__table__.columns.keys()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def delete_by_weoid(cls, weoid):
        tweets = cls.query.filter_by(weoid=weoid).delete()
        db.session.commit()

    @classmethod
    def find_by_locality(cls, locality):
        return cls.query.filter_by(locality=locality).all()

