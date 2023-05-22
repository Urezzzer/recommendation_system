from app import db
from dataclasses import dataclass


class Groups(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.String(120), nullable=True)
    category_1 = db.Column(db.String(120), nullable=True)
    category_2 = db.Column(db.String(120), nullable=True)
    name = db.Column(db.String(120), nullable=True)
    district = db.Column(db.String(120), nullable=True)
    region = db.Column(db.String(120), nullable=True)
    street = db.Column(db.String(120), nullable=True)
    home = db.Column(db.String(120), nullable=True)
    online = db.Column(db.Boolean, nullable=True)
    description = db.Column(db.Text(), nullable=True)
    weekday_1 = db.Column(db.String(120), nullable=True)
    weekday_2 = db.Column(db.String(120), nullable=True)
    active_schedule = db.Column(db.Text(), nullable=True)
    active_group = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return str({'id': self.group_id,
                    'name': self.name})


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_1 = db.Column(db.String(120), nullable=True)
    category_2 = db.Column(db.String(120), nullable=True)
    name = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return str({'id': self.id,
                    'category_2': self.category_2,
                    'category_1': self.category_1,
                    'name': self.name})


class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String(120), nullable=True)
    region = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return str({'id': self.id,
                    'district': self.district,
                    'region': self.region})


class PersonalRecs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), nullable=True)
    group_id = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return str({'id': self.id,
                    'user_id': self.user_id,
                    'group_id': self.group_id})


class SimilarUserBasedRecs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), nullable=True)
    group_id = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return str({'id': self.id,
                    'user_id': self.user_id,
                    'group_id': self.group_id})


class ExpandRecs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), nullable=True)
    group_id = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return str({'id': self.id,
                    'user_id': self.user_id,
                    'group_id': self.group_id})
