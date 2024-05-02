import os
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
from setting_database import SettingDatabase
from env import CURRENT_DIR, START_DATA


class MainDatabaseService_CSV:
    def __init__(self, setting_path) -> None:       
        self._settings = SettingDatabase(setting_path)
        self._tickers = [yf.Ticker(name) for name in self._settings.ticker_props]
        self._db = self._settings.load_db()

    def get_data(self):     

        for stock in self._tickers:

            now = datetime.now()
            last_update = self._settings.last_update(stock.ticker)
            total_days = None
            start = None
            if last_update == None:
                total_days = (now - START_DATA).days
                start = START_DATA
            else:
                total_days = (now - last_update).days
                start = last_update

            if total_days > 0:
                for d in range(1, total_days):
                    _start = start + timedelta(days=d)
                    df = stock.history(start=_start,
                                    end=_start + timedelta(days=1),
                                    interval="1h")
                    
                    if not df.empty:
                        if stock.ticker in self._db.keys():
                            self._db[stock.ticker] =  pd.concat([self._db[stock.ticker], df])
                        else:
                            self._db[stock.ticker] = pd.DataFrame()

                self._settings.save_db(stock.ticker, self._db[stock.ticker])



if __name__ == "__main__":
    setting_path = os.path.join(CURRENT_DIR, "main_database", "settings_db.json")
    service = MainDatabaseService_CSV(setting_path)
    service.get_data()
    pass