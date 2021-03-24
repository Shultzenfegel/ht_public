from django.test import TestCase

from .templatetags.htapp_extras import pluralize_number, format_decimal


class PluralizeNumberTestCase(TestCase):
    '''Тестирует шаблонный тег pluralize_number'''

    def setUp(self):
        self.words = 'отзыв,отзыва,отзывов'

    def test_pluralize_number_0(self):
        self.assertEqual(pluralize_number(0, self.words), '0 отзывов')

    def test_pluralize_number_1(self):
        self.assertEqual(pluralize_number(1, self.words), '1 отзыв')

    def test_pluralize_number_2(self):
        self.assertEqual(pluralize_number(2, self.words), '2 отзыва')

    def test_pluralize_number_5(self):
        self.assertEqual(pluralize_number(5, self.words), '5 отзывов')

    def test_pluralize_number_10(self):
        self.assertEqual(pluralize_number(10, self.words), '10 отзывов')

    def test_pluralize_number_11(self):
        self.assertEqual(pluralize_number(11, self.words), '11 отзывов')

    def test_pluralize_number_12(self):
        self.assertEqual(pluralize_number(12, self.words), '12 отзывов')

    def test_pluralize_number_21(self):
        self.assertEqual(pluralize_number(21, self.words), '21 отзыв')

    def test_pluralize_number_22(self):
        self.assertEqual(pluralize_number(22, self.words), '22 отзыва')


class FormatDecimalTestCase(TestCase):
    '''Тестирует шаблонный тег format_decimal'''

    def test_format_decimal_0(self):
        self.assertEqual(format_decimal(0, 0), '0')

    def test_format_decimal_3_5(self):
        self.assertEqual(format_decimal(3.534, 1), '3.5')

    def test_format_decimal_20_71(self):
        self.assertEqual(format_decimal(20.712, 2), '20.71')

    def test_format_decimal_1234(self):
        self.assertEqual(format_decimal(1234.5, 0), '1 234')
