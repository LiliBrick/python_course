def spisok(a):
    l = 0
    for i in a:
        if i > 0:
            l += 1
    print(l)

spisok([-1, 2, -3, 0, 8, 1])
