class StaffView:
    @staticmethod
    def display_menu():
        print("\n=== STAFF MENU ===")
        print("1. View All Students")
        print("2. View All Positions")
        print("3. Add Student to Shortlist")
        print("4. View All Shortlists")
        print("5. Exit")
    
    @staticmethod
    def display_students(students):
        print("\n=== ALL STUDENTS ===")
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.username} - {student.major} - {student.year}")
    
    @staticmethod
    def display_positions(positions):
        print("\n=== ALL POSITIONS ===")
        for i, pos in enumerate(positions, 1):
            employer_name = pos.employer.company_name if pos.employer else "Unknown"
            print(f"{i}. {pos.title} - {employer_name}")
    
    @staticmethod
    def get_shortlist_details():
        student_id = input("Enter student ID: ")
        position_id = input("Enter position ID: ")
        return int(student_id), int(position_id)
    
    @staticmethod
    def display_shortlists(shortlists):
        print("\n=== ALL SHORTLISTS ===")
        for i, sl in enumerate(shortlists, 1):
            student_name = sl.student.username if sl.student else "Unknown"
            position_title = sl.position.title if sl.position else "Unknown"
            print(f"{i}. Student: {student_name} - Position: {position_title} - Status: {sl.status}")