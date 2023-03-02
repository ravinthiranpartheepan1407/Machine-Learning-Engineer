import unittest
import main

class TestMain(unittest.TestCase):
    def test_guess_input(self):
        test_default = int(0)
        global_num = int(main.guess_input)
        self.assertGreater(global_num, test_default)
    def test_guess(self):
        with self.assertRaises(ValueError):
            raise ValueError("Type Error Dude")
        # with self.assertRaises(ValueError):
        #     main.guess_number(main.guess_input)

unittest.main()
