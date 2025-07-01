

while(True):
    email = input('Пожалуйста, введите адрес электронной почты: ')
    if (email.endswith('@kpfu.ru') == 0):
        print('Требуется указать адрес в доменной зоне kpfu.ru')
    else:
        break

while(True):
    password = input('Пожалуйста введите новый пароль:')
    condition_a = False
    condition11 = 0
    for sym in password:
        if 33 <= ord(sym) and ord(sym) <= 38:
            condition_a = True
        if 33 <= ord(sym) and ord(sym) <= 38 or 48 <= ord(sym) and ord(sym) <= 57 or 65 <= ord(sym) and ord(sym) <= 90 or 97 <= ord(sym) and ord(sym) <= 122:
            condition11 += 1
    condition_1 = condition11 == len(password)
    for_cond2 = [j for j in password if 65 <= ord(j) and ord(j) <= 90 or 97 <= ord(j) and ord(j) <= 122]
    condition_2 = not password.islower() and len(for_cond2) > 0
    for_cond3 = [x for x in password if 48 <= ord(x) and ord(x) <= 57]
    condition_3 = not password.isalpha() and len(for_cond3) > 0
    condition_4 = len(password) > 7
    condition = condition_a and condition_1 and condition_2 and condition_3 and condition_4
    count = 3
    if condition:

        f = False
        while count != 0:
            password2 = input('Повторите введенный пароль: ')
            if password2 == password:
                print('Вы успешно прошли регистрацию')
                f = True
                break
            else:
                print(f'Пароли не совпадают, осталось {count - 1} попыток')
                count -= 1
        if f: break
    else:
        if not condition_1:
            print('Пароль содержит недопустимые символы')
        if not condition_2:
            print('Пароль должен иметь хотя бы 1 заглавную букву')
        if not condition_3:
            print('Пароль должен иметь хотя бы 1 цифру')
        if not condition_4:
            print('Длина пароля должна быть не менее 8 символов')
        if not condition_a:
            print("Пароль должен иметь хотя бы 1 из символов набора '!, “, #, $, %, &'")