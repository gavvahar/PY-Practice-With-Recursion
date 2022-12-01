# Write code for algorithm 2 below
def numbers(low, high):
    if low > high:
        return
    else:
        print(low)
        numbers(low + 1, high)


i = 8
numbers(1, i)
