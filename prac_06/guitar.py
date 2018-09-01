class Guitar:
    CURRENT_YEAR = 2017
    VINTAGE_AGE = 50

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self, name, year, cost):
        print("{} ({}) : ${:,.2f}".format(name, year, cost))

    def get_age(self):
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age(self) >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars by year released."""
        return self.year < other.year
