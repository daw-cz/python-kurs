# sposób 1 przestawiajac elementy

my_l = [
    'włącz czajnik',
    'znajdź opakowanie herbaty',
    'zalej herbatę',
    'nalej wody do czajnika',
    'wyjmij kubek',
    'włóż herbatę do kubka'
]
my_l[0], my_l[1], my_l[2], my_l[3], my_l[4], my_l[5] = my_l[3], my_l[0], my_l[1], my_l[4], my_l[5], my_l[2]

print (my_l)


# sposób 2 tworząc nową listę

my_l2 = [
    'włącz czajnik',
    'znajdź opakowanie herbaty',
    'zalej herbatę',
    'nalej wody do czajnika',
    'wyjmij kubek',
    'włóż herbatę do kubka'
]

poprawna_kolejność = [
    my_l2[3],
    my_l2[0],
    my_l2[1],
    my_l2[4],
    my_l2[5],
    my_l2[2]
]

print (poprawna_kolejność)
