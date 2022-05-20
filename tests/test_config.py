import unittest

import peapy


class TestConfig(unittest.TestCase):
    def test_set_attr(self):
        try:
            config = peapy.config.Config()
            config.test = "test"
        except Exception:
            self.fail("Config.__setattr__() failed.")

    def test_get_attr(self):
        try:
            config = peapy.config.Config()
            config.test = "test"
            self.assertEqual(config.test, "test")
        except Exception:
            self.fail("Config.__getattr__() failed.")

    def test_to_string(self):
        try:
            config = peapy.config.Config()
            config.test = {}
            config.test.test = "test"
            config.test.test2 = "test2"
            self.assertEqual(config.to_string(), "test:\n\ttest: test\n\ttest2: test2\n")
        except Exception:
            self.fail("Config.to_string() failed.")


if __name__ == '__main__':
    unittest.main()
