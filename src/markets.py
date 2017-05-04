from collections import namedtuple
from tabulate import tabulate
from poloniex import Poloniex

try:
    from config import apikey, secret
except ImportError:
    print 'error: rename src/config.py.changeme in src/config.py and edit it.'


Result = namedtuple('Result', ['market', 'shares', 'value', 'delta'])

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
        yield Result(market, amount, value, delta)


if __name__ == "__main__":
    polo = Poloniex(apikey, secret)
    results = [result for result in get_results(polo) if result.value > 10e-4]
    results.sort(key=lambda result: result.delta, reverse=True)
    print tabulate(results, headers=Result._fields)
