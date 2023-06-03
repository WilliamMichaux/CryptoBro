import unittest
import pandas as pd
import numpy as np

from indicators import *


class IndicatorTestCase(unittest.TestCase):
    def test_adx(self):
        data = pd.DataFrame({
            'High': [10, 12, 15, 14, 16, 13, 11, 9],
            'Low': [8, 9, 11, 10, 11, 10, 9, 8],
            'Close': [9, 10, 13, 11, 15, 12, 10, 9]
        })
        result = adx(data)
        self.assertEqual(result.shape, (8, 3))
        self.assertAlmostEqual(result['ADX'].tolist(), [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 14.17322834645669], places=2)

    def test_aroon(self):
        data = pd.DataFrame({
            'High': [10, 12, 15, 14, 16, 13, 11, 9],
            'Low': [8, 9, 11, 10, 11, 10, 9, 8]
        })
        result = aroon(data)
        self.assertEqual(result.shape, (8, 2))
        self.assertEqual(result['Aroon Up'].tolist(), [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 100.0])
        self.assertEqual(result['Aroon Down'].tolist(), [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 12.5])


if __name__ == '__main__':
    unittest.main()
