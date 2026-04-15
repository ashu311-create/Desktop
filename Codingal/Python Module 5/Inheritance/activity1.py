class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage
class Bus(Vehicle):
    pass
school_bus=Bus("School Volvo",180,12)
print("Vehicle_name:", school_bus.name, "Speed:", school_bus.max_speed,"Milage:", school_bus.milage)