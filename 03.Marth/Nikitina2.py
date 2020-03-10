# исходный файл с данными Минфина скачан отсюда https://www.minfin.ru/opendata/7710168360-BanksID/
import xml.etree.ElementTree as ET

filename = "ICB_bank_guarantees.xml"
tree = ET.parse(filename)

root = tree.getroot()

# В данном случае "корень" - root - у вас будет выглядеть вот так:
# <BanksFk xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://budgetminfin.ru/banks/1">
# т.е. к тегу BanksFk в качестве аргументов добавлен неймспейс xmlns="http://budgetminfin.ru/banks/1"
# примечание: если вы видите xmlns:xsd и xmlns:xsi - это не сам неймспейс, это только его настройки, поэтому не обращайте внимания

# как работать с xml, если в нем есть неймспейсы

# ВАРИАНТ 1: подставляете неймспейс к каждому тегу,
# вот так: было banks - стало ns:banks, было bank - стало ns:bank и т.д.
ns = {"ns": "http://budgetminfin.ru/banks/1"}
banks = root.findall("ns:banks/ns:bank", ns)
print(len(banks))


# ВАРИАНТ 2: избавиться от неймспейсов. Вы можете либо вручную удалить их из исходного файла (но лучше так не делать), либо использовать функцию, которая удалит все неймспейсы из дерева
# дополнительно можно почитать здесь: https://homework.nwsnet.de/releases/45be/
def remove_namespace(doc, namespace):
    """Remove namespace in the passed document in place."""
    ns = u'{%s}' % namespace
    nsl = len(ns)
    for elem in doc.getiterator():
        if elem.tag.startswith(ns):
            elem.tag = elem.tag[nsl:]


# удаляем неймспейсы самописной функцией remove_namespace
remove_namespace(tree, "http://budgetminfin.ru/banks/1")
# работаем с xml, как привыкли
banks = root.findall("banks/bank")
print(len(banks))
