from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db=SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False, default=datetime.utcnow)

    def serialize(self):
        return{
            'id':self.id,
            'author':self.autor,
            'title':self.title,
            'content':self.content,
            'date_posted':self.date_posted.strftime('%Y-%m-%d %H:%M:%S')
        }
    