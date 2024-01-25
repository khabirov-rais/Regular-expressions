from pprint import pprint
import csv
import re


# # TODO 1: выполните пункты 1-3 ДЗ
def get_contact_name(contacts_list):
    for contact in contacts_list[1:]:
        full_name = contact[0] + contact[1] + contact[2]
        name = re.sub('([А-Я])', r' \1', full_name).split()
        if len(name) == 3:
            for i in range(3):
                contact[i] = name[i]
        elif len(name) == 2:
            contact[0] = name[0]
            contact[1] = name[1]
            contact[2] = ''
        elif len(name) == 1:
            contact[0] = name[0]
            contact[1] = ''
            contact[2] = ''
    return contacts_list

def get_phone_number(contacts_list):
    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'
    for contact in contacts_list:
        contact[5] = phone_pattern.sub(phone_substitution, contact[5])
    return contacts_list


def fined_duble():
    contact_list = {}
    for contacts in contacts_list[1:]:
        last_name = contacts[0]
        if last_name not in contact_list:
            contact_list[last_name] = contacts
        else:
            for id, item in enumerate(contact_list[last_name]):
                if item == '':
                    contact_list[last_name][id] = contacts[id]

    for last_name, contact in contact_list.items():
        for contacts in contact:
            if contact not in contacts_list_updated:
                contacts_list_updated.append(contact)
    return contacts_list_updated




# читаем адресную книгу в формате CSV в список contacts_list
with open(r'C:\Users\*\Documents\VSC project\Regular expressions\phonebook_raw.csv', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  contacts_list_updated = [contacts_list[0]]
  get_contact_name(contacts_list)
  get_phone_number(contacts_list)
  fined_duble()


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open('phonebook.csv', 'w', encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)


