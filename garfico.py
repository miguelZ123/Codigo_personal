import matplotlib.pyplot as plt
import numpy as np

# Datos de ejemplo con las coordenadas específicas
x = [4, 2, 3, 3, 6, 8, 8]  # coordenada x
y = [2, 2, 0, 3, 4, 6, 2]  # coordenada y
labels = ['1,1', '3,1', '7,1', '16,1', '12,1', '13,1', '18,1']
colores = ['#FFC000', '#70AD47', '#70AD47', '#70AD47', '#FFC000', '#FF0000', '#FFC000']  # Changed color for 13,1 to red

# Crear malla para fondo degradado
x_grid, y_grid = np.meshgrid(np.linspace(-0.5, 9.5, 300), np.linspace(-0.5, 9.5, 300))
z = (x_grid + y_grid)

# Crear figura
fig, ax = plt.subplots(figsize=(10, 8))

# Fondo degradado (verde a rojo claro)
ax.imshow(z, extent=[-0.5, 9.5, -0.5, 9.5], origin='lower', cmap='RdYlGn_r', alpha=0.3)

# Dibujar los puntos
for i in range(len(x)):
    ax.scatter(x[i], y[i], s=300, color=colores[i], edgecolors='black', zorder=3)
    # Modified text position by adding y_offset
    y_offset = 0.3  # Adjust this value to change label height
    ax.text(x[i], y[i] + y_offset, labels[i], fontsize=10, ha='center', va='bottom', zorder=4)

# Ajustes del gráfico
ax.set_xlim(-0.5, 9.5)
ax.set_ylim(-0.5, 9.5)
ax.set_xlabel("Impacto Operativo")
ax.set_ylabel("Impacto Financiero")
ax.set_title("Impacto Operativo vs Financiero")
ax.grid(True)

plt.tight_layout()
plt.show()
