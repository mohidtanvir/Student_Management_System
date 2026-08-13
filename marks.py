import csv
def add_marks():

    field_map = {
        "MATH": "MATH",
        "PHY": "PHY",
        "BIO": "BIO",
        "ENG": "ENGLISH",

    }

    try:
        ID = input("Enter the ID of the Student: ").strip()
        choice = input(
            "What do you want to ADD?\n"
            "MATH\nPHY\nBIO\nENG\nPhone Number\nGardian Name\n> "
        ).strip().lower()

        if choice not in field_map:
            print("Invalid field selected.")
            return

        field_to_update = field_map[choice]

        rows = []
        found = False

        with open("marks.csv", "r", newline="") as file:
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

        with open("marks.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames) # type: ignore
            writer.writeheader()
            writer.writerows(rows)

    except (FileNotFoundError, FileExistsError, PermissionError) as e:
        print("Something went wrong, please try again.")
        print(e)




       
