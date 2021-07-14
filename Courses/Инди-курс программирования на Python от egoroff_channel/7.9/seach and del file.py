import os

path = 'E:\Х3000\Clip'

for el in os.listdir(path):
    if el[-4:] == '.XML':
        os.remove(path + '\\' + el)




