import re


def remove_spaces(query):
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    return query


def normalize(query):
    query = query.casefold()
    return query


def remove_quotes(query):
    query = re.sub(r'"', '', query)
    return query


if __name__ == '__main__':
    search_query = input('Enter your search query: ')
    search_query = remove_spaces(search_query)  # <1>
    search_query = remove_quotes(search_query)  # <2>
    search_query = normalize(search_query)  # <3>
    print(f'Running a search for "{search_query}"')  # <4>
