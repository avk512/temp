# f = open("text.txt", "r")
# x = 0
# for line in f:
#     if x == 1:
#         print(line.split()[3])
#     x += 1
#
# f.close()

with open('text.txt', encoding='UTF-8') as f:
    i = 0
    # line = f.readline()
    for word in f:
        print(word.split())
        if i == 1:
            print(word.split()[3])
        i += 1
