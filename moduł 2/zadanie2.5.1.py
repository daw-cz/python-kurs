numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers3 = [n ** 3 for n in numbers]
for i in numbers3:
    if i % 2 != 0:
        print(i)