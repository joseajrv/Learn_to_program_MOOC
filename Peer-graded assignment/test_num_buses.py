import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses_value_0(self):
        """
        Test num_buses when value is 0.
        """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual,expected)
    
    def test_num_buses_value_1(self):
        """
        Test num_buses when value is 1 as a minimun for 1 bus.
        """
        actual = a1.num_buses(1)
        expected = 1
        self.assertEqual(actual,expected)
        
    def test_num_buses_value_2(self):
        """
        Test num_buses when value is 50 as the maximum for 1 bus.
        """
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual,expected)
        
    def test_num_buses_value_3(self):
        """
        Test num_buses when value is 51 as the minimum for 2 buses.
        """
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(actual,expected)
        
    def test_num_buses_value_4(self):
        """
        Test num_buses when value is 1756, large value.
        """
        actual = a1.num_buses(1756)
        expected = 36
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main(exit=False)
