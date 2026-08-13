import csv
def report():
    id =input("Enter the id of the student :")
    student_file = "student.csv"
    marks_file = "marks.csv"
    grade = None
    try:
        with open (student_file , "r") as file1 , open(marks_file,"r") as file2 :
            student_row = csv.DictReader(file1)
            marks_row = csv.DictReader(file2)
            found = False
            for row in student_row:
                if row["ID"] == id :
                    print(row["Name"])
                    print()
                    break
            for row in marks_row :
              
              if row["ID"] == id :
                print(f"MATH {row["MATH"]}")
                print(f"PHY {row["PHY"]}")
                print(f"BIO {row["BIO"]}")
                print(f"ENGLISH {row["ENGLISH"]}")
                print()
                total = int(row["MATH"]) + int(row["PHY"]) + int(row["BIO"]) + int(row["ENGLISH"])
                print(f"SUM                 {total}")
                print(f"Average             {round(total/4,4)}")
                if round(total/4,4) >= 90:
                        grade = "A"
                elif round(total/4,4) >= 80:
                         grade = "B"
                elif round(total/4,4) >= 70:
                      grade = "C"
                elif round(total/4,4) >= 60:
                       grade = "D"
                else:
                        grade = "F"

                print(f"grade               {grade}")
                if grade == "F":
                     print("Status             Fail")
                else :
                     print("Status             Pass") 
            if not found:
                   print("Student not found")
    except (FileNotFoundError, FileExistsError, PermissionError,ValueError) :
         print("SOmething is wrong")





              

                   
                
