import numpy as np
import pandas as pd

def eventprofile(data, events, lookback=1, lookforward=1):
    '''Event Profiler for a pandas.DataFrame of symbols indexed
    events are picked from the events dataframe by the symbol name and index.
    Output data is normalized agains the event value'''

    index = range(-lookback,lookforward+1)
    periods = pd.DataFrame([], index=index)

    i = 0
    for symbol in events.columns:
        for index in events[events[symbol] != False].index.tolist():
            loc = data.index.get_loc(index)
            period = data.iloc[loc-lookback:loc+lookforward+1][symbol]
            if period.size == lookback + lookforward + 1:
                period = period - period.iloc[lookback]
                periods[i] = period.values
                i += 1

    # Study Params
    mean = np.mean(periods, axis=1)
    mean.name = 'mean'
    std = np.std(periods, axis=1)
    std.name = 'std'
    count = periods.count(axis=1)
    count.name = 'count'

    return pd.concat([mean, std, count], axis=1)
