import unittest
from app import get_all_doc_owners_names, get_doc_owner_name, add_new_doc, delete_doc


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print('===> setUp')

    def tearDown(self) -> None:
        print('===> tearDown')

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(get_all_doc_owners_names(), set)
        self.assertIsNotNone(get_all_doc_owners_names())

    def test_show_document_info(self):
        self.assertEqual(get_doc_owner_name('2207 876234'), 'Василий Гупкин')
        self.assertIsInstance(get_doc_owner_name('2207 876234'), str)

    def test_new_doc_shelf_number(self):
        self.assertEqual(add_new_doc('123456', 'passport', 'Иванов', 3), 3)
        self.assertIsNotNone(add_new_doc('123456', 'passport', 'Иванов', 3))

    def test_delete_doc(self):
        self.assertEqual(delete_doc('10006')[1], True)
