import pandas as pd
import yfinance as yf

def companies_SandP500() -> pd.DataFrame:
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    html = pd.read_html(url)
    df = html[0]
    return df

def finance_data(tickers: list[str]) -> pd.DataFrame:
    return yf.download(tickers=tickers, 
                       period="ytd", 
                       interval="1d",
                       auto_adjust=True,
                       threads=True,
                       proxy=None)

