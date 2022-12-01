# Write code for algorithm 1 below
def countDown(i):
    if i == 0:
        return
    else:
        print(i)
        countDown(i-1)


i = 8
countDown(i)
