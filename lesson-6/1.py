import time

class TrafficLight:
    __color = ''

    def running(self):
        iter = 0
        while iter <= 2:
            self.__color = 'Красный'
            print(f'горит {self.__color} свет')
            for i in range(7, 0, -1):
                print('осталось гореть %d секунд' % i)
                time.sleep(1)
            iter += 1

            self.__color = 'Желтый'
            print(f'горит {self.__color} свет')
            for i in range(2, 0, -1):
                print('осталось гореть %d секунд' % i)
                time.sleep(1)
            iter += 1

            self.__color = 'Зеленый'
            print(f'горит {self.__color} свет')
            for i in range(5, 0, -1):
                print('осталось гореть %d секунд' % i)
                time.sleep(1)
            iter += 1


t = TrafficLight()
t.running()
