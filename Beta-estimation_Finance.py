import pandas_datareader.data as web
import datetime as dt
import streamlit as st
import pandas as pd
from scipy import stats
import numpy as np


#Sp500 --> ^GSPC
#Eurostockk50 --> ^STOXX50E
#Emerging markets --> EEM
#Nasdaq --> ^IXIC
#Dow jones industrial --> DIA
#Germany --> EWG
#Nikkei 225 --> ^N225
#World Index --> IWDA
#Aggregate bond --> AGG
#Russell 2000 --> ^RUT
#Volatility--> ^VIX
#Gold index--> XGD.TO
#Tech industry --> VGT
#High Dividends --> VYM



Etf = ['^GSPC', '^STOXX50E', 'EEM', '^IXIC', 'DIA','EWG', '^N225', 'IWDA.AS','AGG', '^RUT', '^VIX','XGD.TO', 'VGT', 'VYM']
Etf1 = ['Sp500', 'Eurostockk50', 'Emerging markets', 'Nasdaq', 'Dow jones industrial','Germany index', 'Nikkei 225', 'World index','Aggregate Bond', 'Russel 2000', 'Volatility Index','Gold index fund', 'Information Technology index', 'High dividends index fund']


#TITLE OF THE WEB APP
st.write("""
# Beta Prediction App
This app predicts the **beta** and the expected **returns** of your portfolio!
""")

st.sidebar.header('Build your Portfolio')

#SIDEBAR OF THE WEB APP. THIS TAKES THE INPUT OF THE USER(ETF AND WEIGHTS)
First_etf = st.sidebar.selectbox(
    'Select an ETF',
    (['S&P500', 'Eurostoxx50', 'Emerging markets', 'Nasdaq', 'Dow Jones industrial average','Germany index', 'Nikkei 225', 'World index','Aggregate Bond', 'Russel 2000', 'Volatility Index','Gold index fund', 'Information Technology index', 'High dividends index fund'])
)

First_etf_weight = st.sidebar.slider(First_etf, 0, 100, 25)


Second_etf = st.sidebar.selectbox(
    'Select an ETF',
    (['Eurostoxx50', 'S&P500', 'Emerging markets', 'Nasdaq', 'Dow Jones industrial average','Germany index', 'Nikkei 225', 'World index','Aggregate Bond', 'Russel 2000', 'Volatility Index','Gold index fund', 'Information Technology index', 'High dividends index fund'])
)
Second_etf_weight = st.sidebar.slider(Second_etf, 0, 100, 25)

Third_etf = st.sidebar.selectbox(
    'Select an ETF',
    (['Emerging markets', 'S&P500', 'Eurostoxx50', 'Nasdaq', 'Dow Jones industrial average','Germany index', 'Nikkei 225', 'World index','Aggregate Bond', 'Russel 2000', 'Volatility Index','Gold index fund', 'Information Technology index', 'High dividends index fund'])
)
Third_etf_weight = st.sidebar.slider(Third_etf, 0, 100, 25)

Fourth_etf = st.sidebar.selectbox(
    'Select an ETF',
    (['Nasdaq', 'S&P500', 'Eurostoxx50', 'Emerging markets', 'Dow Jones industrial average','Germany index', 'Nikkei 225', 'World index','Aggregate Bond', 'Russel 2000', 'Volatility Index','Gold index fund', 'Information Technology index', 'High dividends index fund'])
)

Fourth_etf_weight = st.sidebar.slider(Fourth_etf, 0, 100, 25)

#DICTIONARY. THIS TRANSFORM THE INPUT IN YAHOO TICKERS. IT IS MADE TO MAKE THE WEB APP MORE USER-FRIENDLY.
d = {
    'S&P500': '^GSPC',
    'Eurostoxx50' : '^STOXX50E',
    'Emerging markets' : 'EEM',
    'Nasdaq' : '^IXIC',
    'Dow Jones industrial average' : 'DIA',
    'Germany index' : 'EWG',
    'Nikkei 225' : '^N225',
    'World index' : 'IWDA.AS',
    'Aggregate Bond' : 'AGG',
    'Russel 2000' : '^RUT',
    'Volatility Index' : '^VIX',
    'Gold index fund' : 'XGD.TO',
    'Information Technology index' : 'VGT',
    'High dividends index fund' : 'VYM'
    }


#TRANSFORM THE USER INPUT INTO A DATAFRAME
def user_input():
    data = {First_etf : str(First_etf_weight) + "%",
            Second_etf : str(Second_etf_weight) + "%",
            Third_etf : str(Third_etf_weight) + "%",
            Fourth_etf : str(Fourth_etf_weight) + "%"}
    features = pd.DataFrame(data, index=[0])
    return features


if (First_etf_weight + Second_etf_weight + Third_etf_weight +Fourth_etf_weight) != 100: #THIS STOPS THE PROGRAM IF THE PORTFOLIO WEIGHTS ARE NOT 100.
    st.write("**The sum of your Portfolio weights must be 100**")
else:
    Portfolio = user_input() #PRINT THE COMPOSITION OF YOUR PORTFOLIO
    st.header('**Your Portfolio composition**')
    st.write(Portfolio)
#..............................................................

#RETRIEVE DATA FROM YAHOO
    df1 = web.get_data_yahoo(d[First_etf],'09/04/2016',interval='m')
    df2 = web.get_data_yahoo(d[Second_etf],'09/04/2016',interval='m')
    df3 = web.get_data_yahoo(d[Third_etf],'09/04/2016',interval='m')
    df4 = web.get_data_yahoo(d[Fourth_etf],'09/04/2016',interval='m')
#MONTHLY RETURN

    df1 = df1.loc[:, ["Adj Close"]] #TAKE ONLY THE COLUMN ADJ CLOSE
    df1.rename(columns={'Adj Close': 'adj_close'}, inplace=True) #RENAME IT
    df1['simple_rtn'] = df1.adj_close.pct_change()
    df1['log_rtn'] = np.log(df1.adj_close / df1.adj_close.shift(1))
    df1_average = df1['log_rtn'].mean() #MEAN OF THE LOG RTN
    df1_average_perc = df1_average * 100 #MAKE IT  EASIER TO READ, DO IT FOR EVERY ETF

    df2 = df2.loc[:, ["Adj Close"]]
    df2.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
    df2['simple_rtn'] = df2.adj_close.pct_change()
    df2['log_rtn'] = np.log(df2.adj_close / df2.adj_close.shift(1))
    df2_average = df2['log_rtn'].mean()
    df2_average_perc = df2_average * 100

    df3 = df3.loc[:, ["Adj Close"]]
    df3.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
    df3['simple_rtn'] = df3.adj_close.pct_change()
    df3['log_rtn'] = np.log(df3.adj_close / df3.adj_close.shift(1))
    df3_average = df3['log_rtn'].mean()
    df3_average_perc = df3_average * 100

    df4 = df4.loc[:, ["Adj Close"]]
    df4.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
    df4['simple_rtn'] = df4.adj_close.pct_change()
    df4['log_rtn'] = np.log(df4.adj_close / df4.adj_close.shift(1))
    df4_average = df4['log_rtn'].mean()
    df4_average_perc = df4_average * 100



    #BETA FOR EACH STOCK
    def regression(Etf): #THIS FUNCTION CALCULATE THE BETA OF THE SELECTED ETF
        sp500 = web.get_data_yahoo('^GSPC', '05/04/2016', interval='m') #RETRIEVE S&P500 DATA
        sp500_list = sp500["Adj Close"].tolist()
        sp500 = pd.DataFrame(sp500_list)
        sp500.columns = ["Adj Close"]
        sp500.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
        sp500['simple_rtn'] = sp500.adj_close.pct_change()
        sp500['log_rtn'] = np.log(sp500.adj_close / sp500.adj_close.shift(1))

        Etf = web.get_data_yahoo(Etf, '05/04/2016', interval='m')
        Etf_list = Etf["Adj Close"].tolist()
        Etf = pd.DataFrame(Etf_list)
        Etf.columns = ["Adj Close"]
        Etf.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
        Etf['simple_rtn'] = Etf.adj_close.pct_change()
        Etf['log_rtn'] = np.log(Etf.adj_close / Etf.adj_close.shift(1))

        X = sp500["log_rtn"][1:] #THE FIRST VALUE IS NAN, SO I TAKE [1:].
        y = Etf["log_rtn"][1:]
        slope, intercept, r_value, p_value, std_err = stats.linregress(X, y) #RETRIEVE MODEL STATS
        return slope

#FIND  BETA FOR EVERY ETF
    beta1 = regression(d[First_etf])
    beta2 = regression(d[Second_etf])
    beta3 = regression(d[Third_etf])
    beta4 = regression(d[Fourth_etf])


    #BETA OF THE PORTFOLIO, USING THE WEIGHTS
    Beta_portfolio = beta1 * (First_etf_weight/100) +beta2 * (Second_etf_weight/100) + beta3 * (Third_etf_weight/100) + beta4 * (Fourth_etf_weight/100)  #WEIGHTS ARE NOT IN %


    #EXPECTED RETURN OF THE PORTFOLIO, USING THE WEIGHTS
    Portfolio_return = df1_average_perc *(First_etf_weight/100) + df2_average_perc *(Second_etf_weight/100)+ df3_average_perc *(Third_etf_weight/100)+ df4_average_perc *(Fourth_etf_weight/100) #WEIGHTS ARE NOT IN %


    #GRAPH COMPARISON

    sp500 = web.get_data_yahoo('^GSPC', '05/04/2016', interval='m')
    sp500_list = sp500["Adj Close"].tolist()
    sp500 = pd.DataFrame(sp500_list)
    sp500.columns = ["Adj Close"]
    sp500.rename(columns={'Adj Close': 'adj_close'}, inplace=True)
    sp500['simple_rtn'] = sp500.adj_close.pct_change()
    sp500['log_rtn'] = np.log(sp500.adj_close / sp500.adj_close.shift(1))

#THE COLUMN 'log_rtn' IS A LIST INSIDE A TUPLE. WE MUST CREATE 2 LIST, AND ITERATE ONE TO OBTAIN THE REAL VALUES
    sp500_list2 = []
    sp500_list1 = sp500["log_rtn"].tolist()
    for el in sp500_list1:
        sp500_list2.append(el)


    df1_list = df1["log_rtn"].tolist()
    df2_list = df2["log_rtn"].tolist()
    df3_list = df3["log_rtn"].tolist()
    df4_list = df4["log_rtn"].tolist()

    df1_list1 = []
    df2_list1 = []
    df3_list1 = []
    df4_list1 = []

    for el in df1_list:
        df1_list1.append(el)
    for el in df2_list:
        df2_list1.append(el)
    for el in df3_list:
        df3_list1.append(el)
    for el in df4_list:
        df4_list1.append(el)

    total_list = []
    weights = [(First_etf_weight / 100), (Second_etf_weight / 100), (Third_etf_weight / 100), (Fourth_etf_weight / 100)] #WEIGHTS ARE NOT IN %
    i = 1
    while i < len(df1_list1):
        elements = df1_list1[i]*weights[0] + df2_list1[i]* weights[1] + df3_list1[i]*weights[2] + df4_list1[i]*weights[3]
        total_list.append(elements)
        i +=1


    #PRINT THE RESULTS IN THE WEB APP
    st.header("**Beta of your portfolio**")
    st.write("The **beta** of your portfolio is " + str(Beta_portfolio)[:5])

    st.header("**Expected returns of your portfolio based on the last 5 years**")
    st.write("The **Expected monthly returns ** of your portfolio is " + str(Portfolio_return)[:5] + "%")

    st.header("**Beta for each Etf**")
    st.write("The " + First_etf + " beta is " +  str(beta1)[:5])
    st.write("The " + Second_etf + " beta is " + str(beta2)[:5])
    st.write("The " + Third_etf + " beta is " + str(beta3)[:5])
    st.write("The " + Fourth_etf +  " beta is " + str(beta4)[:5])

    st.header("**Average monthly return of each element in the last 5 years**")
    st.write("The " + First_etf + " average returns is " +  str(df1_average_perc)[:5] + "%")
    st.write("The " + Second_etf + " average returns is " + str(df2_average_perc)[:5] + "%")
    st.write("The " + Third_etf+ " average returns is " + str(df3_average_perc)[:5] + "%")
    st.write("The " + Fourth_etf +  " average returns is " + str(df4_average_perc)[:5] + "%")


    st.header("**Evaluate the monthly perfomance**")

    st.write("""
    ## Portfolio perfomance
    """)
    chart_data = pd.DataFrame(
    total_list,
    columns = ['Portfolio'])
    st.line_chart(chart_data)

    st.write("""
    ## S&P500 perfomance
    """)
    chart_data2 = pd.DataFrame(
    sp500_list2,
    columns = ['S&P500'])
    st.line_chart(chart_data2)
