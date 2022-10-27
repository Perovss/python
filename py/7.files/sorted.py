import os
from pprint import pprint


def files_to_file(files, file):
    res = file
    with open(file, 'w') as file_write:
        for value in files:
            # Запись наименование обрабатываеомго файла
            file_write.write(value[0]+'\n')
            # Запись количества строк в обрабатываем файле
            file_write.write(str(value[1])+'\n')
            # Запись содержимого, обрабатываемого файла
            with open(value[0]) as file_read:
                file_write.writelines(file_read.readlines())
                file_write.write('\n')
    return res


def len_files(files):
    output_data = {}
    for file in files:
        with open(file) as file_count:
            count = sum(1 for _ in file_count)
        output_data[file] = count
        res = sorted(output_data.items(), key=lambda x: x[1])
    return res


full_path = os.getcwd() + '/sorted'
#Получаем список файлов
files_to_read = [full_path + '/' + name for name in os.listdir(full_path)]

# Вывод на экран списка обрабатываемых файлов
print('\n--- СПИСОК ОБРАБАТЫВАЕМЫХ ФАЙЛОВ ---')
pprint(files_to_read)

# Подсчёт количества строк в файлах
files_dict = len_files(files_to_read)
# Вывод на экран количества строк в файлах
print('\n--- КОЛИЧЕСТВО СТРОК В ФАЙЛАХ ---')
pprint(files_dict)

# Вывод на экран результата объединения файлов
print('\n--- ОБЪЕДИНЕНИЕ ФАЙЛОВ ---')
pprint(f'Результат объедения файлов: {files_to_file(files_dict, "result.txt")}.')