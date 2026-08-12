n = 7
a, b = 0, 1
for i in range(n + 1):
    print (a, end=" ")
    if i == n - 1:
        p, o = a, b
    a, b = b, a + b
print ()

silnia = 1
for i in range (1, n + 1):
    silnia = silnia * i
print (f"{n}! = {silnia}")
print (f"{o} : {p} = {o / p}")