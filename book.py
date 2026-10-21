class Book():
    def __init__(self, id, title, author):
        self.id = id
        self.author = author
        self. title = title

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Book{self.id}, {self.title}, by {self.author}"

