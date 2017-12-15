# Collatz Function Exercise

number = 0
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

print('Enter your number')
number = input(int())

while number != 1:
    number = collatz(number)
    print(number)