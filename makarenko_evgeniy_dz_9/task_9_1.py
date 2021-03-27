import time
class TrafficLight:
    __color = None

    def running(self):
        while True:
            if self.__color == 'green' or self.__color == None:
                self.__color = 'red'
                print(self.__color)
                time.sleep(7)
                if self.__color == 'red':
                    self.__color = 'yellow'
                    print(self.__color)
                    time.sleep(2)
                    if self.__color == 'yellow':
                        self.__color = 'green'
                        print(self.__color)
                        time.sleep(5)
                    else:
                        raise Exception('Что-то идет не так, ожидаемый цвет "желтый"')
                else:
                    raise Exception('Что-то идет не так, ожидаемый цвет "красный"')
            else:
                raise Exception('Что-то идет не так, ожидаемый цвет "зеленый"')




a = TrafficLight()
b = TrafficLight()