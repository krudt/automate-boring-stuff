# script for collatz function including input validation
import sys

# defining the function
def collatz(number):

    if number % 2 == 0:
        result = number // 2
        print(result)
        return result

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

# Input validation
while True:
    try:
        number = int(input("Please enter a number: "))
        break
    except ValueError:
        print('Please enter a valid integer!')
        continue
    except KeyboardInterrupt:
        print('Try again later!')
        sys.exit()

while number != 1:
    number = collatz(number)

