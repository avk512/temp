import json
from pprint import pprint

# with open("newsafr.json", encoding='utf-8-sig') as f:
#     json_data = json.load(f)
#
# # pprint(json_data)
#
# data = json_data["rss"]["channel"]
# # pprint(data)
#
# with open("channel_content.json", "w") as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)
#
# print("Выполнено!")

import csv

# flat_list = list()
# csv.register_dialect("customcsv", delimiter=",", quoting=csv.QUOTE_ALL, quotechar = '"', escapechar = "\\")
# with open("output.csv", newline="") as f:
#     reader = csv.reader(f, delimiter=";")
#     flat_list = list(reader)
#
# # pprint(flat_list[:3])
#
# with open("flats.csv", "w") as f:
#     writer = csv.writer(f, "customcsv")
#     writer.writerows(flat_list)


# with open("output.csv", newline="") as f:
#     reader = csv.DictReader(f, delimiter=";")
#     for flat in reader:
#         pprint(f"Цена в рублях: {flat['Цена (руб)']}")


import xml.etree.ElementTree as ET

tree = ET.parse("newsafr.xml")
root = tree.getroot()
# print(root.tag)
# print(root.attrib)
# print(root.text)

items = root.findall("channel/item")
print(len(items))
# print(items)
for item in items:
    print(item.find("description").text)
# print(items[1])
# print(items[1].find("description").text)
