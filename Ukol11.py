import pandas as pd
import matplotlib.pyplot as plt

# Načtení dat z CSV souboru
data = pd.read_csv("platy_2021_02.csv")

# Nastavení hranic skupin histogramu
bins = [30000, 35000, 40000, 45000, 50000, 55000, 60000]

# Vytvoření histogramu
plt.hist(data["plat"], bins=bins, edgecolor="black")

# Nastavení popisků os
plt.xlabel("Plat")
plt.ylabel("Počet zaměstnanců")
plt.title("Histogram platů zaměstnanců")

# Zobrazení grafu
plt.show()
