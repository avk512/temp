# my_list = ['a', 'b', 'c', 'd', 'f']
# my_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}

# print(my_list)
# print(my_dict)
# print()
# mystr = 'abcde'
# print(mystr[0])
# print(mystr[-1])
# print(mystr[len(mystr)-1])
# print(mystr[-2])

# mystr = [[1, 2, 3], ['a', 'b', 'c']]
# print(mystr[0])
# print(mystr[0][0])
# print(mystr[1][-1])

# mytuple = (1, 2, 3, 4, 5)
# print(mytuple[0])
# mytuple[0] = 100

# mylist = [1, 2, 3, [4, 5], 6]
# mylist[0] = 100
# mylist[-2][0] = 40
# print(mylist)
# mylist[6] = 7

# person = ('Alex', 'Smith', 'May', 10, 1980)
# Name, Birthday = slice(None, 2), slice(2, None)
# print(person[Name])
# print(person[Birthday])

# mylist = [1, 2, 3, 4, 5, 6, 7]
# Even = slice(None, 5, 2)
# print(mylist[Even])

# mylist = [1, 2, 3, 4, 5]
# mylist[1:2] = [20]
# print(mylist)

# mylist = [1, 2, 3, 4, 5]
# mylist[1:3] = [20, 30]
# print(mylist)
# mylist[1:3] = [0]
# print(mylist)
# mylist[2:] = [40, 50, 60]
# print(mylist)
# mylist[:2] = []
# print(mylist)
# mylist = [1, 2, 3, 4, 5]
# print(mylist[-10])
# print(mylist[10])
# print(mylist[0:10])
# print(mylist[10:100])

# mylist = [2, 5, 1, 7, 3]
# mylist_sorted = sorted(mylist)
# print(mylist_sorted)
# print()

# myset = {2, 5, 1, 7, 3}
# myset_sorted = sorted(myset, reverse=True)
# print(myset_sorted)
# print()

# myfiles = ['somecat.jpg', 'pc.png', 'apple.bmp', 'mydog.gif']
# mf_sorted = sorted(myfiles, key=len)
# print(mf_sorted)

# mylist = [2, 5, 1, 7, 3]
# mylist_sorted = reversed(mylist)
# print(mylist_sorted)
# print(list(mylist_sorted))
# print(mylist[::-1])

# mylist = [2, 5, 1, 7, 3]
# mylist.sort()
# print(mylist)
# print(mylist.sort())

# mydict = {'a':1, 'c':3, 'e':5, 'f':6, 'b':2, 'd':4}
# mysorted = sorted(mydict)
# print(mysorted)
# print()
# mysorted = sorted(mydict.items())
# print(mysorted)
# print()
# mysorted = sorted(mydict.values())
# print(mysorted)

# population = {"Shanghai":24256800, "Karachi":23500000, "Beijing":21516000, "Delhi":16787941}
# popsort = sorted(population.items(), key=lambda x: x[1])
# print(popsort)

# str1 = 'abc'
# str2 = 'de'
# str3 = str1 + str2
# print(str3)

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(a, b, c)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + [b]
# print(a, b, c)

# a, b = [1, 2, 3], [4, 5]
# c = [*a, *b]
# print(a, b, c)

# dict1 = {'a':1, 'b':2}
# dict2 = {'c':3, 'd':4}
# dict3 = {**dict1, **dict2}
# dict3 = dict1.copy()
# dict1.update(dict2)
# print(dict1)
# print(list(dict1.values()))
# print(list(dict1.items()))

# mydict = {}
# mydict[99] = 'spam'
# print(mydict)

# mylist = [1, 2, 3]
# mylist.insert(0, 0)
# print(mylist)

# mylist.insert(10, 4)
# print(mylist)

# mylist.insert(-10, -1)
# print(mylist)

# mylist.insert(1, 1.5)
# print(mylist)

# mylist = [1, 2, 3, 4, 5, 6, 7]
# del mylist[1]
# print(mylist)
# del mylist[-3:-1]
# print(mylist)

# mydict = {'a':1, 'b':2, 'c':3}
# del mydict['b']
# print(mydict)

# print(pow(5,3))

# lista = [-2, -1, 0, 1, 2, 3, 4, 5]
# listb = [x for x in lista if x % 2 == 0]
# listb = [x for x in lista if x % 2 == 0 and x > 0]
# listb = [x**2 for x in lista]
# lista = ['a', 'abc', 'abracadabra']
# listb = [len(x) for x in lista]
# print(listb)
# print(lista is listb)

# генератор списка
# [выражение for val in коллекция]

# import random

# a = [random.randint(-10, 10) for i in range(10)]
# print(a)

# #пример с использование синтетического сахара
# lista = [-2, -1, 0, 1, 2, 3, 4, 5]
# listb = [x if x < 0 else x**2 for x in lista]
# print(listb)
# #этот же пример в виде цикла
# listb = []
# for x in lista:
#     if x < 0:
#         listb.append(x)
#     else:
#         listb.append(x**2)
# print(listb)

# numbers = range(10)
# sq = [i**2 for i in numbers if i%2==0]
# print(sq)
# print()
# #
# sq = [
#     i ** 2
#     for i in numbers
#     if i % 2 == 0
# ]
# print(sq)
# print()
# #
# sq = []
# for i in numbers:
#     if i % 2 == 0:
#         sq.append(i ** 2)
# print(sq)

# lista = [-2, -1, 0, 1, 2, 3, 4, 5]
# mygen = sum(i for i in lista)
# print(mygen)

# a = input().split()
# a = [int(i) for i in a]
# print(a)

# n = 5
# m = 4
# a = [[0]*m for i in range(n)]
# a[4][3] = 300
# for i in a:
#     print(i)

# a = [(i,m) for i in 'abc' for m in [1, 2, 3]]
# print(a)

# a = [i*m for i in [2, 3, 4, 5] for m in [1, 2, 3] if i*m > 10]
# print(a)

# a = [
#     ('Sidorof', 1995),
#     ('Egorof', 1998),
#     ('Petrov', 1999),
#     ('Lukov', 2000),
#     ('Ivanov', 1997),
#     ('Efremov', 2005),
#     ('Gavrilov', 2000),
#     ('Gorbachev', 2001),
#     ('Kostin', 1994),
#     ('Isaev', 2002),
#     ('Kozlov', 1984),
# ]
# b = [i[0] for i in a if i[0].startswith('G')]
# b = [i[0][0] for i in a if i[1] > 2000]
# print(b)

# a = {
#     'Sidorof': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
#     'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
#     'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
#     'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
#     'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
#     'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
#     'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
#     'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
#     'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
# }
# b = [(elem, a[elem]['car']) for elem in a if a[elem]['age'] < 2000 and a[elem]['hobby'] == 'soccer']
# print(b)

# str = 'fkjiequ787dfiuqifj48tkkjk50jfiu7fjh46dnjfjbjvi8'
# number = [int(i) for i in str if i.isdigit()]
# print(number)

# import random
# n = 5 # строки
# m = 5 # столбцы
# a = [ [random.randint(1, 6) for j in range(m)] for i in range(n)]
# for i in a:
#     print(i)
# b = [a[i][j] for i in range(n) for j in range(m) if i == j]
# c = [a[2][j] for j in range(m)]
# print('цифры по диагонали: ', b)
# print('цифры из третьей строки:', c)

# b = [a[j][i] for i in range(n) for j in range(m) if i == j]
# c = [a[2][j] for j in range(n)]
# d = [a[i][3] for i in range(n)]
# print('цифры по диагонали: ', b)
# print('цифры из третьей строки:', c)
# print('цифры из четвертого столбца', d)

# n = 5 # строки
# m = 5 # столбцы

# a = [[i * j for i in range(1,n+1)] for j in range(1,m+1)]
# for i in a:
#     print(i)

# days = [d for d in range(1, 32)]
# weeks = [days[i:i+7] for i in range(0, len(days), 7)]
# print(weeks)
# print()

# work_weeks = [week[0:5] for week in weeks]
# print(work_weeks)
# print()

# wdays = [item for sublist in work_weeks for item in sublist]
# print(wdays)
