"""
Verificar contraseña.
"""

def verificar(contrasena):
    "Verificar que la contraseña cumpla los requisitos."
    error = False
    # Tiene una longitud de, al menos, diez caracteres
    if len(contrasena) < 10:
        error = True
    # Contiene, al menos, dos letras mayúsculas
    mayus = 0
    for letra in contrasena:
        # ¿Es letra?
        if letra.upper() != letra.lower():
            # ¿Es mayúscula?
            if letra == letra.upper():
                mayus += 1
    if mayus < 2:
        error = True
    # No comienza con un número
    if contrasena[0] in "0123456789":
        error = True
    return not error


# Entradas
contrasena = input("Contraseña: ")

# Salidas
if verificar(contrasena):
    print("La contraseña sí cumple con los requisitos")
else:
    print("La contraseña no cumple con los requisitos")
