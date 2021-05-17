# script for collatz function

def collatz(number):

    if number % 2 == 0:
        result = number // 2
        print(result)
        return result

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


number = int(input("Please enter a number: "))

while number != 1:
    number = collatz(number)

