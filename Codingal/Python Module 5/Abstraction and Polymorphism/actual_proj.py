from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def fuel_type(self):
        pass
    @abstractmethod
    def max_speed(self):
        pass
class BMW(Car):
    def fuel_type(self):
        return "BMW: Uses Diesel/Petrol/Electric."
    def max_speed(self):
        return "BMW: Max speed is 250 km/h."
class Ferrari(Car):
    def fuel_type(self):
        return "Ferrari: Uses high-octane Petrol."
    def max_speed(self):
        return "Ferrari: Max speed is 350 km/h."
def display_car_info(car_object):
    print(car_object.fuel_type())
    print(car_object.max_speed())
    print("-" * 30)
bmw_car = BMW()
ferrari_car = Ferrari()
cars = [bmw_car, ferrari_car]
for car in cars:
    display_car_info(car)