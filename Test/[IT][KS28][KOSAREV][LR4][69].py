import math

print("\t\t\tLR4\nz1 var20\nz2 var30\nz3 var11\n\n\t\tZ1:\n")
a, b, c = int(input()), int(input()), int(input())
d = (b ** 2) - (4 * a * c)
print("Квадратное уравнение: ", "(", a, ")x^2", "+(", b, ")x+(", c, ")")
if d < 0:
    print("D=", d, "\tКорней нет.")
else:
    x1 = (-b + (pow(d, 0.5))) / (2 * a)
    x2 = (-b - (pow(d, 0.5))) / (2 * a)
    print("D=", d, "\nx1=", x1, "\nx2=", x2)

print("\n\t\tZ2:\n")
spisok = []
for u in range(100, 1000):
    for v in range(100, 1000):
        j = u * v
        if str(j) == str(j)[::-1]:
            spisok.append(j)
print(*spisok, sep='\n')

print("\n\t\tZ3:\n")
x, y, z = 3, 4, 5
while 3 <= x <= 7:
    a = 10 * math.log(x - pow(math.cos(y), 2)) * (z - ((y * y) / (x - (x * x) / 2)))
    b = (2 * (x ** 3)) + (math.fabs((y * y) - (3 * (z ** 3))) / math.exp((3 * x) + (y * y)))
    print("x=", x, "\tF1+F2=", round(a + b, 1), "\n")
    x = round(x + 0.1, 1)
