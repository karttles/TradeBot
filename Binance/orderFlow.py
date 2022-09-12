import  json
import websocket
from datetime import datetime

symbol = "btcusdt"
endpoint = f"wss://stream.binance.com:9443/ws/{symbol}@trade"



def getTime():
    time = datetime.now().strftime("%M")
    return time

def getFormat(msg):
    return {
        'price': float(msg['p']),
        'quantity': float(msg['q']),
        'maker': msg['m'],
        'trend' : ""
        }
def getDir(msg,lastOrder):
    if msg['price']> lastOrder['price']:
        trend = 'buy'
    elif msg['price']< lastOrder['price']:
        trend = 'sell'
    else:
        trend = lastOrder['trend']
    return trend


def addNum(newMsg,lastTime):
    msg = getFormat(newMsg)
    msg['trend'] = getDir(msg,lastTime[1])
    time = int(getTime())
    print(msg, 'is new msg')
    print(lastTime[1], 'is last msg')

  #  print(lastTime[1]['price'],lastTime[1]['trend'],"|",msg['price'],msg['trend'])
    if time == lastTime[0]:
        if msg['maker']:
            s = 'maker'
        else:
            if msg['trend'] == 'sell':
                print('sell')
            if msg['trend'] == 'buy':
                print('buy')

        lastTime=msg
    else :
        print('diff')
        lastTime[0] = int(getTime())
    return lastTime
    

array = [int(getTime()),{'price':1,'trend':'sell'
}]

def on_open(ws):
    print(f"Connected")
def on_message(ws, message):
        msg = json.loads(message)
        
def on_error(ws, error):
    print(f"Error: {error}")
def on_close( close_msg):
    print(f"Connection close")
ws = websocket.WebSocketApp(endpoint,
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
ws.run_forever()
