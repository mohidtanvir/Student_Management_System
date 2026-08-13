import Authentication  # type: ignore
import marks
import sorting
import Report
import clas_static
import Student_Management


def login():

    try:
        user, pawd = Authentication.athorize()  # type: ignore
    except (ValueError, ImportError, PermissionError, AttributeError) as e:
        print("Something Wrong Happened Please Try again")
        print(e)
        return False

    for attempt in range(3):
        user_name = input("Username: ")
        password = input("Password: ")
        if user_name == user and password == pawd:
            return True
        print("Password or username is wrong")

    print("You reached the limit")
    return False


def menu():
    flag = True
    while flag:
        print()
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Add Marks")
        print("6. View Report Card")
        print("7. Class Statistics")
        print("8. Sort Students")
        print("9. Exit")
        print("==============================")
      
        choice = int(input("Please Enter Your Choice: "))
        if choice not in (1, 2, 3,4,5,6,7,8,9):
             print("Please Select valid choice")
             continue

        if choice == 9:
             flag = False
             continue
        match choice:
            case 1:
                Student_Management.add_student()
            case 2:
                Student_Management.view_student()
            case 3:
                Student_Management.update_Student()
            case 4:
                Student_Management.delete_Student()
            case 5:
                marks.add_marks()
            case 6:
                Report.report()
            case 7:
                clas_static.static_boss_func()
            case 8:
                sorting.boss_sorting()



def main():
    print("==============================")
    print(" Student Management System")
    print("==============================")
    print("Enter your user_name and Password")

    if login():
        print("Login Successfully")
        menu()
    else:
        print("Login failed. Exiting program.")


if __name__ == "__main__":
    main()