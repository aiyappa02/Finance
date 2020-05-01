import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
#from matplotlib.finance import candlestick_ohlc
import mplfinance as mpf
#from mplfinance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('tsla.csv',parse_dates=True,index_col=0)
#df=df.set_index("Date")

# df_ohlc=df['Adj Close'].resample('10D').ohlc()
# df_volume=df['Volume'].resample('10D').sum()

#print(df.head())

#df_ohlc.reset_index(inplace=True)
#df_ohlc['Date']=df_ohlc['Date'].map(mdates.date2num)
#print(df_ohlc.head())

#
mpf.plot(df)
#candlestick_ohlc(ax1, df_ohlc.values, width=2,colorup='g')
#ax2.fill_between(df_volume.index.map(mdates.date2num),df_volume.values,0)
#plt.show()
