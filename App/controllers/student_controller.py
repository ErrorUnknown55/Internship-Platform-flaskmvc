from App.models import Student, Shortlist

class StudentController:

    def view_shortlisted_positions(student_id):
        student = Student.get_by_id(student_id)
        if student:
            return student.get_shortlisted_positions()
        return []
    
    def view_empoyer_responses(student_id):
        student = Student.get_by_id(student_id)
        if student:
            return student.view_employer_responses()
        return []