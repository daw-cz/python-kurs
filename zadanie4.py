print ("    ", end="")
for i in range(1, 11):
    print (f"{i:>4}", end="")
print ()
print ("-" * 44)

for i in range(1, 11):
    print (f"{i:>2} |", end="")
    for j in range (1, 11):
        print (f"{i * j:>4}", end="")
    print ()
# poznałem funkcje ":>4" a tak to robiłem to na zasadzie prób i błedów
# dalej nie mam pewności czy o to chodziło