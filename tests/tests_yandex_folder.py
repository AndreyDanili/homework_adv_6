import unittest
from yandex_folder import YaUploader


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print('===> setUp')

    def tearDown(self) -> None:
        YaUploader.remove_folder(YaUploader('test_folder'))

    def test_create_folder(self):
        self.assertEqual(YaUploader.create_folder(YaUploader('test_folder')), 201)

    @unittest.expectedFailure
    def test_no_create_folder(self):
        self.assertEqual(YaUploader.create_folder(YaUploader('test_folder')), 409)

    def test_check_folder(self):
        YaUploader.create_folder(YaUploader('test_folder'))
        self.assertEqual(YaUploader.check_folder(YaUploader('test_folder')), 200)

