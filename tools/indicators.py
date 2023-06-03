import pandas as pd


def adx(data, period=14):
    '''
    Calculates the Average Directional Index (ADX) indicator.

    Parameters:
        data (pandas.DataFrame): The stock data.
        period (int): The period for the ADX calculation.

    Returns:
        pandas.DataFrame: The ADX data.
    '''

    high = data['High']
    low = data['Low']
    close = data['Close']

    tr1 = high - low
    tr2 = abs(high - close.shift())
    tr3 = abs(low - close.shift())

    true_range = pd.DataFrame({'TR1': tr1, 'TR2': tr2, 'TR3': tr3}).max(axis=1)
    plus_di = 100 * (high.diff() / true_range).ewm(span=period, adjust=False).mean()
    minus_di = 100 * (low.diff() / true_range).ewm(span=period, adjust=False).mean()

    dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di)
    adx = dx.ewm(span=period, adjust=False).mean()

    return pd.DataFrame({'ADX': adx, '+DI': plus_di, '-DI': minus_di})


def aroon(data, period=25):
    '''
    Calculates the Aroon indicator for a given period.

    Parameters:
    data (pandas.DataFrame): The data to calculate the Aroon on.
    period (int): The period to calculate the Aroon over.

    Returns:
    pandas.DataFrame: A DataFrame containing the Aroon Up and Aroon Down values.
    '''
    aroon_up = 100 * ((period - data['High'].rolling(window=period).apply(lambda x: x.argmax()) + 1) / period)
    aroon_down = 100 * ((period - data['Low'].rolling(window=period).apply(lambda x: x.argmin()) + 1) / period)

    return pd.DataFrame({'Aroon Up': aroon_up, 'Aroon Down': aroon_down})


def bollinger_bands(data, period):
    '''
    Calculates the Bollinger Bands for a given period.

    Parameters:
    data (pandas.DataFrame): The data to calculate the Bollinger Bands on.
    period (int): The period to calculate the Bollinger Bands over.

    Returns:
    pandas.DataFrame: A DataFrame containing the upper, middle, and lower Bollinger Bands.
    '''
    middle_band = data['Close'].rolling(window=period).mean()
    std = data['Close'].rolling(window=period).std()
    upper_band = middle_band + (2 * std)
    lower_band = middle_band - (2 * std)

    return pd.concat([upper_band, middle_band, lower_band], axis=1, keys=['Upper Band', 'Middle Band', 'Lower Band'])


def ema(data, window):
    '''
    Calculates the Exponential Moving Average (EMA) for a given stock.

    Parameters:
        data (pandas.DataFrame): The stock data.
        window (int): The window size for the EMA.

    Returns:
        pandas.DataFrame: The EMA values.
    '''
    return pd.DataFrame(data['Close'].ewm(span=window, adjust=False).mean(), columns=['EMA'])


def macd(data, fast_period=12, slow_period=26, signal_period=9):
    '''
    Calculates the Moving Average Convergence Divergence (MACD) indicator.

    Parameters:
        data (pandas.DataFrame): The stock data.
        fast_period (int): The period for the fast EMA.
        slow_period (int): The period for the slow EMA.
        signal_period (int): The period for the signal line.

    Returns:
        pandas.DataFrame: The MACD data.
    '''

    ema_fast = data['Close'].ewm(span=fast_period, adjust=False).mean()
    ema_slow = data['Close'].ewm(span=slow_period, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    histogram = macd - signal
    return pd.DataFrame({'MACD': macd, 'Signal': signal, 'Histogram': histogram})


def rsi(data, period=14):
    '''
    Calculates the Relative Strength Index (RSI) indicator.

    Parameters:
        data (pandas.DataFrame): The stock data.
        period (int): The period for the RSI calculation.

    Returns:
        pandas.DataFrame: The RSI data.
    '''
    delta = data['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return pd.DataFrame({'RSI': rsi})


def sma(data, window):
    '''
    Calculates the Simple Moving Average (SMA) for a given stock.

    Parameters:
        data (pandas.DataFrame): The stock data.
        window (int): The window size for the SMA.

    Returns:
        pandas.DataFrame: The SMA values.
    '''
    return pd.DataFrame(data['Close'].rolling(window=window).mean(), columns=['SMA'])


def stochastic(data, period=14, smooth=3):
    """
    Calculates the Stochastic Oscillator indicator.

    Parameters:
        data (pandas.DataFrame): The stock data.
        period (int): The period for the stochastic calculation.
        smooth (int): The period for the smoothing of the stochastic calculation.

    Returns:
        pandas.DataFrame: The Stochastic Oscillator data.
    """

    low_min = data['Low'].rolling(window=period).min()
    high_max = data['High'].rolling(window=period).max()
    k = 100 * ((data['Close'] - low_min) / (high_max - low_min))
    d = k.rolling(window=smooth).mean()

    return pd.DataFrame({'%K': k, '%D': d})
