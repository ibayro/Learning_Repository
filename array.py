cities = ["Kyiv", "Lviv", "Odesa", "Baku", "London"] #array starts with 0

print(cities)
print(len(cities))
print(cities[2])
print(cities[-2]) #prints second city from the end of array

cities[1] = "Uman" #substitutes Lviv into Uman (second city of the array)
print(cities)
cities.append("Ternotyl") #append adds to the end of an array
print(cities)
cities.insert(1, "Uzh") #insert(1) adds Uzh after Kyiv
print(cities)
del cities[4] #delets 5th city
print(cities)
cities.remove("Uzh") #delets certain city
print(cities)
deleted_city = cities.pop()
print("deleted city is: " + deleted_city)

cities.sort() #sorts array in alphabetical order
print(cities)
#cities.sort(reverse=True)
#print(cities)
cities.reverse()
print(cities)

for x in cities:
    print(x.upper())

for x in range(1,6):
    print(x)

my_number_list = list(range(0, 5))
print(my_number_list)

for x in my_number_list:
    x = x * 2
    print(x)

my_number_list.sort(reverse=True)
print(my_number_list)

print("max number is " + str(max(my_number_list)))
print("minimal number is " + str(min((my_number_list))))
print("sum is " + str(sum(my_number_list)))

cars = ["skoda", "vw", "bently", "lamborghini", "seat", "cupra", "audi", "porsche"]
my_cars = cars[1:3] # 1 - starts with second from array, 3 - ends, does not include, so from our example is vw and bently
print(my_cars)
my_cars = cars[:3] #: starts from the beginning of an array
print(my_cars)
my_cars = cars[-2:]
print(my_cars)
my_cars = cars[:]
print(my_cars)
