class Car():
    """Class to Create a Car"""
    def __init__(self, brand, model, year, mileage, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price

    def show_car(self):
        """Prints all parameters"""
        description = ("\nBrend: " + self.brand + "\nModel: " + self.model + "\nYear: " + str(
            self.year) + "\nMileage: " + str(self.mileage) + "km" + "\nPrice: " + str(
            self.price) + "$").title()
        print(description)

    def aprox_price(self):
        self.price -= 1000
        print("Next year" + " " + self.brand + " " + "will cost " + str(self.price) + "$")

#manual price values
#def future_price(self, new_price):
#       """Future price"""
#        self.price = new_price
#        print("Next year" + " " + self.brand + " " + "will cost " +str(new_price) + "$")


class SuperCar(Car):
    """Class to create s SuperCar"""
    def __init__(self, brand, model, year, mileage, price, rarity, condition):
        super().__init__(brand, model, year, mileage, price)
        self.rarity = rarity
        self.condition = condition

    def aprox_price(self):
        self.price += 10000
        print("Next year" + " " + self.brand + " " + "will cost " + str(self.price) + "$")

    def show_car(self):
        description = ("\nBrend: " + self.brand + "\nModel: " + self.model + "\nYear: " + str(self.year) + "\nMileage: " + str(self.mileage) + "km" + "\nPrice: " + str(
            self.price) + "$" + "\nRarity: " + self.rarity + "\nCondition: " + self.condition).title()
        print(description)


mycar1 = Car("Skoda", "Karoq", 2018, 52000, 23500)
mysupercar = SuperCar("Lamborghini", "Liura", 1969, 8000, 250000, "Legend", "New")

mycar1.show_car()
mycar1.aprox_price()
mysupercar.show_car()
mysupercar.aprox_price()

#mycar1.future_price(25000)
#mysupercar.future_price(450000)
