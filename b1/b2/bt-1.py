class BookItem:
    def __init__(self, id, title, author="Unknown", averageRating="0", publicationDate="28-6-2025"):
        self.id = id
        self.title = title
        self.author = author
        self.averageRating = averageRating
        self.publicationDate = publicationDate
    def __str__(self):
        return f"Title: {self.title} Author: {self.author} averageRating: {self.averageRating} publicationDate: {self.publicationDate}"
class BookCollection:
    def __init__(self):
        self.Book_Collection = []

    def create(self, book:Book):
        if self.get_by_id
        self.Book_Collection.append(book)
    
    def get_all(self):
        return self.Book_Collection
    
    def update(self, id, new_data:dict):
        for key, value in new_data.item():
            if value is not None:
                setattr