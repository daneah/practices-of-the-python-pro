def has_long_words(sentence):
    if isinstance(sentence, str):  # <1>
        sentence = sentence.split(' ')

    for word in sentence:  # <2>
        if len(word) > 10:  # <3>
            return True

    return False  # <4>
