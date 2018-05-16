import cards

def load_decks(directory):
    pass

def run_quiz(card_list, flipped = False):
    score = 0

    for i in card_list:
        if flipped:
            print(i.side_b)
            expected_answer = i.side_a
        else:
            print(i.side_a)
            expected_answer = i.side_b

        actual_answer = input('Answer >> ')

        if actual_answer.upper() == expected_answer.upper():
            print("Correct.")
            score += 1
        else:
            print("Incorrect. The correct answer was " + expected_answer)

    print(str(score) + '/' + str(len(card_list)) + " correct!")


if __name__ == "__main__":
    decks = []
    loaded_cards = [cards.Card("A", "B"), cards.Card("漢字", "ה"), cards.Card("C", "D"), cards.Card("E", "F")]
    run_quiz(loaded_cards, flipped=True)