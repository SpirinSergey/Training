
def new_dir():
    import os
    name_dir = input('Название новой папки:\n')
    for i in range(int(input("Сколько создать папок?\n"))):
        new_d = os.path.join(os.getcwd(), name_dir + "_" + str(i + 1))
        os.mkdir(new_d)


new_dir()

