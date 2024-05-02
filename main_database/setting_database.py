import os, json
import pandas as pd
from datetime import datetime


class SettingDatabase:
    def __init__(self, path) -> None:
        self._path = path
        self._param = None
        if os.path.exists(path):
            self._param = {}
            with open(path, 'r') as f:
                self._param = json.load(f)
        else:
            raise Exception("settings file not found!")

    @property
    def ticker_props(self) -> dict[str, dict[str, str]]:
        return self._param["tickers"]
    
    @property
    def interval(self) -> str:
        return self._param["request"]["interval"]

    def last_update(self, ticker: str) -> datetime | None:
         date = self.ticker_props[ticker]["last_update"]
         return None if date == "" else datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

    def save_db(self, ticker_name, db):
        db.to_csv(os.path.join(self._param["database"]["connection"], f'{ticker_name}.csv'))
        self._param["tickers"][ticker_name]["last_update"] = str(datetime.now())
        with open(self._path, 'w') as f:
            json.dump(self._param, f)

    def load_db(self) -> dict[str, pd.DataFrame]:
        db = {}
        for key in self.ticker_props:
            database_path = os.path.join(self._param["database"]["connection"], key + ".csv")
            if os.path.exists(database_path):
                db[key] = pd.read_csv(database_path, index_col=0)
            else:
                db[key] =  pd.DataFrame()
        return db
