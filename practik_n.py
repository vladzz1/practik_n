# завдання 1

c1 = (12, 34, 14, 32, 45, 26, 55)
c2 = (10, 31, 12, 17, 45, 19, 16)
c3 = (19, 12, 16, 32, 45, 22, 26)

res = []
temp = []

for item1 in c1:
    for item2 in c2:
        if (item1 == item2):
            temp.append(item1)
            break
for item1 in temp:
    for item2 in c3:
        if (item1 == item2):
            res.append(item1)
            break

print(res)
res = []
temp = []

# завдання 2

for item1 in c1:
    is_duplicate = False
    for item2 in c2:
        if (item1 == item2):
            is_duplicate = True
            break
    if (not is_duplicate):
        temp.append(item1)
for item1 in temp:
    is_duplicate = False
    for item2 in c3:
        if (item1 == item2):
            is_duplicate = True
            break
    if (not is_duplicate):
        res.append(item1)

print(res)
res = []
temp = []

# завдання 3

i = 0
while (i < len(c1)):
    if (c1[i] == c2[i] and c2[i] == c3[i]):
        is_duplicate = False
        for item in res:
            if (item == c1[i]):
                is_duplicate = True
                break
        if (not is_duplicate):
            res.append(c1[i])
    i += 1

print(res)
res = []