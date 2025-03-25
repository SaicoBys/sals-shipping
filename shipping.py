# Solicita el peso del paquete y convierte a número flotante
peso_paquete = float(input("Por favor, ingresa el peso del paquete en libras: "))

# Calcula el costo de envío terrestre estándar
cargo_base_terrestre = 20.00
if peso_paquete <= 2:
    costo_terrestre = 1.5 * peso_paquete + cargo_base_terrestre
elif peso_paquete <= 6:
    costo_terrestre = 3.00 * peso_paquete + cargo_base_terrestre
elif peso_paquete <= 10:
    costo_terrestre = 4.00 * peso_paquete + cargo_base_terrestre
else:
    costo_terrestre = 4.75 * peso_paquete + cargo_base_terrestre

# Imprime el costo de envío terrestre
print(f"Costo de envío terrestre: ${costo_terrestre:.2f}")

# Coste de envio de Ground Shipping Premium
CARGO_PREMIUM_ENVIO_TERRESTRE = 125.00
# Imprime el costo de Ground Shipping Premium
print(f"Costo de envío terrestre premium: ${CARGO_PREMIUM_ENVIO_TERRESTRE:.2f}")

# Calcula el costo de envío por dron
if peso_paquete <= 2:
    costo_dron = peso_paquete * 4.50
elif peso_paquete <= 6:
    costo_dron = peso_paquete * 9.00
elif peso_paquete <= 10:
    costo_dron = peso_paquete * 12
else:
    costo_dron = peso_paquete * 14.25

# Imprime el costo de envío por dron
print(f"Costo de envío por dron: ${costo_dron:.2f}")

# Determina y comunica el método de envío más económico
costo_minimo = min(costo_terrestre, costo_dron, CARGO_PREMIUM_ENVIO_TERRESTRE)
if costo_minimo == costo_dron:
    metodo_envio = "dron"
elif costo_minimo == costo_terrestre:
    metodo_envio = "terrestre"
else:
    metodo_envio = "premium"
print(f"La opción más económica es el envío {metodo_envio} y cuesta: ${costo_minimo:.2f}")