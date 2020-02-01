# data = {
#     "123": {"name": "Иванов", "email": "email@mail.ru"},
#     "321": {"name": "Петров", "email": "yandex@mail.ru"},
#     "432": {"name": "Василий", "email": "google@mail.ru"}
# }

# for key, val in data.items():
# print(key,':', val)
# print(val.get('name'), ':', val.get('email'))

# my_str = "ok ret. pert"
# print(my_str.rpartition('.'))

# s = "Today is a good day"
# print(s.partition("good"))

# str = "Я недаром вздрогнул, не загробный вздор, в порт, горящий как расплавленное лето, разворачивался и входил товарищ Теодор Нетте"
# print(str.partition(','))
#
# example = {"count": "5", "list": [
#     {"Name": "name1", "Surname": "surname1", "Age": "age1"},
#     {"Name": "name2", "Surname": "surname2", "Age": "age2"},
#     {"Name": "name3", "Surname": "surname3", "Age": "age3"},
#     {"Name": "name4", "Surname": "surname4", "Age": "age4"},
#     {"Name": "name5", "Surname": "surname5", "Age": "age5"}
# ]}

# Найти словарь по значению ключа "surname5"
# def func():
#     for dic in example["list"]:  # для любого элемента (вложенного словаря в списке) в словаре с ключем 'list':
#         if "Surname" in dic and dic[
#             "Surname"] == "surname3":  # если ключ 'Surname' есть в элементе (словаре) и название ключа совпадает со
#             # строкой 'surname3':
#             return dic  # возвращаем найденный словарь
#
# def func2():
#     for dic in example["list"]:  # для любого элемента (вложенного словаря в списке) в словаре с ключем 'list':
#         if "Surname" in dic and dic[
#             "Age"] == "age1":  # если ключ 'Surname' есть в элементе (словаре) и название ключа совпадает со
#             # строкой 'surname3':
#             return dic  # возвращаем найденный словарь
#
# print(func2())


# result = next(d['Age'] for d in example['list'] if d.get('Surname') == 'surname3')
# print(result)

# mytuple = ("яблоко", "банан", "вишня")
# myIt = iter(mytuple)
# print(next(myIt))
