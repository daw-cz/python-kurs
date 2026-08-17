my_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
my_list0 = my_list[1:4] + my_list[5:10] + my_list[-2:]
my_list1 = my_list[0:1] + my_list[4:5] + my_list[10:12]
print(my_list0)
print(my_list1)

# nie wiem czy dobrze rozumiem zadanie, bo z jednej strony każe mi korzystać ze slicingu,
# a z drugiej mówi aby wykorzystać listy składane i wtedy bym to zrobił w ogóle bez korzystania
# slicingu w ten sposób:
new_list0 = [x for x in my_list if x == 0]
new_list1 = [x for x in my_list if x != 0]
print(new_list0)
print(new_list1)