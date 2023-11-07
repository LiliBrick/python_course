def stroki(a):
    if type(a) == str:
        print(a[0], end='')
        for i in range(len(a)):
            if a[i] == ' ':
                print(a[i + 1], end='')
    else:
        print('oshibka')


stroki('Научно технический отчет')
