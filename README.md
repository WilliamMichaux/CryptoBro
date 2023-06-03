# CryptoBro

# `Indicators`

## `adx`

Calculates the Average Directional Index (ADX) indicator.

---

The ADX indicator is used to determine the strength of a trend in a particular security or asset. It is calculated based on the difference between the positive and negative directional indicators, and provides an indication of whether a security is trending or not. Higher ADX values generally indicate a stronger trend, while lower values suggest a weaker or non-existent trend.

---

### Parameters

- `data` (pandas.DataFrame): The stock data.
- `period` (int, optional): The period for the ADX calculation. Default value is 14.

### Returns

`pandas.DataFrame`: The ADX data.

### Example

```python
import pandas as pd

# Assuming 'data' is a pandas DataFrame containing the stock data
result = adx(data, period=14)
print(result)
```

Please note that the data parameter is expected to be a pandas DataFrame with columns named 'High', 'Low', and 'Close', representing the corresponding stock data for the given period.

## `aroon`

Calculates the Aroon indicator for a given period.

---

The Aroon indicator is a technical analysis tool that measures the time between highs and lows of an asset's price. It consists of two lines: Aroon Up and Aroon Down. The Aroon Up line measures the number of periods since the most recent high, while the Aroon Down line measures the number of periods since the most recent low.

---
### Parameters

- `data` (pandas.DataFrame): The data to calculate the Aroon on.
- `period` (int): The period to calculate the Aroon over. Default value is 25.

### Returns

A DataFrame containing the Aroon Up and Aroon Down values.

```python
import pandas as pd

def aroon(data, period=25):
    aroon_up = 100 * ((period - data['High'].rolling(window=period).apply(lambda x: x.argmax()) + 1) / period)
    aroon_down = 100 * ((period - data['Low'].rolling(window=period).apply(lambda x: x.argmin()) + 1) / period)
    return pd.DataFrame({'Aroon Up': aroon_up, 'Aroon Down': aroon_down})
```

## `bollinger_bands`

Calculates the Bollinger Bands for a given period.

---

The Bollinger Bands indicator is a popular technical analysis tool used to assess the volatility and potential price reversal in a financial instrument. It consists of three lines: the upper band, the middle band, and the lower band.

The middle band is calculated as the simple moving average (SMA) of the closing prices over the specified period. The upper band is obtained by adding two times the standard deviation of the closing prices to the middle band. Similarly, the lower band is obtained by subtracting two times the standard deviation from the middle band.

Traders and analysts use Bollinger Bands to identify periods of price consolidation and potential breakouts. When the price is near the upper band, it may indicate that the instrument is overbought, and a reversal or consolidation is likely. Conversely, when the price is near the lower band, it may indicate that the instrument is oversold, and a reversal or consolidation is possible.

It's important to note that Bollinger Bands are not meant to be used in isolation but in conjunction with other technical indicators and price analysis methods.

---

### Parameters
- `data` (pandas.DataFrame): The data to calculate the Bollinger Bands on.
- `period` (int): The period to calculate the Bollinger Bands over.

### Returns
pandas.DataFrame: A DataFrame containing the upper, middle, and lower Bollinger Bands.

**Example:**

```python
import pandas as pd

# Prepare data
data = pd.DataFrame({'Close': [10, 12, 15, 14, 16, 13, 11, 9]})

# Calculate Bollinger Bands
result = bollinger_bands(data, period=5)

print(result)
```

## `ema`

Calculates the Exponential Moving Average (EMA) for a given stock.

### Parameters
- `data` (pandas.DataFrame): The stock data.
- `window` (int): The window size for the EMA.

### Returns
pandas.DataFrame: The EMA values.

---

The Exponential Moving Average (EMA) is a widely used technical analysis indicator that gives more weight to recent price data points. It is calculated by applying a smoothing factor to the previous EMA and the current price.

The EMA is often used to identify trends, generate trading signals, and determine support and resistance levels. It is more responsive to recent price changes compared to other moving average types, such as the Simple Moving Average (SMA).

The `window` parameter determines the number of periods used in the EMA calculation. A shorter window will result in a more sensitive EMA that reacts quickly to price changes, while a longer window will produce a smoother EMA that is less affected by short-term fluctuations.

---

**Example:**

```python
import pandas as pd

# Prepare data
data = pd.DataFrame({'Close': [10, 12, 15, 14, 16, 13, 11, 9]})

# Calculate EMA
result = ema(data, window=5)

print(result)
```




## `macd`

Calculates the Moving Average Convergence Divergence (MACD) indicator.

### Parameters
- `data` (pandas.DataFrame): The stock data.
- `fast_period` (int): The period for the fast EMA.
- `slow_period` (int): The period for the slow EMA.
- `signal_period` (int): The period for the signal line.

### Returns
pandas.DataFrame: The MACD data.

---

The Moving Average Convergence Divergence (MACD) is a popular trend-following momentum indicator. It consists of three components: the MACD line, the signal line, and the histogram.

The MACD line is calculated by subtracting the slow Exponential Moving Average (EMA) from the fast EMA. The signal line is an EMA of the MACD line, and the histogram represents the difference between the MACD line and the signal line.

Traders and analysts use the MACD to identify potential buy and sell signals, determine the strength of a trend, and detect bullish or bearish market conditions. When the MACD line crosses above the signal line, it is considered a bullish signal, indicating a potential buying opportunity. Conversely, when the MACD line crosses below the signal line, it is considered a bearish signal, indicating a potential selling opportunity.

The `fast_period`, `slow_period`, and `signal_period` parameters define the number of periods used in the EMA calculations. Typically, the fast period is shorter than the slow period, and the signal period is shorter than both the fast and slow periods.

---

**Example:**

```python
import pandas as pd

# Prepare data
data = pd.DataFrame({'Close': [10, 12, 15, 14, 16, 13, 11, 9]})

# Calculate MACD
result = macd(data, fast_period=5, slow_period=10, signal_period=3)

print(result)
```

## `rsi`

Calculates the Relative Strength Index (RSI) indicator.

### Parameters
- `data` (pandas.DataFrame): The stock data.
- `period` (int): The period for the RSI calculation.

### Returns
pandas.DataFrame: The RSI data.

---

The Relative Strength Index (RSI) is a widely used momentum oscillator that measures the speed and change of price movements. It oscillates between 0 and 100 and is typically used to identify overbought or oversold conditions in a market.

The RSI is calculated based on the average gain and loss over a specified period. When the RSI value exceeds 70, it is considered overbought, suggesting that the price may be due for a reversal or correction. Conversely, when the RSI value falls below 30, it is considered oversold, indicating that the price may be due for a rebound or rally.

The `period` parameter determines the number of periods used in the RSI calculation. A shorter period will result in a more sensitive RSI that reacts quickly to price changes, while a longer period will produce a smoother RSI that is less affected by short-term fluctuations.

---

**Example:**

```python
import pandas as pd

# Prepare data
data = pd.DataFrame({'Close': [10, 12, 15, 14, 16, 13, 11, 9]})

# Calculate RSI
result = rsi(data, period=5)

print(result)
```

## `sma`

Calculates the Simple Moving Average (SMA) for a given stock.

### Parameters
- `data` (pandas.DataFrame): The stock data.
- `window` (int): The window size for the SMA.

### Returns
pandas.DataFrame: The SMA values.

---

The Simple Moving Average (SMA) is a commonly used technical analysis indicator that calculates the average price over a specified period. It is used to identify trends and smooth out price fluctuations.

The SMA is calculated by adding up the closing prices over a specified number of periods and then dividing the sum by the number of periods. This produces a single value that represents the average price over the specified window.

The `window` parameter determines the number of periods used in the calculation. A larger window will result in a smoother SMA that is less sensitive to short-term price fluctuations, while a smaller window will produce a more responsive SMA that reacts quickly to price changes.

---

**Example:**

```python
import pandas as pd

# Prepare data
data = pd.DataFrame({'Close': [10, 12, 15, 14, 16, 13, 11, 9]})

# Calculate SMA
result = sma(data, window=3)

print(result)
```


## `stochastic`

Calculates the Stochastic Oscillator indicator.

### Parameters
- `data` (pandas.DataFrame): The stock data.
- `period` (int): The period for the stochastic calculation.
- `smooth` (int): The period for the smoothing of the stochastic calculation.

### Returns
pandas.DataFrame: The Stochastic Oscillator data.

---

The Stochastic Oscillator is a momentum indicator that compares a security's closing price to its price range over a given period. It consists of two lines, %K and %D, which fluctuate between 0 and 100.

The %K line represents the current price's position within the recent price range. It is calculated as the percentage of the current price's distance from the lowest low within the specified period to the highest high within the same period.

The %D line is a moving average of the %K line and is often used as a signal line. It is calculated by smoothing the %K line over the specified smoothing period.

The `period` parameter determines the number of periods used in the calculation of the %K line. A larger period will result in a smoother %K line that is less sensitive to short-term price fluctuations.

The `smooth` parameter determines the number of periods used in the calculation of the %D line. It provides a smoothing effect to the %K line and helps to generate more reliable signals.

---

**Example:**

```python
import pandas as pd

# Prepare data
data = pd.DataFrame({'High': [50, 60, 70, 65, 55, 45, 50],
                     'Low': [40, 50, 60, 55, 45, 35, 40],
                     'Close': [45, 55, 65, 60, 50, 40, 45]})

# Calculate Stochastic Oscillator
result = stochastic(data, period=5, smooth=3)

print(result)
```
