# Ben Lizza
# 11/20/19
# Module that will include a Person class and a Textbook that will use Person class in author

from Textbook_Program import Person


class Textbook(Person):
    def __init__(self,title, author, edition, isbn_number, publisher, year_published, inventory, price):
        self.title = title
        super(Person).__init__(first_name=author, last_name=author, age=author)
        self.edition = edition
        self.isbn = isbn_number
        self.publisher = publisher
        self.year_published = year_published
        self.inventory = inventory
        self.price = price

    def __init__subclass(self, add, subtract):
        self.add = add
        self.subtract = subtract
        adding_inv = self.inventory + 1
        subtracting_inv = self.inventory - 1
        if subtract:
            return subtracting_inv
        elif add:
            return adding_inv
