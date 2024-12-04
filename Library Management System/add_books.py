# title, author(s), ISBN, publishing year

import add_books
from save_all_books import save_all_books

def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = int(input("Enter ISBN Number: "))
    year = int(input("Enter Publishing Year: "))
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity Number: "))

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
    }

    all_books.append(book)
    save_all_books(all_books)

    print("Books Added Successfully")

    return all_books

