from flask import Flask
from models import db, User, Employer, Staff, Student, InternshipPosition, Shortlist
from controllers import EmployerController, StaffController, StudentController
from views import EmployerView, StaffView, StudentView
import sys

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///internship.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()
        create_sample_data()
    
    return app

def create_sample_data():
    # Create sample data if not exists
    if not User.query.first():
        # Create employers
        employer1 = Employer(username='tech_corp', email='hr@techcorp.com', 
                           password_hash='pass', company_name='Tech Corp')
        employer2 = Employer(username='innovate_ltd', email='careers@innovate.com', 
                           password_hash='pass', company_name='Innovate Ltd')
        
        # Create staff
        staff1 = Staff(username='advisor_john', email='john@uni.edu', 
                      password_hash='pass', department='CS')
        
        # Create students
        student1 = Student(username='alice_smith', email='alice@student.edu', 
                          password_hash='pass', student_id='S001', major='Computer Science', year='Senior')
        student2 = Student(username='bob_jones', email='bob@student.edu', 
                          password_hash='pass', student_id='S002', major='Engineering', year='Junior')
        
        db.session.add_all([employer1, employer2, staff1, student1, student2])
        db.session.commit()
        
        # Create positions
        position1 = InternshipPosition(title='Software Developer Intern', 
                                     description='Develop web applications',
                                     requirements='Python, JavaScript',
                                     employer_id=employer1.id)
        position2 = InternshipPosition(title='Data Analyst Intern', 
                                     description='Analyze business data',
                                     requirements='SQL, Excel',
                                     employer_id=employer2.id)
        
        db.session.add_all([position1, position2])
        db.session.commit()

def employer_cli(employer_id):
    view = EmployerView()
    controller = EmployerController()
    
    while True:
        view.display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title, description, requirements = view.get_position_details()
            controller.create_position(employer_id, title, description, requirements)
            print("Position created successfully!")
        
        elif choice == '2':
            positions = controller.get_positions(employer_id)
            view.display_positions(positions)
        
        elif choice == '3':
            position_id = int(input("Enter position ID: "))
            shortlists = controller.get_shortlists_for_position(position_id)
            view.display_shortlists(shortlists)
        
        elif choice == '4':
            shortlist_id, feedback = view.get_shortlist_action()
            if controller.accept_student(shortlist_id, feedback):
                print("Student accepted!")
            else:
                print("Error accepting student")
        
        elif choice == '5':
            shortlist_id, feedback = view.get_shortlist_action()
            if controller.reject_student(shortlist_id, feedback):
                print("Student rejected!")
            else:
                print("Error rejecting student")
        
        elif choice == '6':
            break

def staff_cli(staff_id):
    view = StaffView()
    controller = StaffController()
    
    while True:
        view.display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            students = controller.get_all_students()
            view.display_students(students)
        
        elif choice == '2':
            positions = controller.get_all_positions()
            view.display_positions(positions)
        
        elif choice == '3':
            student_id, position_id = view.get_shortlist_details()
            controller.add_to_shortlist(staff_id, student_id, position_id)
            print("Student added to shortlist!")
        
        elif choice == '4':
            shortlists = controller.get_shortlists()
            view.display_shortlists(shortlists)
        
        elif choice == '5':
            break

def student_cli(student_id):
    view = StudentView()
    controller = StudentController()
    
    while True:
        view.display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            shortlists = controller.view_shortlisted_positions(student_id)
            view.display_shortlisted_positions(shortlists)
        
        elif choice == '2':
            responses = controller.view_employer_responses(student_id)
            view.display_employer_responses(responses)
        
        elif choice == '3':
            break

def main():
    app = create_app()
    
    with app.app_context():
        print("=== INTERNSHIP PLATFORM ===")
        print("1. Login as Employer")
        print("2. Login as Staff")
        print("3. Login as Student")
        print("4. Exit")
        
        role_choice = input("Choose your role: ")
        
        if role_choice == '1':
            employers = Employer.query.all()
            for i, emp in enumerate(employers, 1):
                print(f"{i}. {emp.company_name}")
            emp_choice = int(input("Select employer: ")) - 1
            employer_cli(employers[emp_choice].id)
        
        elif role_choice == '2':
            staff_members = Staff.query.all()
            for i, staff in enumerate(staff_members, 1):
                print(f"{i}. {staff.username}")
            staff_choice = int(input("Select staff: ")) - 1
            staff_cli(staff_members[staff_choice].id)
        
        elif role_choice == '3':
            students = Student.query.all()
            for i, student in enumerate(students, 1):
                print(f"{i}. {student.username}")
            student_choice = int(input("Select student: ")) - 1
            student_cli(students[student_choice].id)
        
        elif role_choice == '4':
            sys.exit()

if __name__ == '__main__':
    main()