num = 30
fibonacci = []

a, b = 1, 1

for i in range(num):
    fibonacci.append(a)
    a, b = b, a + b

print(fibonacci)