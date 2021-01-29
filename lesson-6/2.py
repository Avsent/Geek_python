class Road:
    _square_meter = 25 * 5 / 1000

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def as_mass(self):
        as_mass = self._length * self._width * self._square_meter
        print(f'Масса асфальта для покрытия дорожного полотна составит: {round(as_mass)} т')


r = Road(5000, 20)
r.as_mass()
