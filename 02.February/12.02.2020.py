# points = {}
# for line in open('points.txt'):
#     line = line.split('\n')  # из строки получаем список
#     line = line[0]  # избавляемся от последнего элемента (\n)
#     line = line.split(' ')  # разделяем данные
#     line[1] = int(line[1])  # преобразуем координаты
#     line[2] = int(line[2])
#     points[line[0]] = line[1:]  # добавляем в словарь
#     # первый элемент списак - как ключ
#     # остальные - значение
# print(points)
#
# graphs = {}
# for line in open('graphs.txt'):
#     line = line.split('\n')
#     line = line[0]
#     line = line.split(' ')
#     graphs[line[0]] = line[1:]  # первый элемент - название пути
#     # остальные - точки, через которые он проходит
# print(graphs)

# with open('owner.txt') as fh:
#     d = {k.strip(): 0 for k in fh}
#
# print(d)
#
# data = []
# current = {}
# with open('Arts.txt') as f:
#     for line in f:
#         pair = line.split(': ', 1)
#         if len(pair) == 2:
#             if pair[0] == 'product/productId' and current:
#                 # start of a new block
#                 data.append(current)
#                 current = {}
#             current[pair[0]] = pair[1]
#     if current:
#         data.append(current)
#
# print(data)

# keys={}
# birds={}
# with open('birds.txt') as f:
#     for line in f:
#         k,_,v=line.partition(':')
#         k=k.capitalize()
#         v=map(float, v.split())
#         keys[k]=keys.setdefault(k, 0)+1
#         birds.setdefault('{} {}'.format(k, keys[k]), []).extend(v)
#
# print(birds)
