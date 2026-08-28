import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

x = input('''Podaj działanie, posługując się odpowiednią liczbą:
1 -  Dodawanie
2  - Odejmowanie
3  - Mnożenie
4  - Dzielenie
''')
if x not in ["1", "2", "3", "4"]:
    print("Proszę wybrać liczbę od 1 do 4")
    exit(1)

if x in ["2", "4"]:
    try:
        L1 = float(input("Podaj składnik 1. "))
        L2 = float(input("Podaj składnik 2. "))
    except ValueError:
        print("Składnik musi być liczbą")
        exit(1)

if x in ["1", "3"]:
    num =[]
    try:
        n = float(input("Podaj ilość składników do równania: "))
        if n < 2 or n % 1 != 0:
            print("Liczba musi być całkowita i większa niż 1")
            exit(1)
        n = int(n)
    except ValueError:
        print("Wartość musi być liczbą")
        exit(1)
    try:
        for i in range (1, n + 1):
            L = input(f"Podaj składnik {i}. ")
            L = float(L)
            num.append(L)             
    except ValueError:
        print("Składnik musi być liczbą")
        exit(1)

if x == "1":
    logging.info(f"Dodaję liczby z listy {num}")
    result = sum(num)
elif x == "2":
    logging.info(f"Odejmuję {L2} od {L1}")
    result = L1 - L2
elif x == "3":
    logging.info(f"Mnożę liczby z listy {num}")
    x = 1
    for i in num:
        x = x * i
    result = x
elif x == "4":
    logging.info(f"Dzielę {L1} przez {L2}")
    if L2 == 0:
        print("Nie można dzielić przez zero")
        exit(1)
    else:
        result = L1 / L2

print(f"Wynik to {result:.2f}")
