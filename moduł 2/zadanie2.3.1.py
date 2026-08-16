# Zadanie 2.1
# bez zaglądania do podpowiedzi uznałem, że moża wykorzystać len wspomnianie wcześniej

name_list = ["John", "Michael", "Terry", "Eric", "Graham"]
name_dictionary = {
    name_list[0]: len(name_list[0]),
    name_list[1]: len(name_list[1]),
    name_list[2]: len(name_list[2]),
    name_list[3]: len(name_list[3]),
    name_list[4]: len(name_list[4])
}

print(name_dictionary)

# Po przeczytaniu podpowiedzi aby wykorzystać pętle zauważyłem, że do powyższego rozwiązania 
# też można wykorzystać pętle

name_dictionary2 = {}

for name in name_list:
    name_dictionary2[name] = len(name)
print(name_dictionary2)

# Poniżej jeszcze bez użycia len

name_dictionary3 = {}

for name in name_list:
    n = 0
    for i in name:
        n = n + 1
    
    name_dictionary3[name] = n

print(name_dictionary3)