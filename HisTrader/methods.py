
def getAvgVolume(array,count):
    i=0
    num = count-1
    sum = 0
    while i < num:
        sum += array[i]['volume']
        i +=1
    return sum/num

def getSma(array,count):
    i=0
    num = count-1
    sum = 0
    while i < num:
        sum += array[i]['close']
        i +=1
    return sum/num

def checkTrendCont(newCandle,lastCandle):
    if newCandle['trend'] != lastCandle['trend']:
        return 'False'
    else:
        return 'True'

def checkTouch(candle,res,sup):
    if candle['trend'] == 'bull':
        if candle['high'] > res:
            return 'True'

    if candle['trned'] == 'bear':
        if candle['low'] < sup:
            return 'True'
    else :
        return 'False'

def getLastTrendCandle(array):
    lastCandle = array[0]
    LastTrendCandle = {'open': float,
            'close': float,
            'top': float,
            'low': float,
            'volume': float,
            'trend': "",
            'type': "",
            'times':""}
    i = 0
    while array[i] == lastCandle['trend']:
        LastTrendCandle = array[i]
        i =+ 1
        print(f'last candle is {LastTrendCandle}')
    return LastTrendCandle