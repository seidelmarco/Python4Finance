import datetime as dt
import os

import pandas as pd
from financetoolkit import Toolkit
from tqdm import tqdm

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
#tickers = Toolkit(
    #tickers=["AAPL", "MSFT", "CVX"],
    #api_key=api_key,
   ## start_date='2026-01-26'
#)

# Get some basic financial data
#income_statement = tickers.get_income_statement()

# a Historical example
#historical_data = tickers.get_historical_data()

#balance = tickers.get_balance_sheet_statement()
#cashflow = tickers.get_cash_flow_statement()

# a Ratios example
#profitability_ratios = tickers.ratios.collect_profitability_ratios()

#print(type(income_statement))
#print(income_statement)
#print(historical_data)
#print(balance)
#print(cashflow)
#print(profitability_ratios)



# cur_path = os.path.dirname(__file__)
#
# new_path = os.path.relpath('..\\Assets\\Wilshire-5000-Stocks-New.csv')
#
# # data_folder = Path('Assets/Wilshire-5000-Stocks-New.csv')
#
# with open(new_path, 'r') as f:
#     tickers = csv.reader(f)
#     for lines in tickers:
#         print(lines)
#
# global fx, i
#
# class DataCollection:
#     def __int__(self, filename):
#         # read textfile
#         global fx
#         if '__file__' not in locals():
#             fx = inspect.getframeinfo(inspect.currentframe())[0]
#         else:
#             fx = __file__
#
#         # dieser Befehl zeigt mir mein working directory:
#         os_dir = os.path.dirname(os.path.abspath(fx))
#         print("That's my working dir:\n", os_dir)
#
#         with open(os.path.join(os_dir, filename)) as f:
#             # read line for line
#             contents = f.read()
#             print('Contents of textfile:\n', contents)
#
#
# m = DataCollection()
# print('Data:')
# print(m)



def get_fmp_historicaldata(ohlc_attr: str = 'adjclose', reload_sp500=False):
    """
    This function grabs one column at a time from the ohlc-data and puts it into one dataframe per type
    :param ohlc_attr: beim callen entscheiden lassen, welche Spalte nicht gedropped wird
    dann nur open, high usw. in df und main df schreiben lassen
    :param reload_sp500:
    Spalte wieder auf nur ticker umbenennen
    :return:
    """

    # if reload_sp500 is True:
    #     tickers = save_sp500_tickers()
    # else:
    #     with open('sp500tickers_2402.pickle', 'rb') as f:
    #         tickers = pickle.load(f)
    #         print(tickers)
    #
    # #Todo: tickers ist für toolkit unwxpected type!!!!
    #
    # if not os.path.exists('sp500_dfs'):
    #     os.makedirs('sp500_dfs')

    '''
    Variables:
    '''
    ticker_list= ['AAPL', 'MSFT', 'AMZN', 'TSLA', 'XOM']#, 'AAPL', 'CVX', 'IMPUY', 'MTNOY', 'MSFT']'DE', 'CMCL',

    # Create the toolkit for one or more tickers
    tickers = Toolkit(
        tickers=ticker_list,
        api_key=api_key,
        start_date='2026-01-04',
        end_date = (dt.datetime.now() - dt.timedelta(days=1)).strftime("%Y-%m-%d")
    )

    main_df = pd.DataFrame()

    # only for testing, for speed and performance reasons just investing with one ticker-symbol:
    # tickers = ['DE', 'CMCL', 'AAPL', 'CVX', 'IMPUY', 'MTNOY']
    for count, ticker in enumerate(tqdm(ticker_list)):
        # just in case your connection breaks, we'd like to save our progress!
        try:

            # Get some basic financial data
            # income_statement = tickers.get_income_statement()
            print(ticker)
            # a Historical example
            df = tickers.get_historical_data(enforce_source='FinancialModelingPrep', period='weekly', return_column='Adj Close', progress_bar=True)
        except Exception as e:
            print(f"Error with {ticker}: {e}")

        print(df)
        # an dieser Stelle brauchen wir keinen index setzen, weil 'Date' schon der Index ist df = data.set_index('Date', inplace=True)
        # print(df.index)

        # match ohlc_attr:
        #     case 'open':
        #         df.rename(columns={'Open': ticker}, inplace=True)
        #         df.drop(['Adj Close', 'High', 'Low', 'Close', 'Volume'], axis=1, inplace=True)
        #     case 'high':
        #         df.rename(columns={'High': ticker}, inplace=True)
        #         df.drop(['Adj Close', 'Open', 'Low', 'Close', 'Volume'], axis=1, inplace=True)
        #     case 'low':
        #         df.rename(columns={'Low': ticker}, inplace=True)
        #         df.drop(['Adj Close', 'High', 'Open', 'Close', 'Volume'], axis=1, inplace=True)
        #     case 'close':
        #         df.rename(columns={'Close': ticker}, inplace=True)
        #         df.drop(['Adj Close', 'High', 'Low', 'Open', 'Volume'], axis=1, inplace=True)
        #     case 'volume':
        #         df.rename(columns={'Volume': ticker}, inplace=True)
        #         df.drop(['Adj Close', 'High', 'Low', 'Close', 'Open'], axis=1, inplace=True)
        #     case default:
        #         # wir nennen die Spalte Adj Close 'Ticker' damit wir die 503 Einträge unterscheiden können
        #         df.rename(columns={'Adj Close': ticker}, inplace=True)
        #         df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], axis=1, inplace=True)
        #
        # if main_df.empty:
        #     main_df = df
        # else:
        #     main_df = main_df.join(df, how='outer')
        #
        # if count % 10 == 0:
        #     print(count)

    # main_df.to_excel('sp500_dfs/sp500_' + ohlc_attr + '.xlsx', engine='openpyxl')
    return main_df

if __name__ == '__main__':
    get_fmp_historicaldata()


