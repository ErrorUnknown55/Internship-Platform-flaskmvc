class EmployerView:

    def display_employer_info(self, employer):
        print("\nEMPLOYER MENU")
        print("1. Create Internship Position")
        print("2. View My Positions")
        print("3. View Shortlisted for Position")
        print("4. Accept Student")
        print("5. Reject Student")
        print("6. Exit")

    def display_students(students):
        print("\nList of Students:")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.usernamre} - {student.major} - {student.year}")

    def display_positions(positions):
        print("\nList of Positions:")
        for i, position in enumerate(positions, 1):
            employee_name  = pos.employer.company_name if pos.employer else "Unknown"
            print(f"{i}. {pos.title} - {employee_name}")

    def get_shortlist_details():
        student_id =  input("Enter student ID: ")
        position_id = input("Enter position ID: ")
        return int(student_id), int(position_id)
    
    def display_shortlist(shortlist):
        print("\nShortlisted Students:")
        for i, sl in enumerate(shortlist, 1):
            student_name = sl.student.username if sl.student else "Unknown"
            position_title = sl.position.title if sl.position else "Unknown"
            print(f"{i}. Student:{student_name} - Position {position_title} - Status: {sl.status}")
            
