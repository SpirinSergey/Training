
def new_file():
    name_file = input('Название создаваемого файла:\n')
    file_extension = input('Расширение файла:\n')
    num_file = int(input('Количество файлов:\n'))
    if num_file >= 2:
        for i in range(1, num_file + 1):
            f = open(name_file + '_' + str(i) + '.' + file_extension, 'w')
    else:
        f = open(name_file + '.' + file_extension, 'w')

new_file()