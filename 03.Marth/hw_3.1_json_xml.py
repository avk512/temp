import json
import xml.etree.ElementTree as ET
from pprint import pprint
from collections import Counter

filename_json = "newsafr.json"
filename_xml = "newsafr.xml"


def json_parsing(file):
    with open(file, encoding="utf-8-sig") as f:
        json_content = json.load(f)
        data = json_content['rss']['channel']['items']
        txt = [desc['description'] for desc in data]
    allwordslist = ' '.join(txt).split()
    wordslist = [word.capitalize() for word in allwordslist if len(word) >= 6]
    return wordslist


def xml_parsing(file):
    tree = ET.parse(file)
    root = tree.getroot()
    items = root.findall('channel/item')
    txt = []
    for item in items:
        txt.append(item.find('description').text)
    allwordslist = ' '.join(txt).split()
    wordslist = [word.capitalize() for word in allwordslist if len(word) >= 6]
    return wordslist


def words_with_Counter(func_parsing):
    """Функция выборки слов с использованием модуля Counter"""
    wl = Counter(func_parsing).most_common(10)
    for s in wl:
        print(f"Слово '{s[0]}' встретилось в тексте {s[1]} раз(а)")


def words_dict(func_parsing):
    """Функция создания словаря с парами 'слово: количество'"""
    words_count = {}
    for word in func_parsing:
        words_count[word] = func_parsing.count(word)
    return words_count


def mysort(tuple):
    """Функция сортировки кортежа"""
    return tuple[1]


def words_sort(func_dict, func_tuple):
    """Функция выборки слов без использования модуля Counter"""
    wrd = sorted(func_dict.items(), key=func_tuple, reverse=True)
    sl = wrd[0:10]
    for i in sl:
        print(f"Слово '{i[0]}' встретилось в тексте {i[1]} раз(а)")


a = json_parsing(filename_json)
b = xml_parsing(filename_xml)
c = words_dict(a)
d = words_dict(b)

print("Выборка слов при парсинге JSON-файла (используем модуль Counter:)")
words_with_Counter(a)
print()
print("Выборка слов при парсинге XML-файла (используем модуль Counter:)")
words_with_Counter(b)
print()
print("Выборка слов при парсинге JSON-файла (вручную):")
words_sort(c, mysort)
print()
print("Выборка слов при парсинге XML-файла (вручную):")
words_sort(d, mysort)
