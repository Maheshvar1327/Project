students = []
books = []
rentals = [] 

def add_student():
    name = input("Enter student name: ")
    students.append(name)
    print(f"Student '{name}' added successfully!")

def add_book():
    name = input("Enter book name: ")
    books.append(name)
    print(f"Book '{name}' added to library!")

def rent_book():
    print("--- CURRENT STUDENTS ---")
    print(students)
    print("--- AVAILABLE BOOKS ---")
    print(books)

    student = input("Enter student name: ")
    if student not in students:
        print("Student not found! Add student first.")
        return
    
    book = input("Enter book name: ")
    if book not in books:
        print("Book not found! Add book first.")
        return
    
    quantity = int(input("Enter number of books to rent: "))
    
    rentals.append([student, book, quantity])
    print(f"{quantity} copies of '{book}' rented to {student}!")

def show_rentals():
    print("*** RENTAL REPORT ***")
    if not rentals:
        print("No rentals yet!")
        return
    
    for rental in rentals:
        student, book, qty = rental
        print(f"- {student} rented {qty} x '{book}'")

def show_all_data():
    print("--- LIBRARY DATA ---")
    print(f"Total Students: {len(students)}")
    print(f"Total Books: {len(books)}")
    print(f"Total Rentals: {len(rentals)}")
    show_rentals()

while True:
    print("=== LIBRARY SYSTEM ===")
    print("1. Add Student")
    print("2. Add Book") 
    print("3. Rent Book")
    print("4. Show All Data")
    print("5. Exit")
    
    choice = input("Choose option (1-5): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        add_book()
    elif choice == '3':
        rent_book()
    elif choice == '4':
        show_all_data()
    elif choice == '5':
        print("Thank you for using Library System!")
        break
    else:
        print("Invalid choice! Try again.")