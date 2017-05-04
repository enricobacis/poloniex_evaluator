from collections import namedtuple
from itertools import groupby
from operator import itemgetter
from tabulate import tabulate
from poloniex import Poloniex
from six import iteritems, print_
import os
try:
    apikey = os.environ.get('POLONIEX_API_KEY')
    secret = os.environ.get('POLONIEX_SECRET')

except ImportError:
    print_('error: add your key and secret as environment variables.')


Result = namedtuple('Result', ['market', 'shares', 'value', 'delta'])


def get_results(polo, market='all'):
    history = polo.returnTradeHistory(currencyPair=market, start=0, end=2**32-1)
    ticker = polo.returnTicker()

    for market, trades in iteritems(history):

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

def base_market(result):
    return result.market.partition('_')[0]

if __name__ == "__main__":
    polo = Poloniex(apikey, secret)
    results = [result for result in get_results(polo) if result.value > 10e-4]

    for key, group in groupby(sorted(results), key=base_market):
        group = sorted(group, key=lambda result: result.delta, reverse=True)
        last = ('', '', sum(x[2] for x in group), sum(x[3] for x in group))
        rows = tabulate(group + [last], headers=Result._fields).split('\n')

        width = len(rows[0])
        print_('\n' + (' %s ' % key).center(width, '='))

        last = rows.pop(-1)
        print_(*rows, sep='\n')
        print_(rows[1])
        print_(last)
        print_('=' * width + '\n')
