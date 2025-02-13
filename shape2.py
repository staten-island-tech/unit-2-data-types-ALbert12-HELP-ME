""" print("test")
#def defines a function 
#inside the parenthesis are the inputs aka arguments 
def add(x,y):
    print(x+y)
    return(x+y)
    #print(x+y)
    #return creates an output for the function 
print(add(5+6)) """

""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)
print(values[0])
print(values[6])
 """
""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}")
 """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')
 """
#finding odd and even numbers
""" def check_even_odd():
    number = int(input("number:"))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_even_odd() """

""" def calculate_tip(bill, service_rating):
    # Set the tip percentages for different service ratings
    if service_rating == "bad":
        tip_percentage = 0
    elif service_rating == "okay":
        tip_percentage = 0.15
    elif service_rating == "good":
        tip_percentage = 0.20
    elif service_rating == "great":
        tip_percentage = 0.25
    else:
        print("Sorry, that service rating is not valid.")
        return

    # Calculate the tip amount
    tip = bill * tip_percentage

    # Show the results
    print(f"Your bill: ${bill:.2f}")
    print(f"Service rating: {service_rating}")
    print(f"Your tip: ${tip:.2f}")
    print(f"Total bill with tip: ${bill + tip:.2f}")

# Ask the user for the bill amount and service rating
bill = float(input("Enter the bill amount: $"))
service_rating = input("How was the service? (bad, okay, good, great): ").lower()

calculate_tip(bill, service_rating) """




