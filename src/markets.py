from tabulate import tabulate
from poloniex import Poloniex
from blockchain import exchangerates

try:
    from config import apikey, secret
except ImportError:
    print 'error: rename src/config.py.changeme in src/config.py and edit it.'


polo = Poloniex(apikey, secret)
ticker = polo.returnTicker()
btc_usd = 1. / exchangerates.to_btc('USD', 1.)


results = []
for market, trades in polo.returnTradeHistory(start=0, end=2**32-1).items():
    amount = 0.0
    invested = 0.0
    for trade in trades:
        if trade['type'] == 'buy':
            amount += trade['amount']
            invested += trade['total']
        else:
            amount -= trade['amount']
            invested -= trade['total']

    current = ticker.get(market, {}).get('last', 0.0)
    value = amount * current
    delta = value - invested
    results.append((market, amount, value, delta, delta * btc_usd))


results.sort(key=lambda x: x[3], reverse=True)
