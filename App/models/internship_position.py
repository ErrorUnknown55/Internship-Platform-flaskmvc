from .user import db
from datetime import datetime

class InternshipPosition(db.Model):
    __tablename__ = 'internship_positions'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    requirements = db.Column(db.Text)
    employer_id = db.Column(db.Integer, db.ForeignKey('employers.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    # Relationships
    shortlists = db.relationship('Shortlist', backref='position', lazy=True)

    def __repr__(self):
        return f'<InternshipPosition {self.title}>'