# zadanie 2.2

n_list = [1, 2, 3, 5, 6, 11, 12, 18, 19, 21,]
print(f"pierwotna lista: {n_list}")

new_list = []

for i in n_list:
    if i <= 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        new_list.append(i)

print (f"nowa lista: {new_list}")