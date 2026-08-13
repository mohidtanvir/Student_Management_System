# Student Management System

A console-based Student Management System written in Python. It manages student
records, subject marks, report cards, class-wide statistics, and sorted rankings,
using CSV files as storage — no database or external dependencies required.

## Features

- **Login** — Username/password check against `user.csv`, with 3 attempts allowed.
- **Add Student** — Store ID, name, CNIC, address, grade, phone number, and guardian name.
- **Search Student** — View a student's personal data or marks by ID.
- **Update Student** — Edit a single field (name, address, CNIC, grade, phone, guardian) by ID.
- **Delete Student** — Remove a student record by ID, with a confirmation prompt.
- **Add Marks** — Update a student's marks for MATH, PHY, BIO, or ENGLISH by ID.
- **View Report Card** — Show a student's marks, total, average, letter grade, and pass/fail status.
- **Class Statistics** — Class average, highest/lowest average, pass/fail counts, and
  the highest score in each subject.
- **Sort Students** — Rank all students by ID, name, total marks, or average marks.

## Requirements

- Python 3.10+ (uses `match` statements)
- No third-party packages — only the standard library (`csv`) is used

## Project Structure

```
Student_Management_System/
├── Main.py                # Entry point: login flow and main menu
├── Authentication.py      # Reads credentials from user.csv
├── Student_Management.py  # Add / search / update / delete student records
├── marks.py                # Add / update student marks
├── Report.py               # Generates a single student's report card
├── clas_static.py          # Class-wide statistics (averages, highs/lows, pass/fail)
├── sorting.py               # Sorts students by ID, name, total, or average
├── student.csv              # Student personal data (created/updated at runtime)
├── marks.csv                 # Student marks data (created/updated at runtime)
└── user.csv                   # Login credentials
```

## Data Files

**user.csv**
```
user,password
```

**student.csv**
```
ID,Name,CNIC,Address,Grade,Phone Number,Gardian Name
```

**marks.csv**
```
ID,MATH,PHY,BIO,ENGLISH
```

> `marks.csv` and `student.csv` are matched by row position (not by ID lookup) in the
> statistics and sorting modules, so keep the two files in the same student order,
> and make sure every student added also has a corresponding marks entry.

## Getting Started

1. Make sure `user.csv`, `student.csv`, and `marks.csv` are present in the project
   folder (sample data is already included).
2. Run the program:
   ```bash
   python Main.py
   ```
3. Log in with the credentials stored in `user.csv`.
4. Use the on-screen menu to manage students, marks, reports, statistics, and sorting.

## Main Menu

```
1. Add Student
2. Search Student
3. Update Student
4. Delete Student
5. Add Marks
6. View Report Card
7. Class Statistics
8. Sort Students
9. Exit
```

## Grading Scale

Report cards (`Report.py`) grade a student on the **sum** of all four subjects:

| Total Marks | Grade | Status |
|-------------|-------|--------|
| >= 90       | A     | Pass   |
| >= 80       | B     | Pass   |
| >= 70       | C     | Pass   |
| >= 60       | D     | Pass   |
| < 60        | F     | Fail   |

Class statistics (`clas_static.py`) separately count a student as **failed** if
any single subject score is below 40.

## Known Limitations

- No password hashing — credentials are stored and compared in plain text.
- `user.csv` only supports a single login account (the first row is used).
- `student.csv` and `marks.csv` are paired by row order, not by ID, in the
  statistics and sorting features — records in the two files must stay aligned.
- No input validation on numeric fields (e.g. marks, phone numbers), so invalid
  entries can cause errors.
- Single-user, single-session console application (no concurrent access handling).

