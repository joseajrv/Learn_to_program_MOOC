import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_value_0(self):
        """
        Test swap_k when k value is 0.
        """
        k = 0
        nums = [2, 3]
        nums_expected = [2, 3]
        
        a1.swap_k(nums, k)
        
        self.assertEqual(nums, nums_expected)
        
    def test_swap_k_value_1(self):
        """
        Test swap_k when k value is 1.
        """
        k = 1
        nums = [1, 6]
        nums_expected = [6, 1]
        
        a1.swap_k(nums, k)
        
        self.assertEqual(nums, nums_expected)
        
    def test_swap_k_multiple_even(self):
        """
        Test swap_k when k value is 2 and L is even with multiple entries.
        """
        k = 2
        nums = [1, 2, 3, 4, 5, 6]
        nums_expected = [5, 6, 3, 4, 1, 2]
        
        a1.swap_k(nums, k)
        
        self.assertEqual(nums, nums_expected)  
        
    def test_swap_k_multiple_odd(self):
        """
        Test swap_k when k value is 2 and L is odd with multiple entries.
        """
        k = 3
        nums = [1, 2, 3, 4, 5, 6, 7]
        nums_expected = [5, 6, 7, 4, 1, 2, 3]
        
        a1.swap_k(nums, k)
        
        self.assertEqual(nums, nums_expected)   

if __name__ == '__main__':
    unittest.main(exit=False)
