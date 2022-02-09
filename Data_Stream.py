import keys
import json , requests
import ARIMA
import websocket
import config
#def on_open(ws):
#    print("opened")
    #auth_data = {
    #    "action": "authenticate",
    #    "data": {"key_id": keys.API_KEY, "secret_key": keys.SECRET_KEY}


#
#    listen_message = {"action": "listen", "data": {"streams": ["AM.TSLA"]}}

#    ws.send(json.dumps(listen_message))


#def on_message(ws, message):
#    print("received a message")
    #print(message)
    #Counter += 1

#def on_close(ws):
#    print("closed connection")

#ws.run_forever()

#if len(forecast) > Counter:
#    Counter = 0


#working
minute_bars_url = config.BARS_URL + '/5min?symbols=MSFT'
def message(minute,headers):
    requests.get(minute,headers)
ls = message(minute_bars_url, headers=config.HEADERS)
print(json.dumps( ls.json(), indent=4))
