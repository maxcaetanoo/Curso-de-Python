x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
fim = len(x)-1

for i in range(len(x)//2):
    init = x[i]
    x[i] = x[fim]
    x[fim] = init
    fim -= 1    

print(x)
