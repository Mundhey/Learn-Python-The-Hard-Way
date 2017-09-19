def break_words(stuff):
    words=stuff.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(word):
    word=word.pop(0)
    print word

def print_last_word(word):
    word=word.pop(-1)
    print word

def sort_sentence(sentence):
    word=break_words(sentence)
    return sort_words(word)

def print_first_and_last(sentence):
    word=break_words(sentence)
    print_first_word(word)
    print_last_word(word)

def print_first_last_sorted(sentence):
    word=sort_sentence(sentence)
    print_first_word(word)
    print_last_word(word)

