sample_articles = [
    {
        "title": "python logra nuevo exito",
        "source": {"name": "TechNews"},
        "description": "Gran noticia",
        "category": "Tecnologia",
    },
    {
        "title": "Mercado en crisis",
        "source": {"name": "finance"},
        "description": "Analisis completo",
        "category": "Economia",
    },
    {
        "title": "Nueva tecnologia",
        "source": {"name": "TechNews"},
        "description": "Innovacion",
        "category": "Tecnologia",
    },
    {
        "title": "Deportes hoy",
        "source": {"name": "sports"},
        "description": "Resultados",
        "category": "Deportes",
    },
    {
        "title": "politica actual",
        "source": {"name": "News"},
        "description": "Actualidad",
        "category": "politica",
    },
    {
        "title": "ciencia avanzada",
        "source": {"name": "Science"},
        "description": "Descubrimientos",
        "category": "Ciencia",
    },
]


def extract_titles_traditional(articles): 
    titles = []
    for article in articles: 
        if len(article["title"]) > 10:
          titles.append(article["title"])
    return titles 


def extract_titles_comprehension(articles):
    return [article["title"] for article in articles if len(article["title"]) > 10]


def extract_article_summaries(articles):
    return {
        article["title"]: article["description"]
        for article in articles 
    }


def extract_article_categories_traditional(articles):
    categories = set()
    for article in articles: 
        categories.add(article["category"])
    return categories


def extract_article_categories(articles):
    return {
        article["category"] for article in articles
    }


print(extract_titles_traditional(sample_articles))
print("================================")
print(extract_titles_comprehension(sample_articles))
print("================================")
print(extract_article_summaries(sample_articles))
print("================================")
print(extract_article_categories_traditional(sample_articles))