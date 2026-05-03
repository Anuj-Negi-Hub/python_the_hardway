animals = ['bear', 'tiger', 'penguin', 'zebra']
bear = animals[0]

print(bear)


# Ordinal numbers: This is because the order of the animals is important. You can’t have the second animal without the
# first (1st) animal, and you can’t have the third without the second. It’s also impossible to have a “zeroth”
# animal, since zero means nothing. How can you have a nothing win a race? It just doesn’t make sense.
# We call these kinds of numbers “ordinal” numbers, because they indicate an ordering of things.

# Cardinal number: Programmers, however, can’t think this way, because they can pick any element out of a list at any point.
# To programmers, the list of animals is more like a deck of cards. If they want the tiger, they grab it. If they
# want the zebra, they can take it, too. This need to pull elements out of lists at random means that they
# need a way to indicate elements consistently by an address, or an “index,” and the best way to do that is
# to start the indices at 0. Trust me on this: the math is way easier for these kinds of accesses. This kind
# of number is a “cardinal” number and means you can pick at random, so there needs to be a 0 element.

# ordinal == ordered, 1st; cardinal == cards at random, 0.