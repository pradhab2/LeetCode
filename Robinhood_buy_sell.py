import heapq


class Solution:
    def __init__(self):
        self.buy = []
        self.sell = []
        self.count = 0

    def put_order(self, order):
        price, quantity, tran_type = order
        price = int(price)
        quantity = int(quantity)
        if tran_type == 'buy':
            # max-heap
            heapq.heappush(self.buy, (-price, price, quantity))
        elif tran_type == 'sell':
            # min-heap
            heapq.heappush(self.sell, (price, price, quantity))

        self.fulfill()

    def stream(self, orders):
        for order in orders:
            self.put_order(order)

    def fulfill(self):
        while self.buy and self.sell:
            b_key, b_price, b_quantity = self.buy[0]
            s_key, s_price, s_quantity = self.sell[0]
            if b_price >= s_price:
                heapq.heappop(self.buy)
                heapq.heappop(self.sell)
                if b_quantity < s_quantity:
                    heapq.heappush(self.sell, (s_key, s_price, s_quantity - b_quantity))
                elif b_quantity > s_quantity:
                    heapq.heappush(self.buy, (b_key, b_price, b_quantity - s_quantity))

                self.count += min(s_quantity, b_quantity)

            else:
                break


import unittest
class Test(unittest.TestCase):
    def test_1(self):
        sol = Solution()
        orders = [
            ['150', '5', 'buy'],  # Order A
            ['190', '1', 'sell'],  # Order B
            ['200', '1', 'sell'],  # Order C
            ['100', '9', 'buy'],  # Order D
            ['140', '8', 'sell'],  # Order E
            ['210', '4', 'buy'],  # Order F
        ]

        sol.stream(orders)
        print(sol.count)
        self.assertEqual(sol.count, 9)

    # def test_2(self):
    #     sol = Solution()
    #     orders = [
    #         ['150', '5', 'buy'],  # OrderA
    #         ['190', '1', 'sell'],  # OrderB
    #         ['200', '1', 'sell'],  # OrderC
    #         ['100', '9', 'buy'],  # OrderD
    #         ['140', '8', 'sell'],  # OrderE
    #         ['210', '100', 'buy']]  # OrderF
    #
    #     sol.stream(orders)
    #     print(sol.count)
    #     self.assertEqual(sol.count, 10)
    #
    # def test_3(self):
    #     sol = Solution()
    #     orders = [['210', '100', 'buy'],  # OrderF
    #               ['190', '1', 'sell'],  # OrderB
    #               ['200', '1', 'sell'],  # OrderC
    #               ['100', '9', 'buy'],  # OrderD
    #               ['140', '8', 'sell'],  # OrderE
    #               ['150', '5', 'buy']  # OrderA
    #               ]
    #
    #     sol.stream(orders)
    #     print(sol.count)
    #     self.assertEqual(sol.count, 10)
    #
    # def test_4(self):
    #     sol = Solution()
    #     orders = [['150', '10', 'buy'],
    #               ['165', '7', 'sell'],
    #               ['168', '3', 'buy'],
    #               ['155', '5', 'sell'],
    #               ['166', '8', 'buy']
    #               ]
    #
    #     sol.stream(orders)
    #     print(sol.count)
    #     self.assertEqual(sol.count, 11)
    #

if __name__ == "__main__":
    unittest.main(verbosity=2)
