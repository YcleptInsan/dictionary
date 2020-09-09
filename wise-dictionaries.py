def main():

    courses = {
        'CS101': {
            'room': '3004',
            'instructor': 'Haynes',
            'meetingTime': "8:00 am",
        },
        'CS102': {
            'room': '4501',
            'instructor': 'Alvarado',
            'meetingTime': "9:00 am",

        },
        'CS103': {
            'room': '6755',
            'instructor': 'Rich',
            'meetingTime': "10:00 am",

        },
        'NT110': {
            'room': '1244',
            'instructor': 'Burke',
            'meetingTime': "11:00 am",

        },
        'CM241': {
            'room': '1411',
            'instructor': 'Lee',
            'meetingTime': "1:00 pm",

        },
    }

    def restart():
        answer = input("\nWould you like to look for another class? y/n \n").upper()
        if answer == 'y' or answer == 'Y':
            main()
        if answer == 'n' or answer == 'N':
            exit()

    def user_search():
        print("List of Courses: ")
        for course in courses:
            print(course)
        print("\n")
        course_lookup = input("Welcome, Please enter a course number to view it's details. \n").upper()

        search_course(course_lookup)

    def search_course(course_lookup):

        for course, details in courses.items():
            if course == course_lookup:
                room = details['room']
                instructor = details['instructor']
                meeting_time = details['meetingTime']

                print("Course: " + course)
                print("\tRoom #: " + room)
                print("\tInstructor: " + instructor)
                print("\tMeeting Time: " + meeting_time + "\n")

                restart()
            if course != course_lookup:
                print("\nWhoops its seems that class doesn't exist. Please enter a correct class number.")
                print("-------------------------------------------------------------------------------")
                restart()
                break

    user_search()


main()
