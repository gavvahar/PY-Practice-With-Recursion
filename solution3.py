# Write code for algorithm 3 below
def fibonacci(number):
    if number <= 1:
        return number
    else:
        return (fibonacci(number - 1) + fibonacci(number - 2))


number = 10
for i in range(number):
    print(fibonacci(i))
