from flask_sqlalchemy import SQLAlchemy
from demoapp.default_recommendation import DEFAULT_RECOMMENDATION

db = SQLAlchemy()


class Recommendation(db.Model):
    __tablename__ = "recommendations"
    id = db.Column("id", db.Integer, primary_key=True, index=True)
    history = db.Column(db.JSON)
    recommendations = db.Column(db.JSON, default=DEFAULT_RECOMMENDATION)