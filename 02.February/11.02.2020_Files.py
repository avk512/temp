# Вебинар к занятию "Открытие и чтение файла, запись в файл"

### Поиск искомой фразы в тексте (алгоритм)

# Завести счетчик
# Открыть файл на чтение
# читаем каждую строку
# если в строке есть Наташа и Пьер, то счетчик +1
# закрыть файл
# Напечатать результат

# counter = 0
# with open("warandpeace.txt", encoding="UTF-8") as f:
#     for line in f:
#         if 'Наташа' in line and 'Пьер' in line:
#             print(line)
#             counter += 1
#
# print(f"Наташа и Пьер упоминались в тексте вместе {counter} раз.")


# Подсчитать какой класс получил наилучшую среднюю оценку (файл grades.txt)
# заведем лучшую оценку = 0 и лучший класс пустой
# открыть файл
# циклом проходим по файлу "тройками (класс, оценки, пробел)"
# - считаем среднюю оценку
# - - разбиваем строку, суммируем все оценки и делим на общее количество оценок
# - - сравниваем среднюю оценку с лучшей оценкой
# - - - если выше: лучшая = средняя, обновляем лучший класс
# - - - если ниже: ничего не делаем
# закрыть файл
# напечатать результат

# best_grade = None
# best_rating = 0
#
# with open('grades.txt', encoding='UTF-8') as f:
#     while True:
#         grade = f.readline().strip()
#         if not grade:
#             print("Файл закончился")
#             break
#
#         rating = f.readline().strip()
#         # пустая строка
#         f.readline().strip()
#
#         rating_list = rating.split() # создает список из строки оценок
#
#         int_rating_list = []
#         for item in rating_list:
#             int_rating_list.append(int(item))
#
#         avg_rating = sum(int_rating_list) / len(int_rating_list)
#
#
#         # print(grade, '-->', rating_list)
#         # print(avg_rating)
#
#         # сравним среднюю оценку с лучшей
#         if avg_rating > best_rating:
#             best_rating = avg_rating
#             best_grade = grade
#
# print(f"Лучший класс {best_grade} с оценкой {avg_rating}")


# # ### Как писать в файл
# from datetime import datetime
#
# current_time = f"{datetime.now()}\n"
# print(current_time)
#
# # Если файл не существует, то при использовании атрибута "w", файл создается, а текст, содержащийся в файле, будет перезаписываться.
# with open("test_write.txt", "w", encoding="UTF-8") as f:
#     f.write(current_time)
#
# # Если файл не существует, то при использовании атрибута "a" файл создается, а текст будет добавляться в файл в конец.
# with open("test_append.txt", "a", encoding="UTF-8") as f:
#     f.write(current_time)
