from .user import User, db

class Staff(User):
    __tablename__ = 'staff"' \
    
    id = db.Column(db.Interger, db.ForeginKey('users.id'), primary_key=True)
    department = db.Column(db.String(100))
    
    __mapper_args__ = {
        'polymorphic_identity':'staff',
    }

    def __repr__(self):
        return f'<Staff {self.username}>'
    
    def add_student_to_shortlist(self, student_id, position_id):
        from .shortlist import Shortlist
        shortlist = Shortlist(
            student_id=student_id,
            position_id = positiion_id,
            shortlisted_by=self.id
        )

        db.session.add(shortlist)
        db.session.commit()
        return shortlist