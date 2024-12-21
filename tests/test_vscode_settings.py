import unittest
import json
import os

class TestVSCodeSettings(unittest.TestCase):
    def setUp(self):
        self.settings_path = os.path.join('.vscode', 'settings.json')
        with open(self.settings_path) as f:
            self.settings = json.load(f)

    def test_unittest_enabled(self):
        self.assertTrue(self.settings['python.testing.unittestEnabled'])
        self.assertFalse(self.settings['python.testing.pytestEnabled'])

    def test_unittest_args(self):
        unittest_args = self.settings['python.testing.unittestArgs']
        self.assertEqual(len(unittest_args), 5)
        self.assertEqual(unittest_args[0], '-v')
        self.assertEqual(unittest_args[1], '-s')
        self.assertEqual(unittest_args[2], '.')
        self.assertEqual(unittest_args[3], '-p')
        self.assertEqual(unittest_args[4], '*test.py')

    def test_settings_structure(self):
        required_keys = [
            'python.testing.unittestArgs',
            'python.testing.pytestEnabled',
            'python.testing.unittestEnabled'
        ]
        for key in required_keys:
            self.assertIn(key, self.settings)

if __name__ == '__main__':
    unittest.main()
