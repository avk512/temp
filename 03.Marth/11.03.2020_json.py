import json
from pprint import pprint

# student = {
#     'first_name': 'Greg',
#     'last_name': 'Dean',
#     'scores': [70, 80, 90],
#     'description': 'Good job, Greg!',
#     'certificate': True
# }
# #  запись данных в виде словаря в файл формата json
# with open("student.json", "w", encoding="utf-8") as f:
#     json.dump(student, f, indent=2, ensure_ascii=False)
#
# # чтение из файла формата json
# with open("student.json", encoding="utf-8") as f:
#     json_data = json.load(f)
#     # pprint(json_data)
#     print(json_data['scores'][0])

with open("newsafr.json", encoding="utf-8") as f:
    json_data = json.load(f)

# pprint(json_data)

data = json_data['rss']['channel']['items']
# pprint(data)
with open("items.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
