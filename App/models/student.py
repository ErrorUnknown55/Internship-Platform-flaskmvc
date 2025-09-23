from .user import User, db

class Student(User):
    __tablename__ = 'students'

    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    student_id = db.Column(db.String(20), unique=True)
    major = db.Column(db.String(100))
    year = db.Column(db.String(20))#Tobe chnaged to 4 digits

    # Relationships
    shortlists = db.relationship('Shortlist', backref='student', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity':'student',
    }

    def __repr__(self):
        return f'<Student {self.username}>'
    
    def get_shprtlisted_positions(self):
        from .shortlist import Shortlist
        return Shortlist.query.fileter_by(student_id=self.id).all()
    
    def view_employer_responses(self):
        shortlists = self.get_shortlisted_positions()
        responses = []
        for shortlist in shortlists:
            responses.append({
                'position': shortlist.position.title,
                'status': shortlist.status,
                'response_message': shortlist.employer_feedback
            })
        return responses