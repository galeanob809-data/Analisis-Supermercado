import pandas as pd
import matplotlib.pyplot as plt

# Leer CSV
df = pd.read_csv("data/ventas.csv")

# Ingresos totales
ingresos_totales = df["Total"].sum()
print(f"Ingresos totales: ${ingresos_totales:.2f}")

# Ingresos por categoría
ingresos_categoria = df.groupby("Categoria")["Total"].sum().sort_values(ascending=False)
print("\nIngresos por categoría:\n", ingresos_categoria)

# Productos más vendidos
top_productos = df.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False)
print("\nProductos más vendidos:\n", top_productos)

# Ventas mensuales
df['Fecha'] = pd.to_datetime(df['Fecha'])
ventas_mensuales = df.groupby(df['Fecha'].dt.to_period("M"))["Total"].sum()
print("\nVentas mensuales:\n", ventas_mensuales)

# Gráficos
top_productos.plot(kind='bar', title='Top Productos Vendidos')
plt.ylabel("Cantidad")
plt.tight_layout()
plt.savefig("data/top_productos.png")
plt.show()

ventas_mensuales.plot(kind='line', marker='o', title='Ventas Mensuales')
plt.ylabel("Ingresos")
plt.tight_layout()
plt.savefig("data/ventas_mensuales.png")
plt.show()
