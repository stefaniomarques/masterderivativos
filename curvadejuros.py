import numpy as np
import matplotlib.pyplot as plt

# Crie dados simulados para a curva de juros
maturidades = np.array([1, 2, 3, 5, 7, 10, 20, 30])  # Maturidades em anos
taxas = np.array([0.02, 0.025, 0.03, 0.035, 0.037, 0.04, 0.045, 0.05])  # Taxas correspondentes

# Crie um gráfico de dispersão da curva de juros
plt.figure(figsize=(10, 6))
plt.plot(maturidades, taxas, marker='o', linestyle='-', color='b', markersize=8)
plt.title('Curva de Taxa de Juros')
plt.xlabel('Maturidade (Anos)')
plt.ylabel('Taxa de Juros')
plt.grid(True)

# Mostrar o gráfico
plt.show()