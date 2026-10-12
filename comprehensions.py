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


#print(extract_titles_traditional(sample_articles))
#print("================================")
#print(extract_titles_comprehension(sample_articles))
#print("================================")
#print(extract_article_summaries(sample_articles))
#print("================================")
#print(extract_article_categories_traditional(sample_articles))

# Sets

def extract_sources_traditional(articles):
    sources = set()
    for article in articles:
        if article.get("source") and article.get("source").get("name"):
            sources.add(article.get("source").get("name"))
    return sources

def get_sources(articles):
    return {
        article.get("source").get("name") for article in articles
        if article.get("source") and article.get("source").get("name")
    }

print(get_sources(sample_articles))
print("=======")
print(extract_sources_traditional(sample_articles))

def categorize_articles(articles):
    sources = get_sources(articles)
    results = {}

    for source in sources:
        if source not in results:
            results[source] = []
        for article in articles:
            if source == article.get("source").get("name"):
                results[source].append(article)

    return results


def categorize(articles):
    sources = get_sources(articles)

    return {
        source: [
            article
            for article in articles
            if source == article.get("source").get("name")
        ]
        for source in sources
    }

print(categorize(sample_articles))
print(categorize_articles(sample_articles))