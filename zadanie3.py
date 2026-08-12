cashout = 5780

if cashout <= 0:
    print ("Kwota do wypłaty musi być większa niż 0")
elif cashout % 10 != 0:
    print ("Kwota do wypłaty musi być podzielna przez 10")
else:
    fiveH = cashout / 500
    fiveHR = cashout % 500
    twoH = fiveHR / 200
    twoHR = fiveHR % 200
    oneH = twoHR / 100
    oneHR = twoHR % 100
    five = oneHR / 50
    fiveR = oneHR % 50
    two = fiveR / 20
    twoR = fiveR % 20
    one = twoR / 10
    print ("Do wypłaty:")
    if int (fiveH) >= 1:
        print (f"banknotów 500 zł, {int(fiveH)} szt.")
    if int (twoH) >= 1:
        print (f"banknotów 200 zł, {int(twoH)} szt.")
    if int (oneH) >= 1:
        print (f"banknotów 100 zł, {int(oneH)} szt.")
    if int (five) >= 1:
        print (f"banknotów 50 zł,  {int(five)} szt.")
    if int (two) >= 1:
        print (f"banknotów 20 zł,  {int(two)} szt.")
    if int (one) >= 1:
        print (f"banknotów 10 zł,  {int(one)} szt.")

#dowiedziełam się że int() ucina wszystko po przecinku i postanowiłem to wykorzystać