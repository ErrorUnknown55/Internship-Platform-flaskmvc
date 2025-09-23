from .user import db
from datetime import datetime

class Shortlist(db.Model):
    __tablename__ = 'shortlists'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('internship_positions.id'), nullable=False)

    shortlisted_by = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
    status = db.Column(db.String(20), default='Pending')
    employer_feedback = db.Column(db.Text)
    shortlisted_at = db.Column(db.DateTime, default=datetime.utcnow)
    responded_at = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Shortlist Student: {self.student_id}, Position: {self.position_id}>'
    
    def accept_student(self, feedback=""):
        self.status = 'Accepted'
        self.employer_feedback = feedback
        self.responded_at = datetime.utcnow()
        db.session.commit()

    def reject_student(self, feedback=""):
        self.status = 'Rejected'
        self.employer_feedback = feedback
        self.responded_at = datetime.utcnow()
        db.session.commit()
