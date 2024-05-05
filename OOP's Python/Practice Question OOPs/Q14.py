# 14. Create a class `Book` with attributes `title`, `author`, and `year`. Add a method `is_published_in_21st_century` to check if the book was published after 2000.


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def is_published_in_21th_century(self):
        if self.year > 2000:
            return True
        return False

b1 = Book("Book Title", "Book Author", 2000)
result = b1.is_published_in_21th_century()
print(result)



