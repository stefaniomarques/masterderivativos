import MetaTrader5 as mt5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()
 
print(mt5.terminal_info())
print(mt5.version())

symbol="VALE3"
mt5.symbol_select(symbol,True)
lot = 100
price = mt5.symbol_info_tick(symbol).ask
deviation = 2
request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": float(lot),
    "type": mt5.ORDER_TYPE_SELL,
    "price": price,
    "deviation": deviation,
    "magic": 123,
    "comment": "venda",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN
}
result = mt5.order_send(request)
print(result)
print(price)

mt5.shutdown()
