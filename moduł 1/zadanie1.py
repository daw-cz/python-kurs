a = 1
b = 2
c = 3

a, b, c = c, a, b

print(f'''a = {a}
b = {b}
c = {c}''')


a = 1
b = 2
c = 3

a = c
b = a
c = b

print(f'''
a = {a}
b = {b}
c = {c}''')
# w pierwszym przypadku jak dobrze rozumiem przy przypisaniu wartości w jednej linii
# wszystkie zmiany dzieją się równocześnie dlatego dla każdej wartości przypisuje nową
# na podstawie wyżej zdefiniowanych

# w drugim przypadku przy wypisaniu tego w 3 liniach, za każdym razem pobiera nowo przypisaną wartość
# dlatego wszystkie wartości na końcu wynoszą 3
