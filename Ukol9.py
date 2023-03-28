import pandas as pd

# načtení dat csv
df = pd.read_csv('temperature.csv')

# první řádky
print(df.head())

# měření v Praze
praha = df[df['City'] == 'Prague']
print(praha)

# statistika sloupcec AvgTemperature
print(df['AvgTemperature'].describe())

# měření s teplotou vyšší než 80 stupňů
hot = df[df['AvgTemperature'] > 80]
print(hot)

# měření s teplotou vyšší než 60 stupňů a v regionu Evropa
europe = df[(df['AvgTemperature'] > 60) & (df['Region'] == 'Europe')]
print(europe)

# extrémní hodnoty teploty
extremes = df[(df['AvgTemperature'] > 80) | (df['AvgTemperature'] < -20)]
print(extremes)
