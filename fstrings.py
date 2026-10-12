"""
Los fstrings permite formatear cadenas de texto
de una manera más legible y también más eficiente
"""
edad = 20
name = "Juan"

print(f"Tu edad es de {edad}")

print(f"Hola {name} eres {"mayor" if edad >= 18 else "menor"} de edad")

# Modificadores de formato fstrings

balance_price = 12000000
text = f"Usted tiene un balance de {balance_price:,}"
print(text)

stock_price = 1.2939
text = f"Usted tiene un stock de {stock_price:.1f}"
print(text)

text = f"Usted tiene un stock de {stock_price:.3f}"
print(text)

# Alineadores

product = "Laptop"
price = 1000

text = f"Producto: {product:<15} | Precio: {price}"

text = f"{text}\nProducto: {product}\nPrecio: {price}"
print(text)

valor = 0.459323
text = f"{valor:.0%}"
print(text)


