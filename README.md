# python GetIDs

This is a Python port of GetIDs engine that calculates Telegram account age based on known account creation dates.

The original repository can be found [here](https://github.com/wjclub/telegram-bot-getids).

## Installation

```bash
$ pip install -U getids
```

## Usage

You can use the packages in two ways:

### Interactively

```bash
$ python -m getids 1234567 200097591 1200000000
```

#### Expected output:
```text
1234567: older_than 10/2013
200097591: aprox 5/2016
1200000000: newer_than 7/2019
```

### From python code

```python
>>> from getids import get_age
>>>
>>> get_age(1234567)
('older_than', '10/2013')
>>> get_age(200097591)
('aprox', '5/2016')
>>> get_age(1200000000)
('newer_than', '7/2019')
```
