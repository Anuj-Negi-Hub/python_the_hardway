# This exercise is a little different. You won't be running it. Instead you will prompt it into Python and run the functions yourself.

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Print the first word after popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Print the last word after popping it off"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Print first and last word of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words and then prints first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)



# import 25_even_more_practice
# sentence = "All good things come to those who wait."
# words = 25_even_more_practice.break_words(sentence)
# words
# sorted_words = 25_even_more_practice.sort_words(words)
# sorted_words
# 25_even_more_practice.print_first_word(words)
# 25_even_more_practice.print_last_word(words)
# words
# 25_even_more_practice.print_first_word(sorted_words)
# 25_even_more_practice.print_last_word(sorted_words)
# sorted_words
# sorted_words = 25_even_more_practice.sort_sentence(sentence)
# sorted_words
# 25_even_more_practice.print_first_and_last(sentence)
# 25_even_more_practice.print_first_and_last_sorted(sentence)


