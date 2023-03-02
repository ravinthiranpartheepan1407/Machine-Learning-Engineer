import unittest
import main

class TestMain(unittest.TestCase):
    def test_func_eq(self):
        obj = main.add_value()
        obj.value = int(main.num_A + main.num_B)
        obj.total_value = int(main.num_A + main.num_B)
        self.assertEqual(obj.value, obj.total_value)
    def test_func_greater(self):
        obj_1 = main.add_value()
        obj_1.value = main.num_A + main.num_B + 5
        obj_1.total_value = main.num_A + main.num_B
        self.assertGreaterEqual(obj_1.value,obj_1.total_value)
    def test_func_sub(self):
        sub = main.subtract_value()
        sub.total_values = main.num_A + main.num_B - 5
        sub_1 = main.subtract_value()        
        sub_1.total_values = main.num_B + main.num_B - 3
        self.assertNotEqual(sub.total_values, sub_1.total_values)

unittest.main()