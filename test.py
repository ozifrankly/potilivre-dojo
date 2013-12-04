import unittest 
import dojo

class TestFizzBuzz(unittest.TestCase):
    def test_list_size(self):
        new_list = dojo.umAcem()
        self.assertEqual(
				100,
				len(new_list)
			)

    def test_fizz(self):
        self.assertEqual(
                "Fizz",
                dojo.fizz(9)
            )
        self.assertNotEqual(
                "Fizz",
                dojo.fizz(5)
            )

    def test_buzz(self):
        self.assertEqual(
				"Buzz",
				dojo.buzz(20)
			)
        self.assertNotEqual(
				"Buzz",
				dojo.buzz(33)
			)

    def test_fizz_buzz(self):
        self.assertEqual(
				"FizzBuzz",
				dojo.fizz_buzz(15)
            )

        self.assertNotEqual(
                "FizzBuzz",
                dojo.fizz_buzz(33)
            )
        self.assertNotEqual(
                "FizzBuzz",
                dojo.fizz_buzz(20)
            )


if __name__ == "__main__":
	unittest.main()

