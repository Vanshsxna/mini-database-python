# Mini Database Engine (Python)

A simple, interactive, CLI-based database engine built from scratch using Python.

This project was created to understand how databases work internally including table creation, data storage, querying, updating, and deletion without using SQL or external frameworks.

---

## Features
- Create tables with custom columns  
- Insert records dynamically  
- View all records  
- Filter records using conditions (`>`, `<`, `==`)  
- Update records using conditions  
- Delete records using conditions  
- Persistent storage using JSON  
- Interactive command-line interface  

---

## Example Commands

CREATE students id name marks
INSERT students 1 Vansh 95
INSERT students 2 Serah 93
SELECT students
SELECT students marks > 90
UPDATE students marks = 99 WHERE id == 1
DELETE students id == 2
EXIT

---

## Technologies Used
- Python
- Object-Oriented Programming (OOP)
- File Handling
- JSON
- Data Structures 

---

## What I Learned

- How databases store and manage data internally
- How CRUD operations work behind the scenes
- Designing an interactive CLI-based system
- Importance of persistence and data integrity
- Applying DSA concepts like searching, filtering, and indexing logic

---

## Future Improvements

- Indexing for faster searches
- More advanced query parsing
- Data validation and constraints

## Author
Vansh Saxena