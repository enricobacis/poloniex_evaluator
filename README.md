# poloniex_evaluator

Evaulate your Poloniex market trades

## introduction

*Sometimes it's difficult to understand which market is going well in your Poloniex account. This little tool is here to help.*

## Usage

1. Clone this repository
2. Rename the file `src/config.py.changeme` in `src/config.py`
3. Edit the file with your Poloniex `APIKEY` and `SECRET`
4. `make run`

## Output

    market            shares       value         delta
    ---------  -------------  ----------  ------------
    BTC_GNT      502          0.0794164    0.0608193
    BTC_STRAT     55.8729     0.0393468    0.0457939
    BTC_ARDR    2868          0.0996917    0.0257904
    BTC_LTC        2.7        0.0386835    0.0151367
    BTC_NXT     3870          0.0732204    0.0127141
    BTC_SC     32000          0.0288       0.01142
    BTC_FCT        4          0.0213879    0.00879903
    BTC_XRP      738          0.035424     0.00787799
    BTC_REP        2          0.0220973    0.00608315
    BTC_GNO        0.296166   0.0167587    0.0045879
    BTC_MAID     252.211      0.0436552    0.00438857
    BTC_LSK       50          0.018027     0.002962
    BTC_STR     5235.6        0.0221466    0.00219896
    BTC_BURST  10000          0.017        0.002
    BTC_STEEM     50          0.009616     0.000859
    BTC_ZEC        0.1        0.00649589   0.00039951
    BTC_SJCX      19.7        0.0052993   -0.00015596
    BTC_XMR        0.0862036  0.00144081  -0.000597783
    BTC_SYS      427.929      0.0157007   -0.00114818
    BTC_ETC       10.1631     0.0468572   -0.00235772
    XMR_NXT      392.169      0.443763    -0.00623548
    BTC_DASH       0.31       0.0188757   -0.0105091
    
## FAQ

> Q: Will you implement?

> A: This tool seriously need your love and attention, feel free to submit pull requests
