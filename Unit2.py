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

""" x = True #is a factor 
y = True 

def GCF(x,y):
    if x == True and y == True:
        print("common factor") """
""" def vote(age, id):
    if age < 18 or id == False:
        print("cannot vote")
    elif age > 18 and id == True:
        print("you can vote") """

""" def skins(money, age, isAvailable):
    if money < 10 or age < 18 or isAvailable == False:
        return("cannot buy") """
""" def skins(money, cost, isAvailable):
    if isAvailable == True:
        if money >10 or cost == 0:
            print("can purchase")
        else:
            print("Lucas Broke Boy")
    else:
        print("not available")  """

""" def print_factors(x):
    print("the factors of",x, "are:")
    for i in range (1, x + 1):
        if x % i ==0:
            print(i)

num=60

print_factors(num)

def print_factor(y):
    print("the factors of",y, "are")
    for i in range(1, y + 1):
        if y % i ==0:
            print(i)

num = 320

print_factors(num)
 """

""" 
import math 
a = 100
b = 734
gcf = math.gcd(a, b)
print(f"the GCF of {a} and {b} is {gcf}") """

