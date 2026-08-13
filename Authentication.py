import csv 
def athorize():
    with open("user.csv" , "r" ,) as file:
        reader = csv.DictReader(file)
        for row in reader:
           return row['user'] , row['password']

 
    