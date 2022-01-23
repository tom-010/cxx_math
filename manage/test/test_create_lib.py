from unittest import TestCase
import os

class TestCreateLib(TestCase):

    def setUp(self):
        self.name = self._random_name
    
    def tearDown(self):
        os.system(f'cd .. && rm lib/{self.name} -r')

    def test_creates_a_buildable_library(self):
        os.system(f'cd .. && python3 manage/create_lib.py lib/{self.name}/package1/package')
        res = os.system(f'cd .. && bazel build //lib/{self.name}/package1/package:package')
        self.assertEqual(0, res)

    @property
    def _random_name(self):
        import string 
        import random 
        return ''.join(random.choices(string.ascii_letters, k=random.randint(20, 25)))