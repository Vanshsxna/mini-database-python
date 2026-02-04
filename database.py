import json
import os


class Database:
    def __init__(self, filename):
        """
        Initialize the database.
        If file exists → load data
        Else → create empty database file
        """
        self.filename = filename
        self.tables = {}

        if os.path.exists(self.filename):
            self.load()
        else:
            self.save()




    def create_table(self, table_name, columns):
        """
        Create a new table with given columns
        """
        if table_name in self.tables:
            print("Table already exists")
            return

        self.tables[table_name] = {
            "columns": columns,
            "rows": []
        }

        self.save()
        print(f"Table '{table_name}' created")




    def insert_row(self, table_name, values):
        """
        Insert a row into a table
        """
        if table_name not in self.tables:
            print("Table does not exist")
            return

        table = self.tables[table_name]

        if len(values) != len(table["columns"]):
            print("Column count does not match values")
            return

        table["rows"].append(values)
        self.save()

        print(f"Row inserted into '{table_name}'")

    def select_all(self, table_name):
        """
        Display all rows from a table
        """
        if table_name not in self.tables:
            print("Table does not exist")
            return

        table = self.tables[table_name]

        print(f"\nTABLE: {table_name}")
        print(table["columns"])

        for row in table["rows"]:
            print(row)




    def select_where(self, table_name, column, operator, value):
        """
        Select rows using a WHERE condition
        Example: marks > 80
        """
        if table_name not in self.tables:
            print("Table does not exist")
            return

        table = self.tables[table_name]

        if column not in table["columns"]:
            print("Column does not exist")
            return

        col_index = table["columns"].index(column)

        print(f"\n FILTERED RESULTS FROM {table_name}") 

        for row in table["rows"]:
            cell_value = row[col_index]

            if operator == ">" and cell_value > value:
                print(row)
            elif operator == "<" and cell_value < value:
                print(row) 
            elif operator == "==" and cell_value == value:
                print(row)

    



    def save(self):
        """
        Save database to JSON file
        """
        with open(self.filename, "w") as file:
            json.dump(self.tables, file, indent=4)




    def load(self):
        """
        Load database from JSON file
        """
        with open(self.filename, "r") as file:
            self.tables = json.load(file)




    def delete_where(self, table_name, column, operator, value):
        """
        Delete rows using a WHERE condition
        Example: DELETE students WHERE id == 2
        """
        if table_name not in self.tables:
            print("Table does not exist")
            return

        table = self.tables[table_name]

        if column not in table["columns"]:
            print("Column does not exist")
            return

        col_index = table["columns"].index(column)

        original_count = len(table["rows"])
        new_rows = []

        for row in table["rows"]:
            cell_value = row[col_index]

            delete = False
            if operator == "==" and cell_value == value:
                delete = True
            elif operator == ">" and cell_value > value:
                delete = True
            elif operator == "<" and cell_value < value:
                delete = True

            if not delete:
                new_rows.append(row)

        table["rows"] = new_rows
        self.save()

        deleted_count = original_count - len(new_rows)
        print(f"Deleted {deleted_count} row(s) from '{table_name}'")




    def update_where(self, table_name, set_column, new_value, where_column, operator, where_value):
        """
        Update rows using a WHERE condition
        Example: UPDATE students marks = 98 WHERE id == 1
        """
        if table_name not in self.tables:
            print("Table does not exist")
            return

        table = self.tables[table_name]

        if set_column not in table["columns"] or where_column not in table["columns"]:
            print("Column does not exist")
            return

        set_index = table["columns"].index(set_column)
        where_index = table["columns"].index(where_column)

        updated_count = 0

        for row in table["rows"]:
            cell_value = row[where_index]

            condition_met = False
            if operator == "==" and cell_value == where_value:
                condition_met = True
            elif operator == ">" and cell_value > where_value:
                condition_met = True
            elif operator == "<" and cell_value < where_value:
                condition_met = True

            if condition_met:
                row[set_index] = new_value
                updated_count += 1

        self.save()
        print(f"Updated {updated_count} row(s) in '{table_name}'")

