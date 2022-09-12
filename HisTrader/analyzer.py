from hashlib import new
import methods
from datetime import datetime

def analyze(array):

    #start by getting mas
    avgVolume = methods.getAvgVolume(array,20)
    newCandle = array[0]
    lastCandle = array[1]

    #new candle 2x > last candle
        
    #new candle 2x < last candle
    #if newCandle['volume']*2 < lastCandle['volume']:
    
    #new candle 1.5 > avgVolume
    #if newCandle['volume'] > 1.5*avgVolume:

    if newCandle['volume'] > 2*lastCandle['volume'] and newCandle['volume']> 1.2*avgVolume:
        newLevel = methods.getLevel(array)
        return ["True",'getLevel',newLevel]


    #new candle close bellow/above last candle entry LOW VOL
    if newCandle['trend'] == 'bull':
        if newCandle['close'] > lastCandle['open']:
                func = 'openLong'
                touchPrice = lastCandle['low']
                return ["True",func,touchPrice]

    if newCandle['trend'] == 'bear':
        if newCandle['close'] < lastCandle['open']:
                func = 'openShort'
                touchPrice = lastCandle['top']
                return ["True",func,touchPrice]
    else:
        return ["False",""]