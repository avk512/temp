# �������� ����� (� ��������������� ��������)
from pprint import pprint
import sys

# CSV
# �������������� � Excel, ����� ���������������� ������ ��� ���������� ������ � ��������.
# ������ ������� ������� �����
# ������� ������ �� ������ ������, �.�. ���� ����� ���������� ���������
import csv

with open("files/flats.csv", newline="") as datafile:
    flats_csv = csv.reader(datafile, delimiter=";")
    flats_list = list(flats_csv)
print(flats_list[:5])


def read_by_one():
    with open("files/flats.csv", newline="") as datafile:
        flats_csv = csv.reader(datafile, delimiter=";")
        for flat in flats_csv:
            yield flat


iter_flats = iter(read_by_one())
for row in iter_flats:
    print(row[0])

# csv DictReader
# https://docs.python.org/3/library/csv.html#csv.DictReader

with open("files/flats.csv", newline="") as datafile:
    flats_csv = csv.DictReader(datafile, delimiter=";")
    for i, flat in enumerate(flats_csv):
        print(flat["�����"], flat["���������� ������"], flat["����"])
        if i == 5:
            break
# csv ��������� ��������������
# https://docs.python.org/3/library/csv.html#csv-fmt-params
csv.register_dialect('customcsv', delimiter=',', quoting=csv.QUOTE_MINIMAL,
                     quotechar='"', escapechar='\\')
with open("files/flats2.csv", "w") as datafile:
    datafile_csv = csv.writer(datafile, 'customcsv')
    datafile_csv.writerows(flats_list[:5])

# JSON
# ��� ������ ������� � �� (BSON - ��� MongoDB)
# https://stackoverflow.com/questions/39719689/what-is-the-difference-between-json-load-and-json-loads-functions-in-python
# https://docs.python.org/3/library/json.html
import json

with open("files/newsafr.json") as datafile:
    json_data = json.load(datafile)
print(json_data)
pprint(json_data)

# json ensure_ascii=False - ����� �������� ���������� ��������� ��� � ����� ����:
# "\u0441\u0438\u0441\u0442\u0435\u043c\u0430 \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438 \u043f\u0438\u0449\u0435\u0432\u044b\u0445 \u043a\u043e\u043c\u043f\u043e\u043d\u0435\u043d\u0442\u043e\u0432"
# ��������� ������� ����� ������ ����� � https://dencode.com/string/unicode-escape

with open("files/newsafr2.json", "w") as datafile:
    json.dump(json_data, datafile, ensure_ascii=False, indent=2)
print(json_data)

# YAML
import yaml

with open("files/newsafr.yml") as datafile:
    yaml_data = yaml.load(datafile)
    pprint(yaml_data)

with open("files/newsafr2.yml", "w") as datafile:
    yaml.dump(yaml_data, datafile, allow_unicode=True, default_flow_style=False)

# XML
# �������� Microsoft. ����� ������������ ��� ������ ������� � ��������
# � XML (� ����������� �� ��� �������� SOAP), � JSON ������� ������������ ��� �������� API. �� �������� ���������� � ��������� � �������������: https://habr.com/company/sberbank/blog/421693/
# ���������� �� ��� ����� ��� ������ ���� ���������� ������ ������ � ������� XML (������ ��� ���������������� ������������) http://cbr.ru/development/

# ������ XML
# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET

# ���� ����� �������� � ����������, ������� ����� ������� ������ � ���� ������ ��������� �����
parser = ET.XMLParser(encoding="utf-8")
# ����������� ������ ��� ������� xml
tree = ET.parse("files/newsafr.xml", parser)
titles = []
# ��� ����� �������� ������� xml
root = tree.getroot()
# ���� � ��������
print(root.tag)
print(root.attrib)
# ����� � XML
xml_title = root.find("channel/title")
print(type(xml_title))
print(xml_title.text)
xml_items = root.findall("channel/item")
print(len(xml_items))
for xmli in xml_items:
    print(xmli.attrib["id"])

# # ��� ����� XML DOM
# # https://ru.wikipedia.org/wiki/Document_Object_Model
# # �������� �������� ���� <title> ����� ������ � �����
# for item in xml_items:
#   title = item.find("title")
#   titles += title.text.split(" ")
#   # �������� �������� ���� - ������� text
#   print(title.text, "\n")

# # ������� ���������� ���� � ������ �� �����
# # ��������� https://habr.com/post/138535/
# def sortByLength(inputStr):
#         return len(inputStr)

# titles.sort(key=sortByLength, reverse=True)
# print(titles)

# ���������
# encoding="utf_8_sig"
# encoding="utf_8"
# encoding="cp1251"
