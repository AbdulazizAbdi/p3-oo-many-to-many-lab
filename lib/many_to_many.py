class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        royalties_count = [contract.royalties for contract in Contract.all if contract.author == self]
        total_royalty_amount = 0
        for royalty in royalties_count:
            total_royalty_amount = total_royalty_amount + royalty

        return total_royalty_amount


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.royalties = royalties
        self.date = date
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if not isinstance (author, Author):
            raise Exception("Not a valid instance of Author")
        self._author = author

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book):
        if not isinstance (book, Book):
            raise Exception("Not a valid instance of Book")
        self._book = book
    
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance (date, str):
            raise Exception("Not a valid string")
        self._date = date

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties):
        if not isinstance (royalties, int):
            raise Exception("Not a valid integer")
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        same_date_contracts = []
        for contract in cls.all:
            if contract.date == date:
                same_date_contracts.append(contract)
        
        return same_date_contracts