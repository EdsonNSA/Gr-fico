import numpy as np
import matplotlib.pyplot as plt

def fermi_dirac(E, E_F, T):
    k_B = 8.617e-5  # Constante de Boltzmann em eV/K
    return 1 / (np.exp((E - E_F) / (k_B * T)) + 1)

# Parâmetros
E_F = 1  # eV
E = np.linspace(0, 2, 1000)  # Intervalo de energia em eV

# Temperaturas
temperaturas = [5.5, 300]
cores = ['b', 'g', 'r']

# Criando o gráfico
plt.figure(figsize=(8, 5))
for T, cor in zip(temperaturas, cores):
    plt.plot(E, fermi_dirac(E, E_F, T), label=f'T = {T} K', color=cor)

plt.axvline(E_F, color='k', linestyle='--', label='$E_F$ = 1 eV')
plt.xlabel('Energia (eV)')
plt.ylabel('f(E)')
plt.title('Distribuição de Fermi-Dirac')
plt.legend()
plt.grid()
plt.show()

