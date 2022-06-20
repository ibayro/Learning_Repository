def welcome_message(name):
    """Print Welcome"""
    print(name + ", " + "Hello, Welcome to Python Function Lesson")


def summa(x, y):
    return x+y

def factorial(x):
    """Calculate Factorial of number X"""
    answer = 1
    for i in range(1, x + 1):
        answer = answer * i
    return answer


def create_record(name, telephone, address):
    """Create Record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record


def give_awards(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print("Pobratym " + " " + person.title() + " " + "otrimuye medal " + medal)


give_awards("For Kyiv", "Oleh", "Petro", "Ivan")
give_awards("For Sumy", "Alex", "Bohdan")

user1 = create_record("Ihor", "+38050000000", "Kyiv")
user2 = create_record("Alina", "+3809800000", "Krasnosillia")

welcome_message("Ihor")
welcome_message("Alina")

#summa(25, 100)
x = summa(25, 100)
print(x)

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))

print(user1)
print(user2)

def aaa():
    print("aaa")