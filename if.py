x = 23

if x == 25:
    print("yeah, you are right")
else:
    print("oh, no, wrong")

age = 28

if (age <= 4):
    print("you are baby")
elif (age > 4) and (age <= 15):
    print("you are kid")
elif (age >= 16) and (age < 21):
    print("teen")
else:
    print("adult")

print("----------------END---------------------")


all_cars = ("Audi", "BMW", "Cadillac", "Chrysler", "Chevrolet", "Fiat", "Ferrari", "Jeep", "Mercedes-Benz", "Porsche", "Lancia", "Geely", "Great_Wall", "Dong_Feng", "Chery")
german_cars = ("BMW", "Audi", "Porsche", "Mercedes-Benz")
italian_cars = ("Fiat", "Ferrari", "Lancia")
USA_cars = ("Cadillac", "Chrysler", "Chevrolet", "Jeep")

for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " " + "is German Car")
    if xxxx in italian_cars:
        print(xxxx + " " + "is Italian Car")
    if xxxx in USA_cars:
        print(xxxx + " " + "is USA Car")
#    else:
#        print(xxxx + " " + "Other")