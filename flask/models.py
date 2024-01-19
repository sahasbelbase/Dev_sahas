from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PersonModel(db.Model):
    __tablename__ = 'person'
    PersonId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    FullName = db.Column(db.String(200), nullable=False)
    SSN = db.Column(db.String(11), nullable=False)
    Title = db.Column(db.String(200), nullable=False)

    def __init__(self, FullName, SSN, Title):
        self.FullName = FullName
        self.SSN = SSN
        self.Title = Title

    def json(self):
        return {"FullName": self.FullName, "SSN": self.SSN, "Title": self.Title}

# from flask import Flask, request
# from flask_restful import Api, Resource, reqparse
# from models import PersonModel, db
# import os

# app = Flask(__name__)

# base_dir = os.path.abspath(os.path.dirname(__file__))
# db_path = 'data.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# api = Api(app)
# db.init_app(app)

# # Explicitly create the table during application startup
# with app.app_context():
#     db.create_all()
