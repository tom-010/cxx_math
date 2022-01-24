from unittest import TestCase

import os
os.path

class TestCreateApp(TestCase):

    def setUp(self):
        self.name = 'hello'
        self.module_name = self._random_name
        self.outer_dir = 'lib/' + self.module_name
        self.path = self.outer_dir + '/' + 'package'
    
    def tearDown(self):
        os.system(f'cd .. && rm {self.outer_dir} -r 2> /dev/null')

    def test_create_test(self):
        self.assertEqual(0, self.system(f'python3 manage/create_lib.py lib/{self.module_name}/package'))
        self.assertEqual(0, self.system(f'python3 manage/create_test.py lib/{self.module_name}/package hello'))
        self.assertFileExists(f'lib/{self.module_name}/package/hello_test.cc')
        self.assertEqual(0, self.system(f'bazel test //lib/{self.module_name}/package:package_test'))

    def assertFileExists(self, path):
        fixed_path = '../' + path
        self.assertTrue(os.path.isfile(fixed_path), path + ' not found')

    def system(self, command):
        command = 'cd .. && ' + command
        return os.system(command)

    @property
    def _random_name(self):
        import string 
        import random 
        return ''.join(random.choices(string.ascii_letters, k=random.randint(20, 25)))