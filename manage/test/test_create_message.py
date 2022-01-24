from unittest import TestCase

import os
os.path

class TestCreateMessage(TestCase):

    def setUp(self):
        self.name = 'hello'
        self.module_name = self._random_name
        self.outer_dir = 'lib/' + self.module_name
        self.path = self.outer_dir + '/' + 'package'
    
    def tearDown(self):
        os.system(f'cd .. && rm {self.outer_dir} -r 2> /dev/null')

    def test_create_message(self):
        self.assertEqual(0, self.system(f'python3 manage/create_lib.py lib/{self.module_name}/package'))
        self.assertEqual(0, self.system(f'python3 manage/create_message.py lib/{self.module_name}/package LineItem'))
        self.assertFileExists(f'lib/{self.module_name}/package/messages/line_item.proto')
        self.assertFileExists(f'lib/{self.module_name}/package/messages/BUILD')
        self.assertEqual(0, self.system(f'bazel build //lib/{self.module_name}/package/messages:line_item_cc_proto'))

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