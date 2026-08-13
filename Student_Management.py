import csv
def add_student():
    fieldnames = ["ID","Name","CNIC","Address","Grade","Phone Number","Gardian Name"]
    try :
     with open("student.csv","a") as file :
        writer = csv.DictWriter(file,fieldnames=fieldnames)
        ID = input("Enter the Student ID :")
        Name = input("Enter the name of the Student :")
        CNIC = input("Enter the CNIC of the Student :")
        Address = input("Enter the Address of the Student :")
        Grade =input("Enter the Grade of the Student :")    
        Phone_Number = input("Enter the Phone NUmber of the Student :")
        Gardian_Name = input("Enter the Gardian Name of the Student :")
        writer.writerow({"ID":ID,"Name":Name,"CNIC":CNIC,"Address":Address,"Grade":Grade,
                         "Phone Number":Phone_Number,"Gardian Name":Gardian_Name})
        print("Student add Successfully ")
    except(FileNotFoundError,FileExistsError,PermissionError) as e:
           print("Something Happen with the value please try again")
           print(e)


def delete_Student():
 try :
    ID_to_delete = input("Enter roll number to delete: ")
    fieldnames =[]
    rows = []
    found1 = False
    found2 = False
    
    with open("student.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        for row in reader:
            if row["ID"] == ID_to_delete:
                found1 = True   
                found2 = True
                if found2 :
                     answer = input("Are u sure Y/N ").lower().strip()
                     if answer == "n":
                          return
            else:
                rows.append(row)
    
    if not found1:
        print("No student found with that ID.")
        return
    
    with open("student.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames) # type: ignore
        writer.writeheader()
        writer.writerows(rows)
    
    print("Student deleted successfully!")
 except(FileNotFoundError,FileExistsError,PermissionError) as e:
     print("Soemthing Wrong Happen Please Try Again")
     print(e)

def update_Student():
    field_map = {
        "name": "Name",
        "address": "Address",
        "cnic": "CNIC",
        "grade": "Grade",
        "phone number": "Phone Number",
        "gardian name": "Gardian Name",
    }

    try:
        ID = input("Enter the ID of the Student: ").strip()
        choice = input(
            "What do you want to update?\n"
            "Name\nAddress\nCNIC\nGrade\nPhone Number\nGardian Name\n> "
        ).strip().lower()

        if choice not in field_map:
            print("Invalid field selected.")
            return

        field_to_update = field_map[choice]

        rows = []
        found = False

        with open("student.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            for row in reader:
                if row["ID"] == ID:
                    found = True
                    new_value = input(f"Enter the new {field_to_update}: ")
                    row[field_to_update] = new_value
                    print(f"{field_to_update} changed successfully.")
                rows.append(row)

        if not found:
            print("Sorry, that student does not exist.")
            return

        with open("student.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames) # type: ignore
            writer.writeheader()
            writer.writerows(rows)

    except (FileNotFoundError, FileExistsError, PermissionError) as e:
        print("Something went wrong, please try again.")
        print(e)


def view_student():
     flag = True
     while flag:
        print("What u want to see")
        print("1. Marks")
        print("2. Personal Data")
        print("3. Exit")
        choices = int(input("Enter the Choices :"))

        if choices not in (1, 2, 3):
             print("Please Select valid choice")
             continue

        if choices == 3:
             flag = False
             continue

        id = input("Enter the ID of student to view ")

        try:
            match choices:
                case 1:
                    with open("marks.csv", "r") as file_2:
                        reader_2 = csv.DictReader(file_2)
                        print(f"{'ID':<15} {'MATH':<15} {'PHY':<15} {'BIO':<15} {'ENG':<15}")
                        print("-" * 67)
                        found = False
                        for row in reader_2:
                            if id == row["ID"]:
                                print(f"{row['ID']:<15} {row['MATH']:<15} {row['PHY']:<15} {row['BIO']:<15} {row['ENGLISH']:<15}")
                                found = True
                                break
                        if not found:
                            print("There is no student")

                case 2:
                    with open("student.csv", "r") as file_1:
                        reader_1 = csv.DictReader(file_1)
                        print(f"{'ID':<15} {'Name':<15} {'Grade':<15} {'Phone Number':<15} {'Gardian Name':<15} {'Address':<15}")
                        print("-" * 87)
                        found = False
                        for row in reader_1:
                            if id == row["ID"]:
                                print(f"{row['ID']:<15} {row['Name']:<15} {row['Grade']:<15} {row['Phone Number']:<15} {row['Gardian Name']:<15} {row['Address']:<15}")
                                found = True
                                break
                        if not found:
                            print("There is no such student")

        except (FileNotFoundError, FileExistsError, PermissionError) as e:
            print("Something Wrong Happened Please Try Again")
            print(e)

     
     
    
                          
                                    
                                                   
                                     
               




