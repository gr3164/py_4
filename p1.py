# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

N = 60

def ListNumbers(N):
    mylist = []
    count = 2

    while True:
        if N % count == 0:
            N = N / count
            mylist.append(count)
            print(N)
        elif N % count != 0 and N > count: count += 1
        else: break
    return mylist
     
print(N, "-> " + str(ListNumbers(N))[1:-1].rstrip("[]"))   
