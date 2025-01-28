import pandas as pd
import matplotlib.pyplot as plt
import os

norte = pd.Series([2500, 2700, 3000, 2800], name='norte')
sul = pd.Series([2300, 2200, 2400, 2600], name='sul')
leste = pd.Series([3100, 3200, 3300, 3400], name='leste')

data_centers = pd.concat([norte, sul, leste], axis=1)

print(data_centers)

print("\nPrimeiro valor do sul:", sul.iloc[0])
print("Quarto valor do sul:", sul.iloc[3])

# Filtrar os consumos maiores que 2500 e menores que 3500
filtered_data = data_centers[(data_centers > 2500) & (data_centers < 3500)]


# Plotar os dados filtrados
filtered_data.plot(kind='bar', figsize=(10, 6))
plt.title('Consumos entre 2500 e 3500')
plt.xlabel('Índice')
plt.ylabel('Consumo')
plt.legend(title='Data Centers')

output_dir = 'pandas'
os.makedirs(output_dir, exist_ok=True)  
output_path = os.path.join(output_dir, 'consumo dataCenters.png')
plt.savefig(output_path)

plt.show()

