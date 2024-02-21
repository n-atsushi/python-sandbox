import unittest

def fizz_buzz():
    result = []
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):
        expected = [str(i) if (i % 3 != 0 and i % 5 != 0) else ("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0)) for i in range(1, 101)]
        self.assertEqual(fizz_buzz(), expected)

if __name__ == '__main__':
    unittest.main()