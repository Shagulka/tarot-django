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
        theme = fortune.type
        themes = {
            1: 'обычное гадание',
            2: 'гадание на любовь',
            3: 'гадание на деньги',
            4: 'гадание на карьеру',
            5: 'гадание на день',
            6: 'гадание на да/нет'
        }
        theme_text = themes.get(theme)
        card_description = {
            1: 'regular',
            2: 'love',
            3: 'finance',
            4: 'career',
            5: 'regular',
            6: 'yesno'
        }

        for card in cards:
            card['description'] = card[card_description[theme]]

        name = fortune.title_for_AI if fortune.title_for_AI else fortune.title
        description = fortune.description

        generated_cards = []
        for card in cards:
            if card['upright']:
                generated_cards.append(
                    f'{card["name"]} - {card["description"]};')
            else:
                generated_cards.append(
                    f'{card["name"]} (перевернута) - {card["description"]}')

        card_text = 'Вытянутые карты:\n' + '\n'.join(generated_cards)

        prompt = (f'Сгенерируй {theme_text} '
                  f'пользователю {user.first_name} c'
                  f'названием {name} по картам таро.\n'
                  f'Описание гадания: {description}\n'
                  f'{card_text}\nРезультат гадания:\n')

        print(prompt)

        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=prompt,
            temperature=0.9,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=['Результат гадания:']
        )
        if response.choices:
            if response.choices[0].text:
                return response.choices[0].text
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
            now = datetime.datetime.now()
            try:
                random.seed(
                    str(user.first_name + user.last_name +
                        str(user.date_of_birth) + str(now)))
            except Exception:
                pass
        random.shuffle(random_cards)
        prediction = 'будущее неизвестно'
        if os.environ.get('OPENAI_API_KEY'):
            prediction = self.get_gpt_prediction(
                fortune, random_cards[:fortune.number_of_cards], user)
        return random_cards[:fortune.number_of_cards], prediction
