from datetime import datetime
import requests
import pandas as pd
import numpy as np
import candleMaker_FTX
import matplotlib.pyplot as plt
#1296000
import analyzer
symbol= 'BTC-PERP'
resolution = '900'
start_time = int(datetime.now().timestamp() - 1296000)
historical = requests.get(f'https://ftx.com/api/markets/{symbol}/candles?resolution=900&start_time={start_time}').json()
his_candles = historical['result']

peeps = []
supportLevels = []
resistanceLevels = []
buyOrders = []
sellOrders = []
levels = []

for candle in his_candles:
    candle = candleMaker_FTX.addCandel(candle,peeps)
    peeps.insert(0,candle)
    prices = []
    if len(peeps)>20:
        func = analyzer.analyze(peeps)
        #new Level
        if func:
            if func[1] == 'getLevel':
                level = {'startTime': 1.661702e+12,'endTime':1.662998e+12, "levelPrice": func[2]}
                levels.insert(0, level)
        

df = pd.DataFrame.from_records(peeps)
print(df.describe())    
df.plot(x ='time', y='close', kind = 'line')
df2 = pd.DataFrame.from_records(levels)
print(df2.describe())
df2.plot(y = 'levelPrice')
plt.show()

#print(len(peeps))
