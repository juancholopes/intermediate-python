
def newsapi_client(api_key, query, timeout=30, retries=3 ):
    return f"newsapi {query} con timeout {timeout}"

def guardian_client(api_key, query, section, from_date, timeout=30, retries=3):
    return f"Guardian {section} desde {from_date} con timeout de {timeout}"


def fetch_news(api_name, *args, **kwargs):
    """
    Función flexible para conectar con la API
    """
    base_config = {
        "timeout": 30,
        "retries": 2
    }

    config = {
        **base_config,
        **kwargs
    }

    api_clients = {
        "newsapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_clients[api_name]

    return client(*args, **config)