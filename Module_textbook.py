# Ben Lizza
# 11/20/19
# Module that will include a Person class and a Textbook that will use Person class in author

from Textbook_Program import Person

#there is no inheritance, think back to the is-a relationship and you will see that this does not fit.
class Textbook():
    def __init__(self,title, first, last, age, edition, isbn_number, publisher, year_published, inventory, price):
        self.title = title
        #what we are doing is saying that the Textbook has an author that is a person, so make a Person object
        self.author = Person(first, last, age)
        self.edition = edition
        self.isbn = isbn_number
        self.publisher = publisher
        self.year_published = year_published
        self.inventory = inventory
        self.price = price

    #thisis to add to inventory, you also need one to remove.  Not the same process to remove, but similar    
    def add_to_inventory(self, quantity)
        self.inventory = self.inventory + quantity
        
#What other methods?  Think about what you need for the project.
