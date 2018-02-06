import pandas_datareader.data as web
import pandas as pd
import datetime
import csv
from pandas_datareader._utils import RemoteDataError

filename = "Ticker_MF.csv"
tickers = []
i = 0
ticker_frame = pd.read_csv(filename)
ticker_frame.fillna(0, inplace=True)
new_ticker_frame = ticker_frame[ticker_frame.TICKER_SYMBOL_IDENTIFIER != 0]
all_tickers = new_ticker_frame["TICKER_SYMBOL_IDENTIFIER"]
for ticker in all_tickers:
	if ticker[0] == 'F':
		tickers.append(str(ticker))
print (len(tickers))
# with open(filename) as csvfile:
# 	reader = csv.reader(csvfile, delimiter=',')
# 	for row in reader:
# 		if (row[0][0]) == 'F':
# 			tickers.append(row[0])
			

# tickers = ['FAAGX','FRXIX','FSRVX','FPEMX','FSSPX','^GSPC']

d = {}
data_source = 'yahoo'
start = datetime.datetime(2012,1,1)
end = datetime.datetime(2018,1,1)
# f = web.DataReader(tickers[0],'yahoo','01/01/2015',interval = 'm')
# print (f)
# f = web.get_data_yahoo(tickers[0],'yahoo',start,interval = 'm')
# for ticker in tickers:
# 	try:
# 		f = web.DataReader(ticker, 'yahoo', start, end)
# 	except RemoteDataError:
# 		f.fillna(0,inplace = True)
# 		grouped = f.groupby(pd.Grouper(freq='M')).mean()
# 		cleanData = grouped['Adj Close']
# 	# dataFrame = pd.DataFrame(cleanData)
# 	# cleanData.fillna(0, inplace=True)
# 		cleanData.to_csv('sample_nav_%s.csv',str(ticker))
# 		print (cleanData)

f = web.DataReader(tickers[0], data_source, start, end)
print (tickers[0])
# newDataFrame = {}

# cleanData = f.ix['Close']
# dataFrame = pd.DataFrame(cleanData)

# cleanData.fillna(0, inplace=True)
# print cleanData
# missing values are automatically excluded from the dataset when calculating the mean
# grouped_quarter = f.groupby(pd.Grouper(freq='Q')).mean()
# print(grouped)
# group by year and find the YTD using that annual data 
# grouped_annual = f.groupby(pd.Grouper(freq = 'A')).nth(-1)
grouped_annual = f.groupby(pd.TimeGrouper('A'))
# YTD data of adjusted close using the lambda function
# Grab data from just the first date and apply a transformation using the date in each group.
f["YTD"] = grouped_annual['Close'].transform(lambda x: x/x.iloc[0]-1.0)
# f["Morning Star"] = 
# print ("after")

grouped_quarter = f.groupby(pd.Grouper(freq='Q')).mean()
# newDataFrame[tickers[0]] = grouped_quarter.to_dict()
# new = pd.DataFrame(newDataFrame)
print(grouped_quarter)
# print(new)

# GETTING MORNINGSTAR RATINGS using BeautifulSoup?
# print(grouped.describe())
# grouped.to_csv('sample_nav2.csv')


	# print (grouped)
# replace all the NaNs with 0s


# for ticker in tickers:
# 	dataFrame[ticker].fillna(0, inplace=True)
# print (dataFrame)
# dataFrame.to_csv('sample_nav.csv')
# print(f.ix['Open'])


# from yahoo_finance import Share
# import fix_yahoo_finance as yf
# yf.pdr_override()



# print yahoo.get_price()


