import numpy as np
import matplotlib
import os
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(t, A, k, C):
    return A * np.exp(-k * t) + C

np.random.seed(0)
t = np.linspace(0, 10, 50)
A_real, k_real, C_real = 5, 0.8, 1
y_real = func(t, A_real, k_real, C_real)
ruido = np.random.normal(0, 0.5, t.shape)
y_noisy = y_real + ruido


popt, pcov = curve_fit(func, t, y_noisy, p0=(1, 1, 1))
A_est, k_est, C_est = popt


erro_A = abs(A_est - A_real)
erro_k = abs(k_est - k_real)
erro_C = abs(C_est - C_real)

pasta = 'ajuste de curva'
os.makedirs(pasta, exist_ok=True)

caminho = os.path.join(pasta, 'ajuste da curva.png')

plt.scatter(t, y_noisy, label='Dados experimentais', color='red')
plt.plot(t, func(t, *popt), label='Curva ajustada', color='blue')
plt.xlabel('Tempo (s)')
plt.ylabel('y(t)')
plt.legend()
plt.savefig(caminho) 

print(f"Erro absoluto médio para A: {erro_A}")
print(f"Erro absoluto médio para k: {erro_k}")
print(f"Erro absoluto médio para C: {erro_C}")
print("O gráfico foi salvo como 'ajuste_de_curva.png'.")