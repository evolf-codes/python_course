# ASSERT - if statement is true - do nothing
# if statement is FALSE - raise ERROR

# def add_positive(x,y):
#     assert x > 0 and y > 0, ("BOTH nums must be positive")
#     return x + y
#
# print(add_positive(1,1))


import unittest
from Kraken_API import currency_pairs
from ddt import ddt, data

@ddt
class Tests(unittest.TestCase):
    @data('XBTUSD', 'XBTEUR', 'XBTCAD', 'ETHUSD')
    def test_currency(self,value):
        self.assertIn('OK',currency_pairs(value),msg="HELLO")

if __name__ == "__main__":
    unittest.main()
