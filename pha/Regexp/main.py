import re
import csv

pattern_phone = r'(\+7|8)(\s)?(\()?(\d{3})(\))?(\s|-)?(\d{3})(-)?(\d{2})(\s|-)?(\d{2})(\s)?(\()?(доб. )?(\d+)?(\))?'
sub_phone = r'+7(\4) \7-\9-\11\12\14\15'
names_contact = {}
# Открытие файла
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# Исправление номеров телефонов
for contact in contacts_list:
    contact[5] = re.sub(pattern_phone, sub_phone, contact[5])
# Восстановление ФИО
    fio = contact[0] + ' ' + contact[1] + ' ' + contact[2]
    for index, value in enumerate(fio.split()):
        contact[index] = value


for record in contacts_list:
# id - идентификатор по которому будут объединяться записи
    id = record[0] + record[1]
# Получение списка дублируюмых записей
    new_record = names_contact.get(id, False)
# Если дубля нет - то оставляем список без изменений
    if not new_record:
        names_contact[id] = record
    else:
        for index, value in enumerate(record[2:], 2):
# Иначе перезаписаем списки с новым значениями в словаре
            if len(value) > 0 and value != new_record[index]:
                names_contact[id][index] += value
contacts_list = [record for record in names_contact.values()]

# Запись в файл
with open("phonebook.csv", "w") as f:
    data_writer = csv.writer(f, delimiter=',')
    data_writer.writerows(contacts_list)