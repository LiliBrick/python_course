def sravnenie(a, b):

    if len(a) > len(b):
        print(len(a))
    elif len(b) > len(a):
        print(len(b))
    else:
        print("Списки одинаковой длины =", len(a))


sravnenie([1, 2, 3, 4, 3, 4, 5, 6], [1, 2])


