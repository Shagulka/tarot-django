import json
import random


class Deck:
    def __init__(self):

        # print(listdir('.'))
        json_file = open('./deck/data/cards.json', encoding='utf-8')

        self.data = json.load(json_file)

    def get_cards(self, fortune, user=None):
        random_cards = self.data.copy()
        if user:
            random.seed(
                str(user.name + user.surname + str(user.date_of_birth)))
        random.shuffle(random_cards)
        return random_cards[:fortune.number_of_cards]
