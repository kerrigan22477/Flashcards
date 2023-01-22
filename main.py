from deck import Deck

deck = Deck()
deck.load("flashcard_deck.json")
studying = True

while studying:
    answer = input('Do you want to add cards or study?, S = study, A = add, F = finished\n')
    print(answer)

    if answer == 'A':
        deck = Deck()
        adding = True

        while adding:
            term = input('term to add\n')
            definition = input('definition\n')
            deck.add(term, definition)

            cont = input('do you want to add more terms? type A for add, any other button to stop\n')
            if cont != 'A':
                adding = False

    if answer == 'S':
        deck.study()

    if answer == 'F':
        studying = False

    deck.save("flashcard_deck.json")

