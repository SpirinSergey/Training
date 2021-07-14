"""
BEEGEEK
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.

Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
Напишите функцию is_valid_password(password),
которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если
пароль является действительным паролем BEEGEEK банка и False в противном случае.

 Примечание. Следующий программный код:

print(is_valid_password('1221:101:22'))
print(is_valid_password('565:30:50'))
print(is_valid_password('112:7:9'))
print(is_valid_password('1221:101:22:22'))

должен выводить:

True
False
False
False
"""


# объявление функции
def is_valid_password(password):
    pas = password.split(':')
    if len(pas) != 3:
        return False
    if pas[0] != pas[0][::-1]:
        return False
    if len([i for i in range(1, int(pas[1])) if int(pas[1]) % i == 0]) > 2:
        return False
    if int(pas[2]) % 2 != 0:
        return False
    return True


# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))
