import pandas as pd
import numpy as np
from services.db_connection import get_connection

class StockAnalyzer:
    def __init__(self, symbol):
        self.symbol = symbol
        self.df = self.load_data()

    def load_data(self):
        conn = get_connection()
        if conn is None:
            return pd.DataFrame()

        query = f"SELECT * FROM stocks WHERE stock_symbol = '{self.symbol}'"
        df = pd.read_sql(query, conn)
        df['date'] = pd.to_datetime(df['date'])
        df.sort_values('date', inplace=True)
        df.reset_index(drop=True, inplace=True)
        return df

    def compare_volume_vs_price(self):
        print(self.df[['date', 'volume', 'close']].tail(10))

    def analyze_volatility(self):
        self.df['daily_return'] = self.df['close'].pct_change()
        self.df['volatility'] = self.df['daily_return'].rolling(window=20).std()
        print(self.df[['date', 'volatility']].dropna().tail(10))

    def historical_trend(self):
        print(self.df[['date', 'close']].tail(10))

    def analyze_drawdown(self):
        self.df['cum_max'] = self.df['close'].cummax()
        self.df['drawdown'] = (self.df['close'] / self.df['cum_max']) - 1
        print(self.df[['date', 'drawdown']].tail(10))

    def absolute_return(self):
        result = (self.df['close'].iloc[-1] - self.df['close'].iloc[0]) / self.df['close'].iloc[0]
        print(f"Absolute Return: {round(result * 100, 2)}%")

    def cagr(self):
        days = (self.df['date'].iloc[-1] - self.df['date'].iloc[0]).days
        total_return = self.df['close'].iloc[-1] / self.df['close'].iloc[0]
        cagr_value = (total_return ** (365 / days)) - 1
        print(f"CAGR: {round(cagr_value * 100, 2)}%")

    def days_above_previous_close(self):
        self.df['prev_close'] = self.df['close'].shift(1)
        count = (self.df['close'] > self.df['prev_close']).sum()
        print(f"Days Closed Above Previous Close: {count}")

    def moving_averages(self):
        self.df['ma20'] = self.df['close'].rolling(window=20).mean()
        self.df['ma50'] = self.df['close'].rolling(window=50).mean()
        print(self.df[['date', 'close', 'ma20', 'ma50']].dropna().tail(10))

    def generate_signal(self):
        self.df['ma20'] = self.df['close'].rolling(window=20).mean()
        self.df['ma50'] = self.df['close'].rolling(window=50).mean()
        latest = self.df.dropna().iloc[-1]
        signal = "BUY" if latest['ma20'] > latest['ma50'] else "SELL"
        print(f"Signal based on MA20 vs MA50: {signal}")

    def final_score(self):
        print("Final analysis combining key metrics:")
        self.absolute_return()
        self.cagr()
        self.analyze_drawdown()
        self.generate_signal()