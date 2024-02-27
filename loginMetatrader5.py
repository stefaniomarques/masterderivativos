import MetaTrader5 as mt5
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# Inicialize a conexão com o MetaTrader 5
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

account = 559098945
server = "XPMT5-DEMO"
authorized = mt5.login(account, password="XsoT0dZW", server=server)

if authorized:
    print("Connected to account #{}".format(account))
    
    account_info = mt5.account_info()
    print(account_info)

    print("Show account_info()._asdict():")
    account_info_dict = account_info._asdict()
    for prop, value in account_info_dict.items():
        print("  {}={}".format(prop, value))
else:
    print("Failed to connect at account #{}, error code: {}".format(account, mt5.last_error()))

# Encerre a conexão com o MetaTrader 5
mt5.shutdown()