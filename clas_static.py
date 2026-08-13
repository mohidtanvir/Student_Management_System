import csv 
marks_file = "marks.csv"

def class_average_and_total_Student():
    
    list = []
    count = 0
    try:
           with open(marks_file,"r") as file :
               marks_row = csv.DictReader(file)
               for row in marks_row:
                   total = int(row["MATH"]) + int(row["PHY"]) + int(row["BIO"]) + int(row["ENGLISH"])
                   list.append(round(total/4,4))
                   count+=1
           return round(sum(list)/count,4) , count       
    except (FileNotFoundError, FileExistsError, PermissionError,ZeroDivisionError,ValueError) :
        return 0, 0


def highest_Average():
     highest = float("-inf")
     try :
          with open(marks_file,"r") as file :
               marks_row = csv.DictReader(file)
               for row in marks_row:
                   total = int(row["MATH"]) + int(row["PHY"]) + int(row["BIO"]) + int(row["ENGLISH"])
                   average = round(total/4,4)
                   if average >= highest :
                        highest = average
          return highest
                         
     except (FileNotFoundError, FileExistsError, PermissionError,ZeroDivisionError,ValueError) :
             return 0


def lowest_Average():
     lowest = float("inf")
     try :
               with open(marks_file,"r") as file :
                    marks_row = csv.DictReader(file)
                    for row in marks_row:
                        total = int(row["MATH"]) + int(row["PHY"]) + int(row["BIO"]) + int(row["ENGLISH"])
                        average = round(total/4,4)
                        if average <= lowest :
                             lowest = average
               return lowest
     except (FileNotFoundError, FileExistsError, PermissionError,ZeroDivisionError,ValueError) :
             return 0


def failed_student():
     count = 0
     try :
          with open(marks_file,"r") as file :
                              marks_row = csv.DictReader(file)
                              for row in marks_row:
                                    if int(row["MATH"]) < 40 or int(row["PHY"]) < 40 or int(row["BIO"]) < 40 or int(row["ENGLISH"]) < 40:
                                            count += 1
          return count                                                 
     except (FileNotFoundError, FileExistsError, PermissionError,ZeroDivisionError,ValueError) :
             return 0


def math_higgest_Number():
     highest = float("-inf")
     try :
          with open(marks_file,"r") as file :
               marks_row = csv.DictReader(file)
               for row in marks_row:
                   total = int(row["MATH"]) 
                   if total >=  highest :
                        highest = total
          return highest
                         
     except (FileNotFoundError, FileExistsError, PermissionError,ZeroDivisionError,ValueError) :
             return 0


def bio_higgest_Number():
     highest = float("-inf")
     try :
          with open(marks_file,"r") as file :
               marks_row = csv.DictReader(file)
               for row in marks_row:
                   total = int(row["BIO"]) 
                   if total >=  highest :
                        highest = total
          return highest
                         
     except (FileNotFoundError, FileExistsError, PermissionError,ZeroDivisionError,ValueError) :
             return 0

def phy_higgest_Number():
     highest = float("-inf")
     try :
          with open(marks_file,"r") as file :
               marks_row = csv.DictReader(file)
               for row in marks_row:
                   total = int(row["PHY"]) 
                   if total >=  highest :
                        highest = total
          return highest
                         
     except (FileNotFoundError, FileExistsError, PermissionError,ZeroDivisionError,ValueError) :
             return 0     

def eng_higgest_Number():
     highest = float("-inf")
     try :
          with open(marks_file,"r") as file :
               marks_row = csv.DictReader(file)
               for row in marks_row:
                   total = int(row["ENGLISH"]) 
                   if total >=  highest :
                        highest = total
          return highest
                         
     except (FileNotFoundError, FileExistsError, PermissionError,ZeroDivisionError,ValueError) :
             return 0     


def static_boss_func():
       class_average,total_student = class_average_and_total_Student()
       passed_student = total_student-failed_student()
       print(f"Total Student : {total_student}")
       print()
       print(f"Highest Average : {highest_Average()}")
       print()
       print(f"Class Average : {class_average}")
       print()
       print(f"Passed Student : {passed_student}")
       print()
       print(f"Failed Student : {failed_student()}")
       print()
       print(f"Higest Math Marks : {math_higgest_Number()}")
       print()
       print(f"Higest BIO Marks : {bio_higgest_Number()}")
       print()
       print(f"Higest PHY Marks : {phy_higgest_Number()}")
       print()
       print(f"Higest ENG Marks : {eng_higgest_Number()}")

