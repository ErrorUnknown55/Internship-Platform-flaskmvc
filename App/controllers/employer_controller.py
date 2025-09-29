from App.models import Employer, InternshipPosition, Shortlist, db

class EmployerController:
    
    def create_position(employer_id, title, description, requirements):
        employer = Employer.query.get(employer_id)
        if employer:
            return employer.create_internship_position(title, description, requirements)
        return None
    
    def get_positions(employer_id):
        return InternshipPosition.query.filter_by(employer_id=employer_id).all()
    
    def get_shortlists_for_position(position_id):
        return Shortlist.query.filter_by(position_id=position_id).all()
    
    def accept_student(shortlist_id, feedback=""):
        shortlist = Shortlist.query.get(shortlist_id)
        if shortlist:
            shortlist.accept_student(feedback)
            return True
        return False
    
    def reject_student(shortlist_id, feedback=""):
        shortlist = Shortlist.query.get(shortlist_id)
        if shortlist:
            shortlist.reject_student(feedback)
            return True
        return False