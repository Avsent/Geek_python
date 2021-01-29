class Sklad:

    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)

class Equipment:

    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)


sklad = Sklad()
scaner = Scaner('HP', 'HP-1', 2010)
sklad.add_to(scaner)
scaner = Scaner('HP', 'HP-2', 2012)
sklad.add_to(scaner)
printer = Printer('Sony', 'Sony-1', 100, 2020)
sklad.add_to(printer)
xerox = Xerox('X-1', 'Xerox', '2021')
sklad.add_to(xerox)
print(sklad._dict)
