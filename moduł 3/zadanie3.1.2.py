num = 100
przez5 = []
do3 = []
for i in range(num + 1):
  if i % 5 == 0:
    przez5.append(i)
    do3.append(i**3)
print(f'''Liczby podzielne przez 5:
{przez5}

Liczby podniesone do potęgi 3:
{do3}''')