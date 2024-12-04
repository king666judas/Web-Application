import csv
import os

# Get the directory of the current script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the CSV file path
FILE_NAME = os.path.join(CURRENT_DIR, "library_books.csv")

# Initialize the program
def init_csv():
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            pass  # File exists, no action needed
    except FileNotFoundError:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Add headers
            writer.writerow(["Title", "Author(s)", "ISBN", "Year", "Price", "Quantity"])

# Function to add a book
def add_book():
    print("\nAdd a New Book")
    title = input("Enter the title of the book: ")
    author = input("Enter the author(s) of the book: ")
    isbn = input("Enter the ISBN number: ")
    year = input("Enter the publishing year: ")
    price = input("Enter the price of the book: ")
    quantity = input("Enter the quantity of the book: ")
    
    # Save book to CSV
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author, isbn, year, price, quantity])
    
    print(f"\nBook '{title}' by {author} has been added successfully!")

# Function to view all books
def view_books():
    print("\nList of All Books")
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        books = list(reader)
        
        if not books:
            print("No books available in the system.")
            return
        
        for index, book in enumerate(books, start=1):
            print(f"{index}. Title: {book[0]}, Author(s): {book[1]}, ISBN: {book[2]}, Year: {book[3]}, Price: {book[4]}, Quantity: {book[5]}")

# Function to search books by title
def search_by_title():
    search_title = input("\nEnter the book title to search: ").lower()
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        results = [book for book in reader if search_title in book[0].lower()]
    
    if results:
        print(f"\nBooks matching the title '{search_title}':")
        for book in results:
            print(f"Title: {book[0]}, Author(s): {book[1]}, ISBN: {book[2]}, Year: {book[3]}, Price: {book[4]}, Quantity: {book[5]}")
    else:
        print(f"No books found with the title '{search_title}'.")

# Function to search books by author
def search_by_author():
    search_author = input("\nEnter the author's name to search: ").lower()
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        results = [book for book in reader if search_author in book[1].lower()]
    
    if results:
        print(f"\nBooks written by '{search_author}':")
        for book in results:
            print(f"Title: {book[0]}, Author(s): {book[1]}, ISBN: {book[2]}, Year: {book[3]}, Price: {book[4]}, Quantity: {book[5]}")
    else:
        print(f"No books found by the author '{search_author}'.")

# Function to edit a book
def edit_book():
    print("\nEdit a Book")
    view_books()
    try:
        book_index = int(input("Enter the number of the book to edit: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a valid book number.")
        return
    
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    # Skip header
    if book_index < 0 or book_index >= len(rows) - 1:
        print("Invalid book number. Please try again.")
        return
    
    book_to_edit = rows[book_index + 1]  # Skip the header row
    print(f"\nEditing Book: {book_to_edit[0]} by {book_to_edit[1]}")
    
    title = input(f"Enter the new title (current: {book_to_edit[0]}): ") or book_to_edit[0]
    author = input(f"Enter the new author(s) (current: {book_to_edit[1]}): ") or book_to_edit[1]
    isbn = input(f"Enter the new ISBN number (current: {book_to_edit[2]}): ") or book_to_edit[2]
    year = input(f"Enter the new publishing year (current: {book_to_edit[3]}): ") or book_to_edit[3]
    price = input(f"Enter the new price (current: {book_to_edit[4]}): ") or book_to_edit[4]
    quantity = input(f"Enter the new quantity (current: {book_to_edit[5]}): ") or book_to_edit[5]

    # Update the book entry
    rows[book_index + 1] = [title, author, isbn, year, price, quantity]
    
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    print(f"\nBook '{title}' has been updated successfully!")

# Main program
def main():
    init_csv()
    while True:
        print("\nLibrary Management System")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Search Books by Title")
        print("4. Search Books by Author")
        print("5. Edit a Book")
        print("0. Exit")
        
        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 0:
            print("Exiting the program. Goodbye!")
            break
        elif choice == 1:
            add_book()
        elif choice == 2:
            view_books()
        elif choice == 3:
            search_by_title()
        elif choice == 4:
            search_by_author()
        elif choice == 5:
            edit_book()
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()