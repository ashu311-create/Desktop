def Hotel_cost(nights):
    return 140*nights
def plane_cost(city):
    if "London" == city:
        return 183
    elif "Paris" == city:
        return  220
    elif "Berlin" == city:
        return 222
    elif "LA" == city:
        return 475
def car_rental_cost(days):
    if days>=7:
        return 40*days - 50
    elif days>=3:
        return 40*days - 20
    else: 
        return 40*days
def trip_cost (city, days,spending_money):
    return car_rental_cost(days) + Hotel_cost(days)+ plane_cost(city) + spending_money
print ("Cost of rental is", car_rental_cost(5))
print ("Cost of plane rides is", plane_cost("LA"))
print ("Cost of hotel room is", Hotel_cost(7))
print ("Total cost is", trip_cost("LA",7,500))
print (trip_cost ("Berlin",6,500))