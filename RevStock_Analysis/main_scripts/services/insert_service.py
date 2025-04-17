import os
import pandas as pd
import mysql.connector
from .db_connection import get_connection

def insert_all_stocks():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
    data_folder_path = os.path.join(project_root, 'data')

    if not os.path.exists(data_folder_path):
        print(f"Error: The data folder at {data_folder_path} does not exist.")
        return

    mydb = get_connection()
    if mydb is None:
        return

    cursor = mydb.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume BIGINT,
            dividends FLOAT,
            stock_splits FLOAT,
            stock_symbol VARCHAR(10)
        )
    ''')


    for file in os.listdir(data_folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(data_folder_path, file)
            symbol = file.split(".")[0].upper()

            try:
                df = pd.read_csv(file_path)
                df['stock_symbol'] = symbol

                for _, row in df.iterrows():
                    cursor.execute('''
                        INSERT INTO stocks (date, open, high, low, close, volume, dividends, stock_splits, stock_symbol)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ''', (
                        pd.to_datetime(row['Date']).date(),
                        row['Open'],
                        row['High'],
                        row['Low'],
                        row['Close'],
                        int(row['Volume']),
                        row['Dividends'],
                        row['Stock Splits'],
                        symbol
                    ))

                print(f"Inserted data for {symbol}")

            except Exception as e:
                print(f" Error inserting data for {symbol}: {e}")

    mydb.commit()
    cursor.close()
    mydb.close()


if __name__ == "__main__":
    insert_all_stocks()