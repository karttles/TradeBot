import methods
import levelMaker
def analyze(array,sups,ress):
    #start by getting mas
    avgVolume = methods.getAvgVolume(array,20)
    sma = methods.getSma(array,20)
    newCandle = array[0]
    lastCandle = array[1]


    #new 1.5 avg vol or new candle 2x last candle
    #newCandle['volume'] > 1.5*avgVolume
    if newCandle['volume'] > 1.3*avgVolume or newCandle['volume']>1.5*lastCandle['volume'] or newCandle['volume']<0.6*lastCandle['volume']:
        
        if methods.checkTrendCont:
            #last candle trend low ==  sup/res
            lastTrendCandle = methods.getLastTrendCandle(array)
            if lastTrendCandle['trend'] == 'bull':
                levelMaker.getSupport(lastTrendCandle,sups)
                print('get sup')
            if lastTrendCandle['trend'] == 'bear':
                levelMaker.getResistance(lastTrendCandle,ress)
                print('get res')
        else:
            if newCandle['trend'] == 'bull':
                levelMaker.getSupport(newCandle,sups)
                print('get sup')
            if newCandle['trend'] == 'bear':
                levelMaker.getResistance(newCandle,ress)
                print('get res')

    #touch and close above/belo last entry
    if newCandle['trend'] != lastCandle['trend']:
        if newCandle['trend'] == 'bull':
                if newCandle['close']*1.05 > lastCandle['open']:
                    if methods.checkTouch :
                        print('position entry')

        if newCandle['trend'] == 'bear':
           if newCandle['close']*0.95 > lastCandle['open']:
                print('new resistance')
                if methods.checkTouch :
                    print('position entry')
