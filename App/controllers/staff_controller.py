from App.models import Staff, Student, InternshipPosition, Shortlist, db

class StaffController:

    def add_student_to_shortlist(staff_id, student_id, position_id):
        staff = Staff.query.get(staff_id)
        if staff:
            return staff.add_student_to_shortlist(student_id, position_id)
        return None
    
    def get_all_students():
        return Student.query.all()
    
    def get_all_positions():
        return InternshipPosition.query.filter_by(is_active=True).all()
    
    def get_shortlists():
        return Shortlist.query.all()