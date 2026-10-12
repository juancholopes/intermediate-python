# Args en python

def ejemplo_args(*args):
    print(f"Argumentos recibidos {args}")
    print(f"{type(args)}")

ejemplo_args("Hola", "Mundo")

# Argumentos necesarios

def ejemplo_args_obligatorio(api_key, *numeros):
    print(f"Api Key: {api_key}")
    print(f"Resto de args: {numeros}")
    print(f"{type(api_key)}")
    print(f"{type(numeros)}")

ejemplo_args_obligatorio("API_KEY_OPENAI", 3, 23, 32)


