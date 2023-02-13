
from unittest import TestCase

from main import geo_ru, ids_un, queries_says
from ya_disc import upload_path, last_uploaded, delete_folder


class TestGeoRu(TestCase):
    def test_ru(self):
        res = geo_ru([{'visit1': ['Москва', 'Россия']}])
        self.assertEqual(res, [{'visit1': ['Москва', 'Россия']}])

    def test_no_ru(self):
        res = geo_ru([{'visit2': ['Дели', 'Индия']}])
        self.assertEqual(res, [])

    def test_full(self):
        res = geo_ru([{'visit11': ['Лиссабон', 'Португалия']}, {'visit12': ['Тула', 'Россия']}])
        self.assertEqual(res, [{'visit12': ['Тула', 'Россия']}])
        self.assertNotEqual(res, [{'visit11': ['Лиссабон', 'Португалия']}])

    def test_list(self):
        res = geo_ru([{'visit2': ['Дели', 'Индия']}])
        self.assertIsInstance(res, list)
        self.assertNotIsInstance(res, dict)


class TestIdsUn(TestCase):
    def test_del_duplicates(self):
        res = ids_un({'user': [213, 213, 213, 213, 213]})
        self.assertEqual(res, [213])

    def test_not_duplicates(self):
        res = ids_un({'user': [54, 186, 119, 129, 987]})
        for id in [54, 186, 119, 129, 987]:
            self.assertIn(id, res)

    def test_list(self):
        res = ids_un({'user': [54, 186, 119, 129, 987]})
        self.assertIsInstance(res, list)
        self.assertNotIsInstance(res, dict)


class TestQueriesSays(TestCase):
    def test_queries_says(self):
        res = queries_says(['курс доллара', 'сериалы', 'курс по питону'])
        self.assertIn('33', res)
        self.assertIn('1', res)
        self.assertIn('2', res)
        self.assertIn('3', res)

    def test_queries_one(self):
        res = queries_says(['сериалы'])
        self.assertIn('100', res)
        self.assertIn('1', res)
        self.assertNotIn('2', res)
        self.assertNotIn('3', res)

class TestYaDiscPath(TestCase):

    def test_status_code(self):
        res = upload_path('test')
        self.assertEqual(res.status_code, 201)
        # if res.status_code == 201:
        #     print('Папка создана')
        res = last_uploaded('test')
        self.assertEqual(res.status_code, 200)
        # if res.status_code == 200:
        #     print('Папка существует')
        res = delete_folder('test')
        self.assertEqual(res.status_code, 204)
        # if res.status_code == 204:
        #     print('Папка удалена, все работает')