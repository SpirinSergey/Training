# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

print("Введите номер буквы (от 1 до 26): ")
num = int(input())
alpha = num + 96
print(f'Это буква - "{chr(alpha).upper()}"')
