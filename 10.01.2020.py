# countries_population = {}
# countries_population = {
#     'France': 66821000,
#     'Russia': 146691020,
#     'Japan': 126693000
# }
# countries_population['Egypt'] = 91891500
# people_in_russia = countries_population['Russia']
# # print(people_in_russia)
# for population in countries_population.values():
#     print(population)
# for country in countries_population:
#     print(country)
# friends = set()
# classmates = set(['Vasya', 'Petya', 'Kolya'])
# print(classmates)
# # print(type(classmates))
# friends.add('Petro')
# friends.add('Nino')
# friends.add('Petya')
# print(friends)
# print('Kesha' in classmates)
# friends_or_classmates = friends | classmates
# print(friends_or_classmates)
# friends_and_classmates = friends & classmates
# print(friends_and_classmates)
# for elem in classmates:
#     print(elem)
# friends_list = list(friends)
# print(friends_list)

# friends = []
# classmates = ["Vasya", "Petya", "Fedor"]
# friends.append("Vasya")
# friends.append("Kolya")
# # print(friends)
# first_friend = friends[0]
# # print(first_friend)
# # print('Keysha' in classmates)
# friends_then_classmates = friends + classmates
# # print(friends_then_classmates)
# # print(friends)
# # del friends[0]
# # print(friends)
# for mate in classmates:
#     print(mate)

# point = (1, 6)
# print(type(point))
# x, y = point
# # print(x, y)
# # print(type(x))
# # print(type(y))
# for coordinate in point:
#     print(coordinate)
# point = tuple([1, 6])
# print(point)
# coordinate = list(point)
# print(coordinate)
# pp = (1, 2) + (3, 4)
# print(pp)

# for i in range(10):
#     square = i * i
#     print(square)

# x = 21.5
# while x > 0.5:
#     print(x)
#     # x = x - 3.3
#     x -= 3.3

# for i, name in enumerate(['vasya', 'Kolya', 'Petya']):
#     print(i, name)

emp = ['Vasya', 'Petya', 'Kolya']
sol = [2000, 15000, 300]
for x, y in zip(emp, sol):
    print(x, ':', y)
