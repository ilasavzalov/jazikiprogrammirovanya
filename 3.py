def is_number(text):
    try:
        int(text)
        return True
    except ValueError:
        return False
    
history = []

while True:
    line = input()
    if line == '' or line == 'exit':
        break
    elif line == 'clear':
        history.clear()
    elif line == 'history':
        for i in history:
            print(i)
    else:
        a = line.split()
        if len(a) == 3 and is_number(a[1]) and is_number(a[2]):
            if a[0] == '+':
                r = int(a[1]) + int(a[2])
            elif a[0] == '-':
                r = int(a[1]) - int(a[2])
            elif a[0] == '*':
                r = int(a[1]) * int(a[2])
            elif a[0] == '/':
                r = int(a[1]) / int(a[2])
            else:
                print('Ошибка ввода')
                continue
            print('Результат:', r)
            history.append(line + ' = ' + str(r))
        else:
            print('Ошибка ввода')
            continue
