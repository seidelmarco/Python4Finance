"""
Idea:
- download every stock SimFin
- current SP500
-Wilshire-5000
-Eurostoxx
-Russell-2000

We will use FMP for Data
"""
import sys
import os
import inspect

from pathlib import Path

import numpy as np
import pandas as pd

import time

import datetime as dt


from urllib.request import urlopen


import certifi
import json

import simfin as sf

import csv


"""
FMP:
"""



def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/stable/profile?symbol=AAPL&apikey=d8285415cbc592b214ce8ffa2b376c23")
print(get_jsonparsed_data(url))


"""
Simfin:

mit Wilshire-5000-Liste abgleichen
"""
sf.set_api_key('b71d8245-c277-466d-a9f1-87b84fe7af91')


# Set the local directory where data-files are stored.
# The directory will be created if it does not already exist.
sf.set_data_dir('~/simfin_data/')

# Download the data from the SimFin server and load into a Pandas DataFrame.
df = sf.load_companies(market='us')

# Print the first rows of the data.
#print(df.head())
#print(df)

tickersAll = list(df.index)
print(tickersAll)

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




