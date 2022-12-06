def divisor(n, g):
    if (g == 0):
        return n
    else:
        return divisor(g, n % g)


print(divisor(15, 18))
