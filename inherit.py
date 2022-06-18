class vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print('i am a vehicle')
        print('mileage of vehicle', self.mileage)
        print('cost of vehicle ', self.cost)


v = vehicle(65,500)
v.show_details()


class Car(vehicle):
    def show_car(self):
        print('i am car')


c1 = Car(200,100)
c1.show_car()