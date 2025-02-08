import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

#Enter dataset filepath here
csv_filepath = '.Crime_Data_from_2020_to_Present.csv'

csv_data = pd.read_csv(csv_filepath, index_col=0)

#Filtre pour ne prendre que les vols de vehicules
data = csv_data.loc[csv_data['Crm Cd'] == 510]

data['DATE OCC'] = pd.to_datetime(data['DATE OCC'])

data["jour_semaine"] = data["DATE OCC"].dt.day_name()

jour_counts = data['jour_semaine'].value_counts()

jours_moyenne = jour_counts / data["jour_semaine"].nunique()  # Division par le nombre total de jours uniques

jour_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
jours_moyenne = jours_moyenne.reindex(jour_order)

moyenne_globale = jours_moyenne.mean()

plt.figure(figsize=(10,5))
sns.lineplot(x=jours_moyenne.index, y=jours_moyenne.values, marker="o", label="Average vehicle thefts per day")

# Ajouter une ligne horizontale pour la moyenne
plt.axhline(y=moyenne_globale, color="red", linestyle="--", label=f"Overall Mean: {moyenne_globale:.1f}")

#Ajout des labels
plt.xlabel('Day of the Week')
plt.ylabel("Average number of vehicle thefts per day")
plt.title("Average vehicle thefts per day in LA by day of the week (2020-2025)")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()  # Afficher la légende

plt.show()

#print(data.loc[:, ['DATE OCC','AREA','jour_semaine']])