class Book:

    def __init__(self, title, author, quantity, borrows):
        self.title = title
        self.author = author
        self.quantity = quantity
        self.borrows = borrows

    def borrow() -> bool:
        available = True
        if self.quantity <= 0:
            available = False
        else:
            self.quantity = self.quantity - 1
            self.prestamo = self.prestamo + 1
        return available
    
    def refund() -> bool:
        isBorrowed = True
        return isBorrowed