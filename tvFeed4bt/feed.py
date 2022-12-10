from websocket import create_connection
import json
from threading import Thread
import random
import string
import re
import requests
from datetime import datetime
from time import sleep

symbol_name = "BTCUSDT"

def generateSession():
    stringLength = 12
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(stringLength))
    return "qs_" + random_string

def generateChartSession():
    stringLength = 12
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(stringLength))
    return "cs_" + random_string

def prependHeader(st):
    return "~m~" + str(len(st)) + "~m~" + st

def constructMessage(func, paramList):
    return json.dumps({
        "m": func,
        "p": paramList
    }, separators=(',', ':'))

def createMessage(func, paramList):
    return prependHeader(constructMessage(func, paramList))

def sendRawMessage(ws, message):
    ws.send(prependHeader(message))

def sendMessage(ws, func, args):
    ws.send(createMessage(func, args))

def get_result(result):
    d=result.split("\"v\":[")
    if len(d) > 1:
        d1=d[1].split("]}],\"ns\"")
        if len(d1) > 1 :
            d0 = d1[0].split(",")
            ts = datetime.fromtimestamp(float(d0[0])).strftime("%Y-%m-%dT%H:%M:%SZ")
            url = "http://127.0.0.1:8123/tv"
            msg = {'symbol':symbol_name, 'DT':ts, 'O':float(d0[1]), 'H':float(d0[2]), 'L':float(d0[3]), 'C':float(d0[4]), 'V':float(d0[5])}
            requests.post(url,json=msg)

# Initialize the headers needed for the websocket connection
headers = json.dumps({
    'Origin': 'https://data.tradingview.com'
})

# Then create a connection to the tunnel
ws = create_connection(
    'wss://data.tradingview.com/socket.io/websocket', headers=headers)

session = generateSession()

chart_session = generateChartSession()

# Then send a message through the tunnel
sendMessage(ws, "set_auth_token", ["unauthorized_user_token"])
sendMessage(ws, "chart_create_session", [chart_session, ""])
sendMessage(ws, "quote_create_session", [session])
sendMessage(ws, "quote_set_fields",
            [session, "ch", "chp", "current_session", "description", "local_description", "language", "exchange",
             "fractional", "is_tradable", "lp", "lp_time", "minmov", "minmove2", "original_name", "pricescale",
             "pro_name", "short_name", "type", "update_mode", "volume", "currency_code", "rchp", "rtc"])
sendMessage(ws, "quote_add_symbols", [session, symbol_name, {"flags": ['force_permission']}])

sendMessage(ws, "resolve_symbol",
            [chart_session, "symbol_1", "={\"symbol\":\""+symbol_name+"\",\"adjustment\":\"splits\"}"])
sendMessage(ws, "create_series", [chart_session, "s1", "s1", "symbol_1", "1", 1])

sendMessage(ws, "quote_fast_symbols", [session, symbol_name])

sendMessage(ws, "create_study", [chart_session, "st1", "st1", "s1", "achal@backtrader",
                                 {"length": 20, "col_prev_close": "false"}])
sendMessage(ws, "quote_hibernate_all", [session])

def funFeed():
    while True:
        try:
            sleep(1)
            result = ws.recv()
            pattern = re.compile("~m~\d+~m~~h~\d+$")
            if pattern.match(result):
                ws.send(result)
            else:
                get_result(result)

        except Exception as e:
            print(e)
            break

server_thread = Thread(target=funFeed)
server_thread.start()