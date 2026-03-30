#This program is used to understand the magic methods in python.

class Book:
    def __init__(self,author,title,year,price):
        self.author=author
        self.price=price
        self.title=title
        self.year=year
        self._discount=5

    #This magic method is for printing string representation of a given object which is expected to be end-user friendly.
    def __str__(self):
        return f"{self.title} written by {self.author} in {self.year} costs {self.price} dollars."
    
    #This magice methos is mostly for developers if they want to print any specific details about the object.
    #If the method is not defined, we generally id of the object in hex format.
    def __repr__(self):
        return self.__dict__
    
    #This method is called when we try to retrieve any attribute from the object and this can be used to pre-process any data
    #before sharing the attribute.
    def __getattribute__(self, name):
        if name=="price":
            return super().__getattribute__(name)*(1-(0.01*self._discount))
        else:
            return super().__getattribute__(name)

    #This method is invoked if the attribute wasn't found the usual ways. It's good for implementing a fallback for missing attributes.
    def __getattr__(self, name):
        return f"{name} - This attribute doesnot exist."
    
    #This method is used for comparison operator equalsto('=')
    def __eq__(self, value):
        if self.author==value.author and self.title==value.title and self.price==value.price and self.year==value.year:
            return True
        else:
            return False
        
    #This method is used for comparions operator greater than('>')
    def __gt__(self, other):
        if self.price>other.price:
            return True
        else:
            return False
    
    #This method is used to call objects like functions.
    def __call__(self, author,title,year,price):
        self.author = author
        self.title = title
        self.year = year
        self.price = price

book1 = Book("CLRS","Introduction to Algorithms",1996,100)
book2 = Book("Benjamin Graham","Intelligent Investor",1956,200)
book3 = Book("CLRS","Introduction to Algorithms",1996,100)
print(book1)
book1("Al-Khwarizmi","Algorithms",1016,1)
print(book1)
#print(book2)
#print(book1==book2)
#print(book1==book3)
#print(book1>book2)
#print(book2>book3)
#print(book1.__str__())
#print(book1.__repr__())
#print(book1.__dict__)
#print(book1.review)
