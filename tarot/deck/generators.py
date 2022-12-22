import datetime
import json
import os
import random

import openai


class Deck:
    def __init__(self):

        json_file = open('./deck/data/cards.json', 'r', encoding='utf-8')

        self.data = json.load(json_file)

    def get_gpt_prediction(self, fortune, cards, user=None) -> str:
        """Generate prediction using GPT-3

        Args:
            fortune (Fortune): Fortune object
            cards (list): List of cards
            user (User, optional): User object. Defaults to None.

        Returns:
            str: Prediction
        if OPENAI_API_KEY is not provided
        returns default prediction ('будущее неизвестно')
        """
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        theme = fortune.default_card_description
        if theme == 1:
            theme = 'обычное гадание'
        elif theme == 2:
            theme = 'гадание на любовь'
        elif theme == 3:
            theme = 'гадание на деньги'
        elif theme == 4:
            theme = 'гадание на карьеру'
        elif theme == 5:
            theme = 'гадание на день'

        name = fortune.title_for_main_page
        description = fortune.fortune_description

        generated_cards = []
        for card in cards:
            if card['upright']:
                generated_cards.append(card['name'])
            else:
                generated_cards.append(card['name'] + ' (перевернута)')

        card_text = 'Карты:\n' + '\n'.join(generated_cards)

        prompt = (f'Сгенерируй {theme} с '
                  f'названием {name} по картам таро.\n'
                  f'Описание гадания: {description}\n'
                  f'{card_text}\nГадание:\n')

        response = openai.Completion.create(
            engine='davinci',
            prompt=prompt,
            temperature=0.9,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=['\n', ' Гадание:']
        )
        if response.choices:
            return response.choices[0].text
        else:
            return 'будущее неизвестно'

    def get_cards(self, fortune, user=None) -> tuple:
        # removed -> tuple(list, str) as it is not supported in python 3.8
        """Get cards and prediction for fortune

        Args:
            fortune (Fortune): fortune object
            user (User, optional): user object. Defaults to None.

        Returns:
            list: list of cards
            str: prediction

        if OPENAI_API_KEY is set, then use GPT-3 to generate prediction
        otherwise the prediction is 'будущее неизвестно'
        """
        random_cards = self.data.copy()
        if user:
            today = datetime.datetime.now().date()
            try:
                random.seed(
                    str(user.first_name + user.last_name +
                        str(user.date_of_birth) + str(today)))
            except Exception:
                pass
        random.shuffle(random_cards)
        prediction = 'будущее неизвестно'
        if os.environ.get('OPENAI_API_KEY'):
            prediction = self.get_gpt_prediction(
                fortune, random_cards[:fortune.number_of_cards], user)
        return random_cards[:fortune.number_of_cards], prediction
