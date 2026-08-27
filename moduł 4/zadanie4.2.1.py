def palindrom_check(x):
    """
        Checks if word is an palindrom
    """
    return x == x[::-1]

word = "kajak"

if palindrom_check(word) == True:
    print(f"{word} jest palindromem")
else:
    print(f"{word} nie jest palindromem")
