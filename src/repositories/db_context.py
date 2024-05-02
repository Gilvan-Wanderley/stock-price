import yfinance as yf
import pandas as pd
import os
from pytz import timezone


DATABASE_DIR = os.path.join(os.getcwd(), "database")

class Stock:
    def __init__(self, ticker_name: str) -> None:
        self.database_path = os.path.join(DATABASE_DIR, ticker_name + ".csv")
        if os.path.exists(self.database_path):
            self.history = pd.read_csv(self.database_path, index_col=0)
        else:
            self._ticker = yf.Ticker(ticker_name)
            self.history = self._ticker.history(period="max").drop(columns=["Dividends", "Stock Splits"])
            self.history.to_csv(self.database_path)




if __name__ == "__main__":
    sp500 = Stock("^GSPC")
    
    print(sp500.history.index)
    pass
