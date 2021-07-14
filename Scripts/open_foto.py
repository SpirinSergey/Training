import os
import psutil
import keyboard


def open_fot(f):
    """Открывает фотографию. Принимает в качестве параметра имя файла"""
    os.system(f)


def stop_process(proc):
    """Завершает процесс. Принимает в качестве параметра имя процесса в системе"""
    for process in (process for process in psutil.process_iter() if process.name() == proc):
        process.kill()


file_list = os.listdir()

for el in file_list:
    if el[-4:].lower() == '.jpg':
        open_fot(el)
        keyboard.wait('Space')
        stop_process("Microsoft.Photos.exe")
