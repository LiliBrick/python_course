lst = [2, 4, 5, 8, 9, 13]
a = 0
while a < len(lst):
    lst[a] *= a
    a += 1
    print(lst)