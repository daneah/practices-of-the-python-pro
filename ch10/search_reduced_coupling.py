import re


def _remove_spaces(query):  # <1>
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    return query


def _normalize(query):
    query = query.casefold()
    return query


def _remove_quotes(query):
    query = re.sub(r'"', '', query)
    return query


def clean_query(query):  # <2>
    query = _remove_spaces(query)
    query = _remove_quotes(query)
    query = _normalize(query)
    return query


if __name__ == '__main__':
    search_query = input('Enter your search query: ')
    search_query = clean_query(search_query)  # <3>
    print(f'Running a search for "{search_query}"')
