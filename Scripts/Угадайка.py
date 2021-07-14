from random import randint

user_number = input("Загадай число: \n")
user_put = None
comp_number = None
start_num = 1
end_num = 100

while True:
    comp_number = randint(start_num, end_num)
    print(f'Комп - {comp_number}')
    user_put = input("Ну?!\n")
    if user_put == "+":
        start_num = comp_number
    elif user_put == "-":
        end_num = comp_number
    elif user_put == "=":
        break
print('Утерся?!')


