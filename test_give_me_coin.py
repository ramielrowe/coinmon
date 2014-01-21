import unittest

import give_me_coin


class TestGiveMeCoin(unittest.TestCase):
    def test_coin_str(self):
        result = give_me_coin.coin_str(2.123456, '1.1', '3')
        self.assertEqual(result, '2.12346 ($2.336, $6.370)')

    def test_strip_user(self):
        result = give_me_coin.strip_user('ramielrowe', 'ramielrowe.test')
        self.assertEqual(result, 'test')

    def test_status_str_up(self):
        result = give_me_coin.status_str('1', '1')
        self.assertEqual(result, 'OK')

    def test_status_str_down(self):
        result = give_me_coin.status_str('0', '1')
        self.assertEqual(result, 'DOWN! (1969-12-31 19:00:01)')