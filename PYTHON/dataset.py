import os
import pandas as pd
import random
from datetime import datetime, timedelta

# 1️⃣ Crear la carpeta 'data' si no existe
os.makedirs("data", exist_ok=True)
# Generar dataset de ejemplo
n = 200
productos = [
    ("Leche", "Lácteos", 120),
    ("Pan", "Panadería", 50),
    ("Queso", "Lácteos", 300),
    ("Manzanas", "Frutas y Verduras", 80),
    ("Pollo", "Carnicería", 500),
    ("Yogur", "Lácteos", 60)
]

ventas = []
fecha_inicio = datetime(2024,1,1)

for i in range(1, n+1):
    producto, categoria, precio_unitario = random.choice(productos)
    cantidad = random.randint(1,5)
    total = cantidad * precio_unitario
    fecha = fecha_inicio + timedelta(days=random.randint(0,30))
    cliente = f"Cliente_{random.randint(1,50)}"
    ventas.append([i, fecha.strftime("%Y-%m-%d"), producto, categoria, cantidad, precio_unitario, total, cliente])

df = pd.DataFrame(ventas, columns=[
    "ID_Venta","Fecha","Producto","Categoria","Cantidad","Precio_Unitario","Total","Cliente"
])

# Guardar CSV limpio
df.to_csv("data/ventas.csv", index=False, float_format="%.2f", encoding="utf-8")
print("✅ Dataset generado correctamente en data/ventas.csv")
