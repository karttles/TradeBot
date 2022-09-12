def addCandel(candle,array):

    def getFormat(candle):

        return { 
            'open': float(candle['open']),
            'close': float(candle['close']),
            'top': float(candle['high']),
            'low': float(candle['low']),
            'volume': float(candle['volume']),
            'trend': "",
            'type': "",
            'time':candle['time']
            }
        
    def getOtherData(candle):

        def getTrend(candle,array):
                if candle['open'] > candle['close']:
                    return 'bear'
            
                if candle['open'] < candle['close']:
                    return 'bull'
                
                else:
                    return array[0]['trend']
                
        def getBody(candle,trend):
            if trend  == 'bear':
                topWick = candle['top']-candle['open']
                lowWick = candle['close']-candle['low']
                body = candle['open']-candle['close']
            if trend == 'bull':
                topWick = candle['top']-candle['close']
                lowWick = candle['open']-candle['low']
                body = candle['close']-candle['open']
            return [topWick,lowWick,body]


        def getType(topWick,lowWick,body,candleRange):
            
            if topWick > 0.7*candleRange:
                return 'shootingStar'
            if lowWick > 0.7*candleRange:
                return 'hammer'

            if body < 0.1*candleRange and topWick/lowWick <= 1.3:
                return 'doji'
            if body > 0.4*candleRange and body < 0.52*lowWick:
                return 'bull rejection'
            if body > 0.4*candleRange and body < 0.52*topWick:
                return 'bear rejection'

            if body >= 0.7*candleRange:
                return 'trendCandle'
            else:
                return'basicCandle'
        
        def getRange(candle):
            candleRange = candle['top'] - candle['low']
            return candleRange

        trend = getTrend(candle,array)

        bodys = getBody(candle,trend)

        topWick,lowWick,body = bodys[0],bodys[1],bodys[2]

        candleRange = getRange(candle)

        candleType = getType(topWick,lowWick,body,candleRange) 
        
        BodyRangeRation = body/candleRange

        return [candleType, trend,topWick,lowWick,body,candleRange,BodyRangeRation]

    c = getFormat(candle)
    otherData = getOtherData(c)
    c.update({'type': otherData[0], "trend": otherData[1], 'topWick': otherData[2],'lowWick':otherData[3],'body': otherData[4],'range': otherData[5],'BodyRangeRation': otherData[6]})
    return c
    
