import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/DanChitwood/PlantsAndPython/master/grape_harvest.csv')

min_an = data["harvest"].min()
print(data[data['harvest'] == min_an])

max_an = data["harvest"].max()
print(data[data['harvest'] == max_an])

prova1 = data[data['year'] <= 1849]
prova2 = data[(data['year'] >= 1850) & (data['year'] <= 1899)]
prova3 = data[(data['year'] >= 1900) & (data['year'] <= 1999)]

print(prova1['harvest'].median())
print(prova2['harvest'].median())
print(prova3['harvest'].median())

# Import matplotlib and seaborn
import matplotlib.pyplot as plt
import seaborn as sb
plt.figure(figsize=(15, 4))
sb.boxplot(data['region'], data['harvest'])
plt.show()

# Remember the line of code to set matplotlib figures to inline in Jupyter

# a list of regions, from the most southern to northern
latitude_order = ['spain', 'maritime_alps', 'languedoc', 'various_south_east',
                  'gaillac_south_west', 'southern_rhone_valley', 'bordeaux',
                  'northern_rhone_valley', 'auvergne', 'savoie', 'northern_italy',
                  'beaujolais_maconnais', 'vendee_poitou_charente', 'switzerland_leman_lake',
                  'jura', 'high_loire_valley', 'low_loire_valley', 'burgundy', 'auxerre_avalon',
                  'champagne_2', 'southern_lorraine', 'alsace', 'northern_lorraine',
                  'germany', 'ile_de_france', 'champagne_1', 'luxembourg']

plt.figure(figsize=(15, 4))
plt.title('Harvest times acrrosss time')

sb.boxplot(x=data['region'], y=data['harvest'], order=latitude_order)

# Put your code here
plt.xticks(rotation=45)
  # Rotates x axis labels so that they are readable
plt.show()
