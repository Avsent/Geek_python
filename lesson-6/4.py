class Car:

    def __init__(self, name, speed, color, police_car=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.police_car = police_car

    def go(self):
        return f'The {self.name} went.'

    def stop(self):
        return f'\nThe {self.name} has stopped.'

    def turn(self, direction):
        return f'\nThe {self.name} turned {direction}'

    def show_speed(self):
        return f'\nSpeed of movement - {self.speed} km/h'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\n{self.speed} km/h - too fast! slow down!'
        else:
            return f'{self.name} km/h - speed is normal'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\n{self.speed} km/h - too fast! slow down!'
        else:
            return f'{self.name} km/h - speed is normal'


class PoliceCar(Car):
    pass


town = TownCar('LADA', 80, 'white')
print(town.go(), town.show_speed(), town.turn('left'), town.turn('right'), town.stop())

sport = SportCar('Ferrari', 150, 'red')
print('\n' + sport.go(), sport.show_speed(), sport.turn('left'), sport.stop())

work = WorkCar('UAZ', 30, 'green')
print('\n' + work.go(), work.show_speed(), work.turn('right'), work.stop())

police = PoliceCar('Chevrolet', 90, 'black', True)
print('\n' + police.go(), police.show_speed(), police.turn('right'), police.stop())
