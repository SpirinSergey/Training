
products: list = []
temp_dict: dict = {}
i: int = 0

while 1 < 2:
    temp_dict["Наименование"] = input("Введите наименование товара: ")
    temp_dict["Цена"] = input("Введите цену товара: ")
    temp_dict["Количество"] = input("Введите количество товара: ")
    temp_dict["Единицы"] = input("Введите единицы измерения товара: ")
    i = i + 1
    print(temp_dict)
    products.append(tuple([i, temp_dict]))

    if input("Продолжить? Y/N ") == "N":
        break

print(products)
