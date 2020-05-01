import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

df = pd.read_csv('tsla.csv')
df=df.set_index("Date")

df['100MA']=df['Adj Close'].rolling(window=100).mean()
df.dropna(inplace=True)
print(df.tail())
print(df.head())

ax1= plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2= plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1,sharex=ax1)

ax1.plot(df.index,df['Adj Close'])
ax1.plot(df.index,df['100MA'])
ax2.bar(df.index,df['Volume'])

plt.show()
