car = {
    'Brand':  'Skoda',
    'Model':  'Karoq',
    'Year' :   2018,
    'Mileage': 1000,
}

print(car)
print("Car Name = " + (car['Brand']) + " " "Car Model = " + (car['Model']) + " " + "Year = " + str(car['Year']))

if car['Mileage'] <= 1000:
    car['Condition'] = 'Brand New'
elif car['Mileage'] > 1001:
    car['Condition'] = 'Decent'

print(car)

print(car.keys())
print(car.values())
print("------------------------END-------------------------")

all_cars = []

for x in range(0, 3):
    all_cars.append(car.copy())

for xx in all_cars:
    print(xx)

all_cars[1]['Year'] = 2020
print(all_cars)