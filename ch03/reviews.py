# A single procedure for splitting a paragraph into sentences and tokens
import re

product_review = '''This is a fine milk, but the product
line appears to be limited in available colors. I
could only find white.'''  # <1>

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)  # <2>
matches = sentence_pattern.findall(product_review)  # <3>
sentences = [match[0] for match in matches]  # <4>

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")  # <5>
for sentence in sentences:
    matches = word_pattern.findall(sentence)
    words = [match[0] for match in matches]  # <6>
    print(words)


# Sentence parsing with the pattern matching factored into a function
import re


def get_matches_for_pattern(pattern, string):  # <1>
    matches = pattern.findall(string)
    return [match[0] for match in matches]


product_review = '...'

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)
sentences = get_matches_for_pattern(  # <2>
    sentence_pattern,
    product_review,
)

word_pattern = re.compile(r"([\w\-']+)([\s,.])?")
for sentence in sentences:
    words = get_matches_for_pattern(  # <3>
        word_pattern,
        sentence
    )
    print(words)
