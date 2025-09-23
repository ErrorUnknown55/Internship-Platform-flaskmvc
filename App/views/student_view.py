class StudentView:

    def display_menu():
        print("STUDENT MENU")
        print("1. View Shortlisted Positions")
        print("2. View Employer Responses")
        print("3. Exit")

    def display_shortlisted_positions(shortlist):
        print("\n SHORTLISTED POSITIONS")
        for i, sl in enumerate(shortlist, 1):
            position_title =sl.position.title if sl.position else "Unknown"
            employee_name = sl.position.employer.company_name if sl.position and sl.position.employer else "Unknown"

            print(f"{i}. {position_title} - Employer: {employee_name} - Status: {sl.status}")

    def display_employer_responses(responses):
        print("\n EMPLOYER RESPONSES")
        for i,  responce in enumerate(responses, 1):
            print(f'{i}. Position: {responce['position_title']}')
            print(f'Status: {responce['statis']}')
            print(f'Feedback: {responce['employer feedback']}')