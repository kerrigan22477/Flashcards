from deck import Deck

deck = Deck()
set_name = input('Type the name of the json deck file you would like to use\n')
deck.load(set_name)
studying = True

while studying:
    answer = input('Do you want to add cards or study?, s = study, a = add, f = finished d = display deck\n')

    if answer == 'd':
        deck.display_deck()

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
        type = input('do you want to study all the cards or the ones you are due to review? a = all')
        if type == 'a':
            deck.study_all()
        else:
            deck.study()
        cont = input('do you want to remove any cards? r = remove, any other button otherwise\n')
        if cont == 'r':
            term = input('type the term you want to remove\n')
            deck.remove(term)

    if answer == 'f':
        studying = False

    deck.save(set_name)

