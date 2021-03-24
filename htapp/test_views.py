from django.http import response
from django.test import TestCase


class IndexViewTestCase(TestCase):
    '''Тестирует представление главной страницы'''

    fixtures = ['user.json', 'init.json']

    def setUp(self):
        self.url = '/'

    def test_ok_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_contain_header(self):
        response = self.client.get(self.url)
        self.assertContains(response, '<nav class="b-body__wrapper b-nav">')

    def test_contain_footer(self):
        response = self.client.get(self.url)
        self.assertContains(
            response, '<footer class="b-body__wrapper b-footer">')

    def test_context_has_hobbies(self):
        response = self.client.get(self.url)
        self.assertGreater(len(response.context['hobbies']), 0)

    def test_context_has_countries(self):
        response = self.client.get(self.url)
        self.assertGreater(len(response.context['countries']), 0)

    def test_context_has_two_slides(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['slides']), 2)

    def test_context_has_four_hotels(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['hotels']), 4)


class SearchViewTestCase(TestCase):
    '''Тестирует представление страницы поиска'''

    fixtures = ['user.json', 'init.json']

    def setUp(self):
        self.url = '/yoga/search/1'

    def test_ok_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context_has_six_specials(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['specials']), 6)

    def test_context_has_six_facilities(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['facilities']), 6)

    def test_context_has_six_hotel_types(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['hotel_types']), 6)

    def test_context_has_six_hotel_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['hotel_categories']), 6)

    def test_context_min_price(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['hotels_aggr']['min_price'], 1_350)

    def test_context_max_price(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['hotels_aggr']['max_price'], 11_150)

    def test_context_hotels_count(self):
        response = self.client.get(self.url)
        self.assertEqual(response.context['hotels_aggr']['count'], 4)


class SearchResultsViewTestCase(TestCase):
    '''Тестирует представление результатов поиска'''

    fixtures = ['user.json', 'init.json']

    def setUp(self):
        self.url = '/yoga/search-results?country=1'

    def test_ok_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_can_filter_by_specials(self):
        response = self.client.get(
            '/yoga/search-results?country=1&specials[]=1&pricefrom=1350.00&priceto=11150.00')
        self.assertEqual(len(response.context['hotels']), 2)

    def test_can_filter_by_facilities(self):
        response = self.client.get(
            '/yoga/search-results?country=1&facilities[]=4&pricefrom=1350.00&priceto=11150.00')
        self.assertEqual(len(response.context['hotels']), 3)

    def test_can_filter_by_hotel_types(self):
        response = self.client.get(
            '/yoga/search-results?country=1&hotel_types[]=3&pricefrom=1350.00&priceto=11150.00')
        self.assertEqual(len(response.context['hotels']), 1)

    def test_can_filter_by_hotel_types(self):
        response = self.client.get(
            '/yoga/search-results?country=1&hotel_types[]=3&pricefrom=1350.00&priceto=11150.00')
        self.assertEqual(len(response.context['hotels']), 1)

    def test_can_filter_by_hotel_categories(self):
        response = self.client.get(
            '/yoga/search-results?country=1&hotel_categories[]=5&pricefrom=1350.00&priceto=11150.00')
        self.assertEqual(len(response.context['hotels']), 2)

    def test_can_filter_by_price(self):
        response = self.client.get(
            '/yoga/search-results?country=1&pricefrom=1550.00&priceto=10550.00')
        self.assertEqual(len(response.context['hotels']), 2)


class HotelViewTestCase(TestCase):
    '''Тестирует представление страницы отеля'''

    fixtures = ['user.json', 'init.json']

    def setUp(self):
        self.url = '/yoga/hotel/1'

    def test_ok_status(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_context_has_nine_photos(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['photos']), 9)

    def test_context_has_three_reviews(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['reviews']), 3)

    def test_context_has_three_specials(self):
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['specials']), 3)
