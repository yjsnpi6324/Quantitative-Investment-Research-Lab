"""Trading-day horizon scheduling."""
from datetime import date,timedelta
def add_trading_days(start,horizon,is_trading_day):
    if horizon<1: raise ValueError("horizon must be >= 1")
    d=start; seen=0
    while seen<horizon:
        d+=timedelta(days=1)
        if is_trading_day(d): seen+=1
    return d
def is_due(generated_date,horizon,as_of,is_trading_day):
    return as_of>=add_trading_days(generated_date,horizon,is_trading_day)
