import wikipedia

search_phrase = input("Search phrase: ")

while search_phrase != "":
    try:
        page = wikipedia.page(search_phrase)
        print(page.title)
        print(page.summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_phrase = input("Search phrase: ")
