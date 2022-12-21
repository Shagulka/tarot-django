# from django.contrib.auth import get_user_model
# from django.test import Client, TestCase
# from django.urls import reverse
#
# from fortune.models import Fortune
#
# from coins.models import BankAccount
#
#
# class FortuneViewTest(TestCase):
#     def setUp(self):
#         Fortune.objects.create(
#             name='Гадание 1', slug="fortune-1",
#             title_for_main_page="Обычное гадание",
#             fortune_description="бла бла",
#             title_for_fortune="Гадание",
#             type_fortune_telling=1,
#             default_card_description=1,
#             price=10)
#         Fortune.objects.create(
#             name='Гадание 2', slug="fortune-2",
#             title_for_main_page="Гадание на любовь",
#             fortune_description="бла бла",
#             title_for_fortune="Гадание",
#             type_fortune_telling=2,
#             default_card_description=2,
#             price=10)
#         Fortune.objects.create(
#             name='Гадание 3', slug="fortune-3",
#             title_for_main_page="Гадание на деньги",
#             fortune_description="бла бла",
#             title_for_fortune="Гадание",
#             type_fortune_telling=3,
#             default_card_description=3,
#             price=10)
#         User = get_user_model()
#         User.objects.create_user(email='temporary@gmail.com', password='temporary131')
#
#     def test_fortune_context(self):
#         self.client.login(email='temporary@gmail.com', password='temporary131')
#         response = Client().get(reverse('fortune:fortune_list'))
#         b = response.context
#         self.assertIn('fortunes', response.context)
#         self.assertEqual(len(response.context['fortunes']), 3)
#
#     def test_fortune_detail_context(self):
#         self.client.login(email='temporary@gmail.com', password='temporary131')
#         user = get_user_model().objects.get(email='temporary@gmail.com')
#         response = Client().get(reverse('fortune:fortune_detail',
#                                         kwargs={'pk': 1}))
#         a = response.context
#         self.assertEqual(response.context['email'], 'temporary@gmail.com')
#
#         self.assertIn('fortune', response.context)
#         self.assertIn('cards', response.context)
#         self.assertIn('prediction', response.context)
#         self.assertEqual(response.context['fortune'].name, 'Гадание 1')
#
#     def test_fortune_detail_context_404(self):
#         self.client.login(email='temporary@gmail.com', password='temporary131')
#         response = Client().get(reverse('fortune:fortune_detail',
#                                         kwargs={'pk': 100}))
#
#         self.assertEqual(response.status_code, 404)
