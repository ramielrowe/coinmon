# The MIT License (MIT)
#
# Copyright (c) 2014, Andrew Melton
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

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

