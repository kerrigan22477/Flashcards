from deck import Deck

deck = Deck()
deck.load("flashcard_deck.json")
studying = True

while studying:
    answer = input('Do you want to add cards or study?, s = study, a = add, f = finished\n')

    if answer == 'a':
        adding = True

        while adding:
            term = input('term to add\n')
            definition = input('definition\n')
            deck.add(term, definition)

            cont = input('do you want to add more terms? type A for add, any other button to stop\n')
            if cont != 'a':
                adding = False

    if answer == 's':
        deck.study()
        cont = input('do you want to remove any cards? r = remove, any other button otherwise\n')
        if cont == 'r':
            term = input('type the term you want to remove\n')
            deck.remove(term)

    if answer == 'f':
        studying = False

    deck.save("flashcard_deck.json")

