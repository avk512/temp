import json
import xml.etree.ElementTree as ET
from pprint import pprint
from collections import Counter

filename_json = "newsafr.json"
filename_xml = "newsafr.xml"

##############################
# ЗАДАЧА №1 (для json файла) #
##############################
# with open(filename_json, encoding="utf-8-sig") as f:
#     json_content = json.load(f)
#     data = json_content['rss']['channel']['items']
#     txt = [desc['description'] for desc in data]  # получаем список описаний
#
# # получаем список всех слов из описаний
# allwordslist = ' '.join(txt).split()
#
# # создаем список слов длиннее 6 символов и у каждого слова первую букву делаем прописной (для корректности подсчета)
# # wordslist = [word.capitalize() for word in allwordslist if len(word) >= 6]
# # без изменения первых букв (результат несколько другой)
# wordslist = [word for word in allwordslist if len(word) >= 6]
#
# 1) решение задачи с помощью модуля Counter
# wdc = Counter(wordslist)
# wl = Counter(wordslist).most_common(10)
# for s in wl:
#     print(f"Слово '{s[0]}' встретилось в тексте {s[1]} раз(а)")
#
# 2) решение задачи без использования модуля Counter смотрите ниже в примере для xml-файла

##############################
# ЗАДАЧА №2 (для xml файла) #
##############################

tree = ET.parse(filename_xml)
root = tree.getroot()
items = root.findall("channel/item")

txt = []
for item in items:
    txt.append(item.find('description').text)

allwordslist = ' '.join(txt).split()

wordslist = [word for word in allwordslist if len(word) >= 6]

# 2) решение задачи без использования модуля Counter
words_count = {}
for word in wordslist:
    words_count[word] = wordslist.count(
        word)  # создаем словарь с парами: слово: количество


# функция выбора 2-го значения из кортежа (с количеством-частотой упоминания слова)
def mysort(tuple):
    return tuple[
        1]  # возврат из кортежа 2-го значения (частота упоминания слова)


# функция sorted возвращает из словаря список кортежей, которые сортируются по частоте упоминания слова
wrd = sorted(words_count.items(), key=mysort, reverse=True)
sl = wrd[0:10]  # срез кортежа от первого значения до 10 включительно
for i in sl:
    print(f"Слово '{i[0]}' встретилось в тексте {i[1]} раз(а)")
