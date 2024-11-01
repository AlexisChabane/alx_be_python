class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
class EBook(Book):
    def __init__(self, title: str, author: str, file_size):
        super().__init__(title, author)
        self.file_size = file_size
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count):
        super().__init__(title, author)
        self.page_count = page_count
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only instances of Book, Ebook, or printBook can be added")
        
    def list_books(self):
        for book in self.books:
            print(book)
        