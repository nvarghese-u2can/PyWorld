my_list = [(1, 2), (3, 4), (5, 6)]

for (k1, v1) in my_list:
    print(k1)
    print(v1)

# using break
for (k1, v1) in my_list:
    if k1 == 3:
        break
    print(k1)
    print(v1)

# using continue
for (k1, v1) in my_list:
    if k1 == 3:
        continue
    print(k1)
    print(v1)

# using continue
for (k1, v1) in my_list:
    if k1 == 3:
        pass
    print(k1)
    print(v1)
