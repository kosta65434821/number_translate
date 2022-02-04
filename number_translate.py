# сбор обрабатываемых данных
system = int(input("Enter number system: "))
number = list(input("Enter the number: "))
system_2 = int(input("Enter number system 2: "))

# вспомогательные переменные 
list_1 = [ ]
i = 0
j = 0

# вспомогательные функции:

# остаток от деления
def dil_1(x, y):
    return x % y
# целочисленное деление
def dil_2(x, y):
    return x // y
# преобразование чисел в буквы
def dil_3(x):
    if x > 32:
        raise SystemExit("dil_3")
    elif x > 9:
        return(chr(x + 55))   
    else:
        return (x)
# преобразование букв в числа
def dil_4(x, y, system):
    for j in x:
        try:
            y.append(int(j))
        except:
            i = ord(j) - 55
            dil_4_1(y, i, system)
    return(y)
# проверка чисел
def dil_4_1(y, i, system):
        if i in range(system):
        	y.append(i)
        else:
            raise SystemExit("dil_5")
# преобразование числа в список делением
def dil_5(number, system_2, i, list_1):
    i = number
    while i >= 1:
        list_1.append(dil_1(i, system_2))
        i = dil_2(i, system_2)
    return(list_1)

# основные функции

# из 10 системы исчисления в n
def block_1(number, system_2, list_1):
    i = 0
    dil_5(number, system_2, i, list_1)
    number = list_1.copy()
    i = 0
    for j in number:
        number[i] = dil_3(j)
        i += 1
    number = list(map(str, number))
    number.reverse()
    number = "".join(number)
    return(number)

# из n системы исчисления в 10
def block_2(number, system):
    dil_4(number, list_1, system) 
    number = list_1.copy()
    i = len(number)
    for j in range(i):
        list_1[j] = number[j]*(system**(i-(j+1)))
    number = list_1.copy()
    return(sum(number))

# системы исчисления менее 2 не поддерживаются
if system < 2:
    raise SystemExit("if")
# с помощью блоков переводит число
if system == 10:
    number = int("".join(number))
    g = block_1(number, system_2, i)
    print(g)
else:
    g = block_1(block_2(number, system), system_2, [ ])
    print(g)