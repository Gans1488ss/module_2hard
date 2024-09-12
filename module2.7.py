def get_password(number):# Получить пароль - get_password
    password = ''   #пароль =
    for i in range(1, number):    # диапозон в i для (1, числа)
        for j in range(2, number):   #  диапозон в j для (2, числа)
            if j <= i:   # j <= i если
                continue   #  продолжить
            if number % (i + j) == 0:   # % числа если (i + j) == 0
                password += str(i) + str(j)   # str += пароль(i) +str(j)
    return password   # верните пароль

n = int(input('Введите целое число от 3 до 20: '))

result = get_password(n)   #  get_password - результат(n)
print('Пароль:', result)