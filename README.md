# poloniex_evaluator

Evaulate your Poloniex market trades

## introduction

*Sometimes it's difficult to understand which market is going well in your
Poloniex account. This little tool is here to help.*

## Usage

1. Clone this repository
2. Add the following environment variables with `export`:  
    `export 'POLONIEX_API_KEY'='<YOUR_POLONIEX_API_KEY>'`   
    `export 'POLONIEX_SECRET'='<YOUR_POLONIEX_SECRET>'`  
4. `make run`

## Output

    ====================== BTC =======================
    market     shares              value         delta
    ---------  -------------  ----------  ------------
    BTC_GNT    502.0          0.081565     0.0629678
    BTC_STRAT  55.87289273    0.0387864    0.0452335
    BTC_ARDR   2868.0         0.098229     0.0243277
    BTC_LTC    2.7            0.0389443    0.0153975
    BTC_NXT    3870.0         0.0729882    0.0124819
    BTC_SC     32000.0        0.0288       0.01142
    BTC_XRP    738.0          0.036162     0.00861599
    BTC_FCT    4.0            0.0208014    0.00821255
    BTC_REP    2.0            0.0220802    0.00606601
    BTC_GNO    0.29616555     0.0167317    0.00456091
    BTC_MAID   252.21114354   0.0427876    0.00352096
    BTC_LSK    50.0           0.018463     0.003398
    BTC_STR    5235.60209424  0.022199     0.00225131
    BTC_BURST  10000.0        0.0171       0.0021
    BTC_STEEM  50.0           0.0094645    0.0007075
    BTC_ZEC    0.1            0.00657337   0.00047699
    BTC_SJCX   19.7           0.00544035  -1.4908e-05
    BTC_XMR    0.08620358     0.00143787  -0.000600721
    BTC_SYS    427.92886001   0.0157949   -0.00105404
    BTC_ETC    10.16314865    0.047064    -0.0021509
    BTC_DASH   0.31           0.018753    -0.0106317
    ---------  -------------  ----------  ------------
                              0.660166     0.197286
    ==================================================

## FAQ

> Q: Will you implement?

> A: This tool seriously need your love and attention, feel free to submit pull
> requests
