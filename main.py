from database import Database

db = Database("mydb.json")

print("Database Started")
print("Type HELP to see commands, EXIT to quit\n")

while True:
    command = input("DB> ").strip()

    if command.upper() == "EXIT":
        print("Exiting database")
        break

    elif command.upper() == "HELP":
        print("""
Commands:
CREATE students id name marks
INSERT students 1 Vansh 85
SELECT students
SELECT students marks > 80
UPDATE students marks = 98 WHERE id == 1
DELETE students id == 2
EXIT
""")

    else:
        parts = command.split()

        if parts[0].upper() == "CREATE":
            table = parts[1]
            columns = parts[2:]
            db.create_table(table, columns)

        elif parts[0].upper() == "INSERT":
            table = parts[1]
            values = []
            for val in parts[2:]:
                if val.isdigit():
                    values.append(int(val))
                else:
                    values.append(val)
            db.insert_row(table, values)

        elif parts[0].upper() == "SELECT":
            table = parts[1]
            if len(parts) == 2:
                db.select_all(table)
            else:
                column = parts[2]
                operator = parts[3]
                value = int(parts[4])
                db.select_where(table, column, operator, value)

        elif parts[0].upper() == "DELETE":
            table = parts[1]
            column = parts[2]
            operator = parts[3]
            value = int(parts[4])
            db.delete_where(table, column, operator, value)

        elif parts[0].upper() == "UPDATE":
            table = parts[1]
            set_column = parts[2]
            new_value = int(parts[4])
            where_column = parts[6]
            operator = parts[7]
            where_value = int(parts[8])

            db.update_where(
                table,
                set_column,
                new_value,
                where_column,
                operator,
                where_value
            )

        else:
            print("Unknown command. Type HELP.")
