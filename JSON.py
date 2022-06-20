import json
filename = "car_settings.txt"
myfile = open(filename, mode='w', encoding='UTF-8')

car1 = {
    'CarName': "Skoda Karoq",
    'HP': 150,
    'Torque': 250,
    'Awards': ["Car of the Year", "Best SUV", "Family Car"]
}

car2 = {
    'CarName': "Honda CR-V",
    'HP': 170,
    'Torque': 300,
    'Awards': ["Best Japaneese Car", "Best Design", "AWD Car of the Year"]
}

mycars = []
mycars.append(car1)
mycars.append(car2)

json.dump(mycars, myfile)
myfile.close()

myfile = open(filename, mode='r', encoding='UTF-8')
json_data = json.load(myfile)

for user in json_data:
    print("Car Name list is " + str(user['CarName']))
    print("Number of Horse Powers: " + str(user['HP']))
    print("Torque: " + str(user['Torque']))
    print("Car Awards: " + str(user['Awards'][0]))
    print("Car Awards: " + str(user['Awards'][1]))
    print("Car Awards: " + str(user['Awards'][2]))