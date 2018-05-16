import cards, unittest

class CardTests(unittest.TestCase):
    def test_ascii(self):
        card = cards.Card("A", "B")
        self.assertEqual(card.side_a, "A")
        self.assertEqual(card.side_b, "B")

    def test_unicode(self):
        card = cards.Card("漢字", "ה")
        self.assertEqual(card.side_a, "漢字")
        self.assertEqual(card.side_b, "ה")


class DeckTests(unittest.TestCase):
    def test_add_card(self):
        deck = cards.Deck("Test Deck")
        comparison_card = cards.Card("A", "B")
        deck.add_card("A", "B")

        self.assertEqual(deck.cards[0].side_a, "A")  # Test if card was created with the correct data
        self.assertEqual(deck.cards[0].side_b, "B")

        self.assertEqual(deck.cards[0].side_a, comparison_card.side_a)  # Test if card contains same data as directly created card
        self.assertEqual(deck.cards[0].side_b, comparison_card.side_b)

    def test_draw(self):
        deck = cards.Deck("Test Deck", [cards.Card("A", "B"), cards.Card("C", "D"), cards.Card("E", "F")])

        self.assertRaises(IndexError, deck.draw_random, 4)
        self.assertEqual(set(deck.draw_random(3)), set(deck.cards))
        self.assertEqual(len(set(deck.draw_random(2))), 2)


if __name__ == "__main__":
    unittest.main()
