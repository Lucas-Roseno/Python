import pandas as pd
import matplotlib.pyplot as plt
import os

temperaturas = pd.DataFrame(
    {
        'segunda' : [45, 40, 55],
        'terca' : [47, 41, 54],
        'quarta' : [49, 42, 56],
        'quinta' : [50, 40, 57],
        'sexta' : [46, 43, 56],
        'sabado' : [48, 44, 55],
        'domingo' : [47, 42, 54]
    },
    index=['Servidor A', 'Servidor B', 'Servidor C']
)

print(temperaturas)
print('\nTemperaturas maiores que 50C:\n')
print(temperaturas[temperaturas > 50])


temperaturas.plot(kind='bar', figsize=(10, 6))
plt.title('Temperaturas por Dia da Semana')
plt.xlabel('Servidores')
plt.ylabel('Temperatura (°C)')
plt.legend(title='Dias da Semana')


output_dir = 'pandas'
os.makedirs(output_dir, exist_ok=True)  
output_path = os.path.join(output_dir, 'temperaturas.png')
plt.savefig(output_path)

plt.show()