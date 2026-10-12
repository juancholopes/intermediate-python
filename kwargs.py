"""
Los kwargs permiten al usuario tener
"""

def ejemplo_kwargs(**kwargs):
    print(f"Kwargs: {kwargs}")
    print(f"{type(kwargs)}")

ejemplo_kwargs(key="value", clave="valor", lista=[1, 2, 3])
