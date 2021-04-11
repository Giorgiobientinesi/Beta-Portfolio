import pandas as pd
import numpy as np
from scipy import stats
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

#World--> IWDA.AS
#Aggregate Bond --> AGG
#Commodities --> SPDR S&P Metals and Mining ETF --> XME
#Volatile Etf ---> Microcap --> IWC


Etf = ['IWDA.AS', 'AGG', 'XME', 'IWC','^GSPC']

#RETRIEVING FROM YAHOO, MONTLHY
World_index = web.get_data_yahoo(Etf[0],'09/04/2016',interval='m')
Aggregate_bond_index = web.get_data_yahoo(Etf[1],'09/04/2016',interval='m')
Metals_index = web.get_data_yahoo(Etf[2],'09/04/2016',interval='m')
Microcap_index = web.get_data_yahoo(Etf[3],'09/04/2016',interval='m')
Sp500 = web.get_data_yahoo(Etf[4],'09/04/2016',interval='m')

#CREATION OF SIMPLE AND LOG RETURN COLUMNS
World_index = World_index.loc[:, ["Adj Close"]]
World_index.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
World_index['simple_rtn'] = World_index.adj_close.pct_change()
World_index['log_rtn'] = np.log(World_index.adj_close / World_index.adj_close.shift(1))

Aggregate_bond_index = Aggregate_bond_index.loc[:, ["Adj Close"]]
Aggregate_bond_index.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
Aggregate_bond_index['simple_rtn'] = Aggregate_bond_index.adj_close.pct_change()
Aggregate_bond_index['log_rtn'] = np.log(Aggregate_bond_index.adj_close / Aggregate_bond_index.adj_close.shift(1))

Metals_index = Metals_index.loc[:, ["Adj Close"]]
Metals_index.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
Metals_index['simple_rtn'] = Metals_index.adj_close.pct_change()
Metals_index['log_rtn'] = np.log(Metals_index.adj_close / Metals_index.adj_close.shift(1))

Microcap_index = Microcap_index.loc[:, ["Adj Close"]]
Microcap_index.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
Microcap_index['simple_rtn'] = Microcap_index.adj_close.pct_change()
Microcap_index['log_rtn'] = np.log(Microcap_index.adj_close / Microcap_index.adj_close.shift(1))

Sp500 = Sp500.loc[:, ["Adj Close"]]
Sp500.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
Sp500['simple_rtn'] = Sp500.adj_close.pct_change()
Sp500['log_rtn'] = np.log(Sp500.adj_close / Sp500.adj_close.shift(1))


#Taking the log_rtn columns to tuple, and then to list
World_index_list = World_index["log_rtn"].tolist()
World_index_lst = []

Aggregate_bond_index_list = Aggregate_bond_index["log_rtn"].tolist()
Aggregate_bond_index_lst = []

Metals_index_list = Metals_index["log_rtn"].tolist()
Metals_index_lst = []

Microcap_index_list = Microcap_index["log_rtn"].tolist()
Microcap_index_lst = []

for el in World_index_list:
    World_index_lst.append(el)
for el in Aggregate_bond_index_list:
    Aggregate_bond_index_lst.append(el)
for el in Metals_index_list:
    Metals_index_lst.append(el)
for el in Microcap_index_list:
    Microcap_index_lst.append(el)

#Ho i log_rtn di ogni strumento

#---------------------------------------------------------------------------------------
def Portfolio_Montlhy_return(list, weights):
    i =1
    while i < len(World_index_list):
        Monthly_returns = World_index_lst[i] * weights[0] + Aggregate_bond_index_lst[i] * weights[1] + Metals_index_lst[i] * weights[2] + Microcap_index_lst[i] * weights[3]
        list.append(Monthly_returns)
        i += 1

Stock_aggressive_portfolio_Mreturn = []
Aggressive_weights = [0.3, 0.1, 0.1, 0.5]

Portfolio_Montlhy_return(Stock_aggressive_portfolio_Mreturn, Aggressive_weights)



df_Stock_aggressive_portfolio_Mreturn = pd.DataFrame(Stock_aggressive_portfolio_Mreturn, columns=["log_rtn"])

X = Sp500["log_rtn"][1:]
y = df_Stock_aggressive_portfolio_Mreturn["log_rtn"]
slope, intercept, r_value, p_value, std_err = stats.linregress(X, y)

print(Stock_aggressive_portfolio_Mreturn)
print("The beta of the Stock Aggressive Portfolio is " + str(slope))
print("The average montlhy expected return of the Stock Aggressive Portfolio is " + str(sum(Stock_aggressive_portfolio_Mreturn)/len(Stock_aggressive_portfolio_Mreturn)))

#-------------------------------------
Conservative_portfolio = []
Conservative_weights = [0.2, 0.5, 0.2, 0.1] #Conservative
Portfolio_Montlhy_return(Conservative_portfolio, Conservative_weights)

df_Conservative_portfolio= pd.DataFrame(Conservative_portfolio, columns=["log_rtn"])

X1 = Sp500["log_rtn"][1:]
y1 = df_Conservative_portfolio["log_rtn"]
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(X1, y1)

print(Conservative_portfolio)
print("The beta of the Conservative Portfolio is " + str(slope1))
print("The average montlhy expected return of the Conservative Portfolio is " + str(sum(Conservative_portfolio)/len(Conservative_portfolio)))