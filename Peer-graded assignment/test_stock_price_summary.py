import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_empty(self):
        """
        Test stock_price_summary when input list is empty.
        """
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual,expected)
        
    def test_stock_price_summary_single_positive(self):
        """
        Test stock_price_summary when input list is contains only one 
        positive value.
        """
        actual = a1.stock_price_summary([0.01])
        expected = (0.01, 0)
        self.assertEqual(actual,expected)
        
    def test_stock_price_summary_single_negative(self):
        """
        Test stock_price_summary when input list is contains only one 
        negative value.
        """
        actual = a1.stock_price_summary([-0.03])
        expected = (0, -0.03)
        self.assertEqual(actual,expected)
    
    def test_stock_price_summary_mixed_values(self):
        """
        Test stock_price_summary when input list is contains a mixture of
        0s, positives and negatives values.
        """
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual,expected)


if __name__ == '__main__':
    unittest.main(exit=False)
