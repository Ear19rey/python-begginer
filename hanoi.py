def hanoi(n, start, finish ,temp):
    global counter
    if n==1:
        counter += 1
        print("%d:Move disk from %s to %s"%(counter, start, finish))
    else:
        hanoi(n-1, start, temp, finish)
        hanoi(1, start, finish, temp)
        hanoi(n-1, temp, finish, start)

counter = 0
hanoi(2,"A","C","B")
print()
counter = 0
hanoi(3,"A","C","B")
print('total moves: %d' % counter)
