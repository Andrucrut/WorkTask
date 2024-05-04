import unittest


def find_divisors(numbers):
    if numbers == []:
        return []
    mas = []
    for i in range(1, min(numbers) + 1):
        if all(n % i == 0 for n in numbers):
            mas.append(i)
    return mas


class TestFindCommonDivisors(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_divisors([]), [])

    def test_single_number(self):
        self.assertEqual(find_divisors([12]), [1, 2, 3, 4, 6, 12])

    def test_two_numbers(self):
        self.assertEqual(find_divisors([12, 18]), [1,2, 3, 6])

    def test_three_numbers(self):
        self.assertEqual(find_divisors([42, 12, 18]), [1,2, 3, 6])

    def test_no_common_divisors(self):
        self.assertEqual(find_divisors([25, 35, 49]), [1])
