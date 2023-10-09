class Book:

    def __init__(self, title, author, quantity, borrows):
        self.title = title
        self.author = author
        self.quantity = quantity
        self.borrows = borrows

    def borrow() -> bool:
        available = True
        if self.quantity == 0:
            available = False
        else:
            self.quantity = self.quantity - 1
            self.prestamo = self.prestamo + 1
        return available
    
    def refund() -> bool:
        isBorrowed = True
        if self.borrows == 0:
            isBorrowed = False
        else:
            self.borrows = self.borrows - 1
            self.quantity = self.quantity + 1
        return isBorrowed
    
    def __str__(self):
        return "Title: " + self.title + " Author: " + self.author + " Quantity: " + self.quantity + " Borrows: " + self.borrows + "\n"
    
    def __eq__(self, obj) -> bool:
        equal = False
        if self.title == obj.title:
            equal = True
        return equal
    
    def __lt__ (self, obj) -> bool:
        lessThan = False
        if self.author < obj.author:
            lessThan = True
        return lessThan