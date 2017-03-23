import matplotlib.pyplot as plt
import eventprofiler as ep
import pandas as pd


def makeSignal():
    columns = ['symbol1', 'symbol2']
    signal = [[False, False],
              [True, True],
              [False, True],
              [True, False],
              [False, True],
              [False, False]]
    index = range(0, len(signal))
    dataframe = pd.DataFrame(data=signal, index=index, columns=columns)
    return dataframe


def makeData():
    columns = ['symbol1', 'symbol2']
    prices = [[-1, 0],
              [2, 1],
              [3, 2],
              [4, 10],
              [5, 8],
              [6, 12]]
    index = range(0, len(prices))
    dataframe = pd.DataFrame(data=prices, index=index, columns=columns)
    return dataframe


def main():
    lookback = 1
    lookforward = 2
    result = ep.eventprofile(
        makeData(), makeSignal(), lookback, lookforward)

    plt.clf()
    plt.plot(result['mean'])
    plt.errorbar(result['mean'].index, result['mean'],
                 yerr=result['std'], ecolor='#AAAAFF')
    plt.xlim(-lookback - 1, lookforward + 1)
    plt.savefig('test.pdf', format='pdf')

if __name__ == '__main__':
    main()
