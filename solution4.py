# Write code for algorithm 4 below
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base*power(base, exp - 1)


print(power(4, 4))
