import os
import urllib.request
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWSAPI_KEY")
base_url = os.getenv("BASE_URL")

def newsapi_client(api_key, query, timeout=30, retries=3 ):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url= f"{base_url}?{query_string}"

    with urllib.request.urlopen(url, timeout=timeout) as response:
        data = response.read()
        print(data)
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

fetch_news("newsapi", api_key=api_key, query="Python")