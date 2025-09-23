from .user import User, db

class Employer(User):
    __tablename__ = 'employers'

    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    company_description = db.Column(db.Text)

    #Relationships
    internship_positions = db.relationship('InternshipPosition', backref='employer', lazy=True)
    
    __mapper_args__ = {
        'polymorphic_identity':'employer',
    }

    def __repr__(self):
        return f'<Employer {self.username}>'

    def create_internship_position(self, title, description, requirements):
        from .internship_position import IntershipPosition
        position = InternshipPosition(
            title=title,
            description=description,
            requirements=requirements,
            employer_id=self.id
        )
        db.session.add(position)
        db.session.commit()
        return position
