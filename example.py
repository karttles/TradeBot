import  json
import websocket
import candleMaker
#import resMaker


symbol = "btcusdt"
endpoint = f"wss://stream.binance.com:9443/ws/{symbol}@kline_1m"


array = []
def on_open(ws):
    print(f"Connected")
def on_message(ws, message):
    msg = json.loads(message)
    can = msg['k']
    is_candle_closed = can['x']

    if is_candle_closed:
        c = candleMaker.addCandel(can,array)
        array.append(c)
        print(array[0]['type'])

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
