class Film():
    def __init__(self, title, year):
        self.title = title
        self.year = year
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __repr__(self):
        return f"Film: {self.title}, {self.year}"