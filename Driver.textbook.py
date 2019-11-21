# Ben Lizza
# 11/20/19
# Driver for the Textbook module
# create two textbooks that the user will input. Have a menu to let the user pick one of three things to do with the textbook

from Module_textbook import Textbook


def textbook1():
    print("""Enter the title of the textbook, author, edition, ISBN number, publisher, 
    year published, inventory amount, and price.""")
    print("Type RETURN/ENTER after each input")
    Textbook(title=input(), author=input(), edition=input(), isbn_number=input(), publisher=input(), year_published=input(), inventory=input(), price=input())
    print(Textbook)


textbook1()
