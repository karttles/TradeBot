from array import array
from datetime import datetime
import requests
import pandas as pd
import numpy as np
import candleMaker_FTX
#1296000
import analyzer
symbol= 'BTC-PERP'
resolution = '60'
start_time = int(datetime.now().timestamp() - 1296000)
historical = requests.get(f'https://ftx.com/api/markets/{symbol}/candles?resolution=900&start_time={start_time}').json()
his_candles = historical['result']

peeps = []
suportLevels = []
resistanceLevels = []
buyOrders = []
selOrders = []

for candle in his_candles:
    candle = candleMaker_FTX.addCandel(candle,peeps)
    peeps.append(candle)
    if len(peeps)>20:
        analyzer.analyze(peeps,suportLevels,resistanceLevels)

df = pd.DataFrame.from_records(peeps)
print(df.head())    