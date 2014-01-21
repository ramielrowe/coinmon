## Cryptocurrency Mining Monitoring Scripts ##

### Example Output ###

* give_me_coin.py:

```
    LTC/USD: 1.00000 ($24.050, $24.000)
    Total Hash: 287 kh/s, Shares: 316
    Uncashed: 0.05525 ($1.329, $1.326)
    Round Est.: 0.00088 ($0.021, $0.021)
    History: 0.17171 ($4.130, $4.121)
    worker1 - S: OK, R: 112 kh/s, P: 39.02%
    worker2 - S: OK, R: 175 kh/s, P: 60.98%
```

### Requirements ###

* requests

```
    $ pip install -r pip-requires.txt
```

### Usage ###

* give_me_coin.py:

```
    $ # Refresh stats every 60 seconds
    $ watch -n 60 python give_me_coin.py -k < api_key >
```
