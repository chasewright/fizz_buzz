import time
import sys
# first attempt at fizzbuzz
#define range of integers

#where the script is located
print("The name of this script is {}".format(sys.argv[0]))

#let the user read before being questioned
time.sleep(2)


while True: 
    try:
        max_n = int(input("Please enter an integer less than 250 "))
    except Exception:
        print("Please enter a value integer")
        continue
    else:
        break
    
max_n = max_n + 1

numbers = range(1,max_n)
    
#let everyone know what we will we be counting to
print("""Fizz buzz counting up to {}. Please hold while we calculate
        """.format(max(numbers)))

time.sleep(2)

for n in numbers:
    if (n % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")
    elif (n % 3 == 0):
        print("Fizz")
    elif (n % 5 == 0):
        print("Buzz")
    else:
        print(n)








