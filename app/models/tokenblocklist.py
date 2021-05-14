from app import db


class TokenBlockList(db.Model):
    __tablename__ = "TokenBlockList"
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

