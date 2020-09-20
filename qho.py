import numpy as np
import matplotlib.pyplot as plt

hbar = 1
m = 1
a = 8
b = 2
step = 0.01
x = np.arange(-a/2, a/2, step)
n = len(x)

V = x**2

mdd = 1/(step**2) * (np.diag(np.ones(n-1), k=-1)
                     - 2 * np.diag(np.ones(n))
                     + np.diag(np.ones(n-1), k=1))

H = -(hbar**2)/(2.0 * m) * mdd + np.diag(V)
E, psi_t = np.linalg.eigh(H)
psi = np.transpose(psi_t)

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, V, color='k', label='V')
print('Energies of the bound states:')
for i in range(len(E)):
    if(E[i] < x[0]**2):
        print('E%s = %.2f' %(i, E[i]))
        ax.plot(x, E[i] + 8*psi[i])
ax.grid()
ax.set_xlabel('Position: x')
ax.set_ylabel('Energy: E')
ax.legend()
plt.show()
