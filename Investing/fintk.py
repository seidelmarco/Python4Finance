from financetoolkit import Toolkit
import os

import sys
import inspect

from pathlib import Path

import time


from urllib.request import urlopen


import certifi
import json

import csv


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.graph_objects as go

import datetime as dt

from myutils import connect, sqlengine, sqlengine_pull_from_db

from p5_get_sp500_list import save_sp500_tickers
from p1add_pricedata_to_database import push_df_to_db_append, pull_df_from_db, push_df_to_db_replace

import pickle

# use the power of a dictionary to loop through several options at once:

settings = {
    'max_columns': None,
    'min_rows': None,
    'max_rows': 10,
    'precision': 6,
    'float_format': lambda x: f'{x:.6f}'
    }

for option, value in settings.items():
    pd.set_option(f'display.{option}', value)

currentdatetime = dt.datetime.now()


# Terminal:
# setx FMP_API_KEY "APIKEY"


# Load API key from environment variable
api_key = os.getenv("FMP_API_KEY")

# Create the toolkit for one or more tickers
tickers = Toolkit(
    tickers=["AAPL", "MSFT", "CVX"],
    api_key=api_key,
    start_date='2026-01-26'
)

# Get some basic financial data
#income_statement = tickers.get_income_statement()

# a Historical example
historical_data = tickers.get_historical_data()

#balance = tickers.get_balance_sheet_statement()
#cashflow = tickers.get_cash_flow_statement()

# a Ratios example
#profitability_ratios = tickers.ratios.collect_profitability_ratios()

#print(type(income_statement))
#print(income_statement)
print(historical_data)
#print(balance)
#print(cashflow)
#print(profitability_ratios)



cur_path = os.path.dirname(__file__)

new_path = os.path.relpath('..\\Assets\\Wilshire-5000-Stocks-New.csv')

# data_folder = Path('Assets/Wilshire-5000-Stocks-New.csv')

with open(new_path, 'r') as f:
    tickers = csv.reader(f)
    for lines in tickers:
        print(lines)

global fx, i

class DataCollection:
    def __int__(self, filename):
        # read textfile
        global fx
        if '__file__' not in locals():
            fx = inspect.getframeinfo(inspect.currentframe())[0]
        else:
            fx = __file__

        # dieser Befehl zeigt mir mein working directory:
        os_dir = os.path.dirname(os.path.abspath(fx))
        print("That's my working dir:\n", os_dir)

        with open(os.path.join(os_dir, filename)) as f:
            # read line for line
            contents = f.read()
            print('Contents of textfile:\n', contents)


m = DataCollection()
print('Data:')
print(m)


