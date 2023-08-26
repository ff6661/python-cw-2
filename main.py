my_name = input('whats your name? ')
my_age = input('how old are you? ')
print(f'my name is {my_name} an i am {my_age} years old')

first_number = int(input("choose a number: "))
second_number =int(input("choose another number: "))
operation = input('choose an operator: ')
if operation == '+' :
    print(first_number + second_number)
elif operation == '-' :
    print(first_number - second_number)
elif operation == "*" :
    print(first_number * second_number)
elif operation == "/" :
    print(first_number / second_number)
else :
    print("the operation is invalid ")

bus_capacity = 30
passengers = int(input("how many people are in the bus? "))
people_wanting_to_get_in = int(input("how many persons want to use the bus? "))
empty_seats = bus_capacity - passengers

if empty_seats > people_wanting_to_get_in :
    print("there are available seats")
elif empty_seats <= people_wanting_to_get_in :
    print(f"the bus is full only {empty_seats} seats are available right now :/ ")
    