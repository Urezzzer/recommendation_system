from sqlalchemy.orm import relationship

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
    popularity = db.Column(db.Integer, nullable=True)

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
    group_id = db.Column(db.String(120), db.ForeignKey('groups.group_id'), nullable=True)
    score = db.Column(db.Float(), nullable=True)

    def __repr__(self):
        return str({'id': self.id,
                    'user_id': self.user_id,
                    'group_id': self.group_id})


class ExpandRecs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), nullable=True)
    group_id = db.Column(db.String(120), db.ForeignKey('groups.group_id'), nullable=True)
    score = db.Column(db.Float(), nullable=True)

    def __repr__(self):
        return str({'id': self.id,
                    'user_id': self.user_id,
                    'group_id': self.group_id})


class Ranks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), nullable=True)
    group_id = db.Column(db.String(120), db.ForeignKey('groups.group_id'), nullable=True)
    score = db.Column(db.Float(), nullable=True)

    def __repr__(self):
        return str({'id': self.id,
                    'user_id': self.user_id,
                    'group_id': self.group_id,
                    'score': self.score})


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), nullable=True)
    sex = db.Column(db.Integer, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    active_in_months = db.Column(db.Integer, nullable=True)
    active_in_years = db.Column(db.Integer, nullable=True)
    user_district = db.Column(db.String(120), nullable=True)
    user_region = db.Column(db.String(120), nullable=True)
    history = db.Column(db.String(120), nullable=True)
    name = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return str({'id': self.id,
                    'user_id': self.user_id,
                    'user_district': self.user_district})
