import pprint

lst = [[{'Classes': '10', 'Year': '2016', 'quantity': 100},
        {'Classes': '9', 'Year': '2016', 'quantity': 100},
        {'Classes': '6', 'Year': '2016', 'quantity': 300}],
       [{'Classes': '7', 'Year': '2019', 'quantity': 20},
        {'Classes': '11', 'Year': '2016', 'quantity': 50},
        {'Classes': '10', 'Year': '2016', 'quantity': 10}]]

newDict = {}
#
# for l in lst:
#     for d in l:
#         k = d['Classes']
#         del d['Classes']
#         if k in newDict:
#             newDict[k]['quantity'] += d['quantity']
#         else:
#             newDict[k] = d
#
# pprint.pprint(newDict)


# for l in lst:
#     # pprint.pprint(l)
#     for dicts in l:
#         cls = dicts['Classes']
#         quantity = dicts['quantity']
#         dicts.pop('Classes')
#
#         newDict[cls] = dicts


# pprint.pprint(newDict)
# for elem in l:
# pprint.pprint(elem)  # получаем отдельные словари для каждого ингредиента

# for recept in lst:
#     for elem in recept:
#         name = elem['ingredient_name']
#         quantity = elem['quantity']
#         elem.pop('ingredient_name')
#         elem['quantity'] = quantity * person
#         newDict[name] = elem
#
# pprint.pprint(newDict)

# pprint.pprint(newDict)
