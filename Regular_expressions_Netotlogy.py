from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)
pattern = r'(\+7|8){1}\s?\(?([0-9]{3})\)?\s?-?([0-9]{3})-?([0-9]{2})-?([0-9]{2})(\s?)\(?(доб.\s[0-9]{4})?\)?'
substitution = r'+7(\2)\3-\4-\5\6\7'

# корректная разбивка фио , замена телефона на правильный формат
for k in range(1,len(contacts_list)):
    fio = ' '.join(contacts_list[k][:3])
    contacts_list[k][5] = re.sub(pattern, substitution,contacts_list[k][5])
    for i in range(len(fio.split())):
        contacts_list[k][i] = fio.split()[i]
# заполнение пустых ячеек у дублей
for n in range(1,len(contacts_list)-1):
    for m in range(n+1,len(contacts_list)):
        if ' '.join(contacts_list[n][:2]) == ' '.join(contacts_list[m][:2]):
            for l in range(len(contacts_list[n])):
                if contacts_list[n][l] != contacts_list[m][l] and contacts_list[n][l] == '':
                    contacts_list[n][l] = contacts_list[m][l]
                else:
                    contacts_list[m][l] = contacts_list[n][l]

# избавляемся от дублей
new_contact_list = []
for i in contacts_list:
    if i not in new_contact_list:
        new_contact_list.append(i)


pprint(new_contact_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contact_list)