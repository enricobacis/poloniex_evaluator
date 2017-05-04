from tabulate import tabulate
from poloniex import Poloniex

try:
    from config import apikey, secret
except ImportError:
    print 'error: rename src/config.py.changeme in src/config.py and edit it.'


def get_results(polo, market='all'):
    history = polo.returnTradeHistory(currencyPair=market, start=0, end=2**32-1)
    ticker = polo.returnTicker()

    for market, trades in history.items():

        amount = 0.0
        invested = 0.0

        for trade in trades:
            sign = +1 if trade['type'] == 'buy' else -1
            amount += sign * trade['amount']
            invested += sign * trade['total']

        current = ticker.get(market, {}).get('last', 0.0)
        value = (amount * current)
        delta = value - invested
        yield (market, amount, value, delta)


if __name__ == "__main__":
    polo = Poloniex(apikey, secret)
    results = [(m, a, v, d) for (m, a, v, d) in get_results(polo) if v > 10e-4]
    results.sort(key=lambda (m, a, v, d): d, reverse=True)
    print tabulate(results, headers=['market', 'shares', 'value', 'delta'])
