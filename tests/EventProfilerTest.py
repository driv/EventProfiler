import unittest as ut
from eventprofiler import eventprofile
import pandas as pd
import numpy as np


class Test(ut.TestCase):

    def testNormalProfile(self):
        result = eventprofile(self.data, self.signal, 1, 1)
        self.assertSeriesValuesEqual(result['mean'], [-2,  0,  1])
        self.assertSeriesValuesEqual(result['std'], [1, 0, 0])
        self.assertSeriesValuesEqual(result['count'], [2, 2, 2])

    def testFirstEventNotInResult(self):
        result = eventprofile(self.data, self.signal, 2, 1)
        self.assertSeriesValuesEqual(result['mean'], [-2, -1, 0, 1])
        self.assertSeriesValuesEqual(result['std'], [0, 0, 0, 0])
        self.assertSeriesValuesEqual(result['count'], [1, 1, 1, 1])

    def testLastEventNotInResult(self):
        result = eventprofile(self.data, self.signal, 1, 2)
        self.assertSeriesValuesEqual(result['mean'], [-3, 0, 1, 2])
        self.assertSeriesValuesEqual(result['std'], [0, 0, 0, 0])
        self.assertSeriesValuesEqual(result['count'], [1, 1, 1, 1])

    def testNormalProfile_Accum(self):
        result = eventprofile(self.data, self.signal, 1, 1, True)
        self.assertSeriesValuesEqual(result['mean'], [-6.5,  0. ,  7.5])
        self.assertSeriesValuesEqual(result['std'], [ 4.5,  0. ,  4.5])
        self.assertSeriesValuesEqual(result['count'], [2, 2, 2])

    @classmethod
    def setUpClass(cls):

        def makeSignal():
            columns = ['symbol1', 'symbol2']
            signal = [[False, False],
                      [True, False],
                      [False, False],
                      [False, False],
                      [False, True],
                      [False, False]]
            index = range(0, len(signal))
            dataframe = pd.DataFrame(data=signal, index=index, columns=columns)
            return dataframe

        def makeData():
            columns = ['symbol1', 'symbol2']
            prices = [[-1, 7],
                      [2, 8],
                      [3, 9],
                      [4, 10],
                      [5, 11],
                      [6, 12]]
            index = range(0, len(prices))
            dataframe = pd.DataFrame(data=prices, index=index, columns=columns)
            return dataframe

        cls.data = makeData()
        cls.signal = makeSignal()

    @classmethod
    def tearDownClass(cls):
        return None

    def assertSeriesValuesEqual(self, serie, array):
        np.testing.assert_array_equal(serie.values, array)


if __name__ == '__main__':
    import sys
    print(sys.version)
    ut.main()
