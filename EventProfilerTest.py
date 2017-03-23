import unittest
import EventProfiler
import pandas as pd


class Test(unittest.TestCase):

    def testNormalProfile(self):
        result = EventProfiler.eventprofiler(self.data, self.signal, 1, 1)
        assertValuesEqualsTo(result['mean'], [-2,  0,  1])
        assertValuesEqualsTo(result['std'], [1, 0, 0])
        assertValuesEqualsTo(result['count'], [2, 2, 2])

    def testFirstEventNotInResult(self):
        result = EventProfiler.eventprofiler(self.data, self.signal, 2, 1)
        assertValuesEqualsTo(result['mean'], [-2, -1, 0, 1])
        assertValuesEqualsTo(result['std'], [0, 0, 0, 0])
        assertValuesEqualsTo(result['count'], [1, 1, 1, 1])

    def testLastEventNotInResult(self):
        result = EventProfiler.eventprofiler(self.data, self.signal, 1, 2)
        assertValuesEqualsTo(result['mean'], [-3, 0, 1, 2])
        assertValuesEqualsTo(result['std'], [0, 0, 0, 0])
        assertValuesEqualsTo(result['count'], [1, 1, 1, 1])

    @classmethod
    def setUpClass(cls):

        def makeSignal():
            signal = [[False, False], [True, False], [False, False],
                      [False, False], [False, True], [False, False]]
            index = range(0, len(signal))
            columns = ['symbol1', 'symbol2']
            dataframe = pd.DataFrame(data=signal, index=index, columns=columns)
            return dataframe

        def makeData():
            columns = ['symbol1', 'symbol2']
            prices = [[-1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]
            index = range(0, len(prices))
            dataframe = pd.DataFrame(data=prices, index=index, columns=columns)
            return dataframe

        cls.data = makeData()
        cls.signal = makeSignal()

    @classmethod
    def tearDownClass(cls):
        return None


def assertValuesEqualsTo(df, arr):
    assert list(df.values) == list(arr)

if __name__ == '__main__':
    unittest.main()
