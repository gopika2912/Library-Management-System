books = []

def add_book(title, author):
    books.append({"title": title, "author": author})

def view_books():
    for book in books:
        print(f"{book['title']} by {book['author']}")

if __name__ == "__main__":
    add_book("1984", "George Orwell")
    add_book("To Kill a Mockingbird", "Harper Lee")
    view_books()
