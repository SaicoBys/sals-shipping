# Prompt the user to enter the package weight and convert to float
peso_paquete = float(input("Por favor, ingresa el peso del paquete en libras: "))

# Calculate the cost of standard ground shipping
cargo_base_terrestre = 20.00
if peso_paquete <= 2:
    costo_terrestre = 1.5 * peso_paquete + cargo_base_terrestre
elif peso_paquete <= 6:
    costo_terrestre = 3.00 * peso_paquete + cargo_base_terrestre
elif peso_paquete <= 10:
    costo_terrestre = 4.00 * peso_paquete + cargo_base_terrestre
else:
    costo_terrestre = 4.75 * peso_paquete + cargo_base_terrestre

# Print the ground shipping cost
print(f"Costo de envío terrestre: ${costo_terrestre:.2f}")

# Cost of Premium Ground Shipping
CARGO_PREMIUM_ENVIO_TERRESTRE = 125.00
# Print the cost of Premium Ground Shipping
print(f"Costo de envío terrestre premium: ${CARGO_PREMIUM_ENVIO_TERRESTRE:.2f}")

# Calculate the cost of drone shipping
if peso_paquete <= 2:
    costo_dron = peso_paquete * 4.50
elif peso_paquete <= 6:
    costo_dron = peso_paquete * 9.00
elif peso_paquete <= 10:
    costo_dron = peso_paquete * 12
else:
    costo_dron = peso_paquete * 14.25

# Print the drone shipping cost
print(f"Costo de envío por dron: ${costo_dron:.2f}")

# Determine and display the most cost-effective shipping method
costo_minimo = min(costo_terrestre, costo_dron, CARGO_PREMIUM_ENVIO_TERRESTRE)
if costo_minimo == costo_dron:
    metodo_envio = "dron"
elif costo_minimo == costo_terrestre:
    metodo_envio = "terrestre"
else:
    metodo_envio = "premium"
print(f"La opción más económica es el envío {metodo_envio} y cuesta: ${costo_minimo:.2f}")