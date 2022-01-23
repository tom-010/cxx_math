from unittest import TestCase
import os

class TestCreateApp(TestCase):

    def setUp(self):
        self.name = 'hello'
        self.outer_dir = self._random_name
        self.path = self.outer_dir + '/' + 'blub'
    
    def tearDown(self):
        os.system(f'cd .. && rm {self.outer_dir} -r 2> /dev/null')

    def test_create_app(self):
        create_command = f'cd .. && python3 manage/create_app.py {self.path} {self.name}'
        self.assertEqual(0, os.system(create_command))
        self.assertNotEqual(0, os.system(create_command))

        run_command = f'cd .. && bazel run //{self.path}:hello'
        self.assertEqual(0, os.system(run_command))


    @property
    def _random_name(self):
        import string 
        import random 
        return ''.join(random.choices(string.ascii_letters, k=random.randint(20, 25)))