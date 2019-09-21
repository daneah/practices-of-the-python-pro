import re


def remove_spaces(query):  # <1>
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    return query


def normalize(query):  # <2>
    query = query.casefold()
    return query


def remove_quotes(query):  # <1>
    query = re.sub(r'"', '', query)
    return query


if __name__ == '__main__':
    search_query = input('Enter your search query: ')  # <3>
    search_query = remove_spaces(search_query)  # <4>
    search_query = remove_quotes(search_query)  # <2>
    search_query = normalize(search_query)
    print(f'Running a search for "{search_query}"')  # <5>
