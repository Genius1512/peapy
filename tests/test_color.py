import unittest

import peapy


class TestColor(unittest.TestCase):
    def test_hex(self):
        self.assertEqual(
            peapy.Color("#FFFFFF").hex,
            "#ffffffff"
        )

        self.assertEqual(
            peapy.Color("#ff").hex,
            "#ffffffff"
        )

        self.assertEqual(
            peapy.Color("#0f0").hex,
            "#00ff00ff"
        )

    def test_tuple_3(self):
        self.assertEqual(
            peapy.Color(0, 0, 0).hex,
            "#000000ff"
        )

        self.assertEqual(
            peapy.Color(255, 255, 255).hex,
            "#ffffffff"
        )

    def test_tuple_4(self):
        self.assertEqual(
            peapy.Color(0, 0, 0, 0).hex,
            "#00000000"
        )

        self.assertEqual(
            peapy.Color(255, 255, 255, 255).hex,
            "#ffffffff"
        )


if __name__ == '__main__':
    unittest.main()
