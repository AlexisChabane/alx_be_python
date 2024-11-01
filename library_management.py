class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_avaliable(self):
        return not self._is_checked_out
        
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, title, author):
        new_book = Book(title , author)
        self._books.append(new_book)
        print(f"{title}, {author}")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return()
    
    def list_available_books(self):
        available_books = [book.title for book in self._books if book.is_available()]
        