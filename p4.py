# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2+3x |2. 3x^2+1x+8 Результат: 8x^2+4x+8

with open('m1.txt', 'r', encoding='utf-8') as f1:
    x = f1.readlines()
    s1 = str(x).strip('[]\'').split()

    with open('m2.txt', 'r', encoding='utf-8') as f2:
        x2 = f2.readlines()
        s2 = str(x2).strip('[]\'').split()

def Format(s):
    mylist = []
    f = s[-1]
    for i in range(0, len(s)):
        if i == 0:
            s[i] = int(s[i][:-3])
        if i == 2:
            s[i] = int(s[i][:-1])
        if f.isdigit():
            s[-1] = int(s[-1])
        mylist.append(s[i])  
  
Format(s1)
Format(s2)

max = s1
min = s2
if len(s1) < len(s2):
    max = s2
    min = s1
z = len(max) - len(min)
for i in range(0, z): min.append(0)

s3 = []
for i in range(0, len(max), 2):
    s3.append(max[i] + min[i])

print("№: 1 | " + str(x).strip('[]\''))
print("№: 2 | " + str(x2).strip('[]\''))
print("Sum  | " + f"{s3[0]}x^2 + {s3[1]}x + {s3[2]}")



