
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


def getLastTrendCandle(array):
    lastCandle = array[0]
    i = 0
    while array[i]['trend'] == lastCandle['trend']:
        i =+ 1
        break 
    return array[i]

def getLevel(array):
        newCandle = array[0]
        oldCandle = array[1]
    #higher volume same trend
        if checkTrendCont(newCandle,oldCandle):
            lastCandle = getLastTrendCandle(array)
            return lastCandle['open']
    #higher volume diff trend
        else :
            if newCandle['trend'] == 'bull':
                return newCandle['open']
            else:
                return newCandle['close']