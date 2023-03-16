# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:59:14 2023

@author: marie
"""

import pandas as pd

# Import dat
df = pd.read_csv('zver.csv',sep = ';')

# Seznameni s daty
print("ukol 1 output: \n")
col_names = df.columns
[rows,cols] = df.shape

print("Pocet radku tabulky: " + str(rows))
print("Pocet sloupcu tabulky: " + str(cols))
print("\nJmena jednotlivych sloupcu: \n")
for col_name in col_names:
    print(col_name)
    
# Hledani zvirete s indexem 34

print("\nukol 2 output: \n")
zvire_name_cz = df[34:35]['nazev_cz']
zvire_name_en = df[34:35]['nazev_en']

print("Jmeno zvirete s indexem 34 v Cz: " + zvire_name_cz)
print("Jmeno zvirete s indexem 34 v En: " + zvire_name_en)

# Bonus

print("\nBonusovy ukol 1 output: ")
sorted_by_price = df.sort_values(['cena'], ascending = False)

max_price = int(sorted_by_price[0:1]['cena'])

most_expensive_animals = sorted_by_price[sorted_by_price['cena'] == max_price]

print("\nZvirata jejichz adopce je nejdrazsi (" + str(max_price) + "): \n")
[rows2,cols]  = most_expensive_animals.shape

for i in range(rows2):
    print(most_expensive_animals[i:i+1]['nazev_cz'].str.lower())
    
sort_by_name_cz = df.sort_values(['nazev_cz'])
sort_by_name_en = df.sort_values('nazev_en')

last_name_cz = sort_by_name_cz[rows-1:rows]['nazev_cz']
last_name_en = sort_by_name_en[rows-1:rows]['nazev_en']

print("\n")
print("Posledni zvire podle abecedy v CZ: " + last_name_cz)
print("Posledni zvire podle abecedy v EN: " + last_name_en)