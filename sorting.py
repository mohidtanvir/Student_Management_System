import csv
student_file ="student.csv"
marks_file="marks.csv"
def avarage_sorting():
     lis = []
     with open(student_file,"r") as file1 , open(marks_file,"r") as file2 :
          reader1 = csv.DictReader(file1)
          reader2 = csv.DictReader(file2)
          for row1,row2 in zip(reader1,reader2):
               total = int(row2["MATH"]) + int(row2["PHY"]) + int(row2["BIO"]) + int(row2["ENGLISH"])
               average = round(total/4,4)
               student_list ={"ID" : row1["ID"],
                              "Name" : row1["Name"],
                              "Total" : total,
                              "Average" :average}
               lis.append(student_list)

     lis.sort(key=lambda s: s["Average"], reverse=True)
 
     print(f"{'ID':>15}{'Name':>15}{'Total':>15}{'Average':>15}")
     print("*" * 60)
     for s in lis :
          
            print(f"{s['ID']:>15}{s['Name']:>15}{s['Total']:>15}{s['Average']:>15}")


def total_sorting():
     lis = []
     with open(student_file,"r") as file1 , open(marks_file,"r") as file2 :
          reader1 = csv.DictReader(file1)
          reader2 = csv.DictReader(file2)
          for row1,row2 in zip(reader1,reader2):
               total = int(row2["MATH"]) + int(row2["PHY"]) + int(row2["BIO"]) + int(row2["ENGLISH"])
               average = round(total/4,4)
               student_list ={"ID" : row1["ID"],
                              "Name" : row1["Name"],
                              "Total" : total,
                              "Average" :average}
               lis.append(student_list)

     lis.sort(key=lambda s: s["Total"], reverse=True)
 
     print(f"{'ID':>15}{'Name':>15}{'Total':>15}{'Average':>15}")
     print("*" * 60)
     for s in lis :
          
            print(f"{s['ID']:>15}{s['Name']:>15}{s['Total']:>15}{s['Average']:>15}")        
          


def name_sorting():
     lis = []
     with open(student_file,"r") as file1 , open(marks_file,"r") as file2 :
          reader1 = csv.DictReader(file1)
          reader2 = csv.DictReader(file2)
          for row1,row2 in zip(reader1,reader2):
               total = int(row2["MATH"]) + int(row2["PHY"]) + int(row2["BIO"]) + int(row2["ENGLISH"])
               average = round(total/4,4)
               student_list ={"ID" : row1["ID"],
                              "Name" : row1["Name"],
                              "Total" : total,
                              "Average" :average}
               lis.append(student_list)

     lis.sort(key=lambda s: s["Name"])
 
     print(f"{'ID':>15}{'Name':>15}{'Total':>15}{'Average':>15}")
     print("*" * 60)
     for s in lis :
        
            print(f"{s['ID']:>15}{s['Name']:>15}{s['Total']:>15}{s['Average']:>15}")        


def Id_sorting():
     lis = []
     with open(student_file,"r") as file1 , open(marks_file,"r") as file2 :
          reader1 = csv.DictReader(file1)
          reader2 = csv.DictReader(file2)
          for row1,row2 in zip(reader1,reader2):
               total = int(row2["MATH"]) + int(row2["PHY"]) + int(row2["BIO"]) + int(row2["ENGLISH"])
               average = round(total/4,4)
               student_list ={"ID" : row1["ID"],
                              "Name" : row1["Name"],
                              "Total" : total,
                              "Average" :average}
               lis.append(student_list)

     lis.sort(key=lambda s: s["ID"], reverse=True)
 
     print(f"{'ID':>15}{'Name':>15}{'Total':>15}{'Average':>15}")
     print("*" * 60)
     for s in lis :
         
            print(f"{s['ID']:>15}{s['Name']:>15}{s['Total']:>15}{s['Average']:>15}")

def boss_sorting():
    flag = True
    while flag :
        print("===== Sort Students =====\n")
        print("1. Sort by Student ID")
        print("2. Sort by Name")
        print("3. Sort by Total Marks")
        print("4. Sort by Average Marks")
        print("5. Back\n")
        choice = int(input("Please enter your choice :\n"))
        match choice:
            case 1 :
                Id_sorting()
                print()
            case 2 : 
                name_sorting()
                print()
            case 3 :
                total_sorting()
                print()
            case 4 :
                avarage_sorting()
                print()
            case 5 :
                flag = False
            case _ :
                print("Please enter the correct choice")
                print()            
        