from datetime import datetime
from app import db

class Todo(db.Model):
    
    srno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(600), nullable=False)
    created_Date = db.Column(db.DateTime ,default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.srno} - {self.title}"