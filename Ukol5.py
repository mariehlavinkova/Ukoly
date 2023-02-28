teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]
#Vytvoř seznam průměrných teplot pro každý den.
prumerne_teploty = []
for den in teploty:
    prumerne_teploty.append(sum(den)/len(den))
print("Průměrné teploty pro každý den:", prumerne_teploty)

#Vytvoř seznam ranních teplot.
ranni_teploty = []
for den in teploty:
    ranni_teploty.append(den[0])
print("Ranní teploty:", ranni_teploty)

#Vytvoř seznam nočních teplot.
nocni_teploty = []
for den in teploty:
    nocni_teploty.append(den[-1])
print("Noční teploty:", nocni_teploty)

#Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
poledni_nocni_teploty = []
for den in teploty:
    poledni_nocni_teploty.append([den[1], den[-1]])
print("Polední a noční teploty:", poledni_nocni_teploty)
