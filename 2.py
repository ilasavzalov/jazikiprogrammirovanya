n = int(input())
otl = []
hor = []
ud = []
neud = []
for i in range(n):
    s, b = input().split()
    b = int(b)
    if b < 60:
        neud.append(s)
    elif b < 75:
        ud.append(s)
    elif b < 90:
        hor.append(s)
    elif b < 101:
        otl.append(s)
print('Отлично:', ', '.join(otl))
print('Хорошо:', ', '.join(hor))
print('Удовлетворительно:', ', '.join(ud))
print('Неудовлетворительно:',  ', '.join(neud))
