import yfinance as yf


def calculate_values(entry_price, entry_multiplier, target_multiplier, stop_loss_multiplier):
    entry = float(entry_price) * entry_multiplier
    target = entry * target_multiplier
    stop_loss = entry * stop_loss_multiplier
    return entry, target, stop_loss


def get_index_price():
    nifty = yf.Ticker('^NSEI')
    nifty_price = nifty.history(period='1d')['Close'].iloc[-1]
    sensex = yf.Ticker('^BSESN')
    sensex_price = sensex.history(period='1d')['Close'].iloc[-1]
    return nifty_price, sensex_price
