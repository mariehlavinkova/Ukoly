import pandas as pd

# Načtení dat o zaměstnancích z CSV souborů
df_zam_praha = pd.read_csv('zam_praha.csv', delimiter = ',')

df_zam_plzen = pd.read_csv('zam_plzen.csv', delimiter = ',')

df_zam_liberec = pd.read_csv ('zam_liberec.csv', delimiter = ',')

# Přidání sloupce město
df_zam_praha ['mesto'] = 'Praha'

df_zam_plzen ['mesto'] = 'Plzen'

df_zam_liberec ['mesto'] = 'Liberec'

# Vytvoření nové tabulky zamestnanci
df_zamestnanci = pd.concat([df_zam_praha, df_zam_plzen, df_zam_liberec])

# Načtení platy
df_platy = pd.read_csv ('platy_2021_02.csv', index_col = False)

# Propojení tabulky
df_zamestnanci_platy = df_zamestnanci.join(df_platy.set_index(['cislo_zamestnance']), on=['cislo_zamestnance'])

# Průměrný plat zaměstnanců v jednotlivých kancelářích.
prum_plat = df_zamestnanci_platy.groupby('mesto')['plat'].mean()
print('Průměrný plat zaměstnanců v jednotlivých kancelářích:', prum_plat)

# Načíst vykazy.csv
df_vykazy = pd.read_csv('vykazy.csv', delimiter = ',')

# Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.
df_vykazy.groupby('project')

print(df_vykazy.groupby('project')['hours'].mean())

