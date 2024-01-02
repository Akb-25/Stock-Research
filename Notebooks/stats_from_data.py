import pandas as pd
def get_stats(company):
    data=pd.read_csv(f"Data/DataFrame/{company}.csv")
    # print(data.sample(6))
def get_dataframe(company):
    data=pd.read_csv(f"Data/DataFrame/{company}.csv")
    return data
def get_changes_in_weeks(company):
    data=get_dataframe(company)
    front=-1
    back=-6
    change=0

    for i in range(1,10):
        change+=((data["Close"].iloc[front]-data["Close"].iloc[back])/data["Close"].iloc[back])*100
        print(f"The cumilative change from {i} weeks is {change:.1f}%")
        print(f"Starting Prices: {data['Close'].iloc[back]} - Ending Prices: {data['Close'].iloc[front]}")
        front-=6
        back-=6
    print("*********************************")
def moving_average(company,small,big):
    data=get_dataframe(company)
    small_average=data["Close"].rolling(window=small).mean()
    small_average=small_average.iloc[-1]
    big_average=data["Close"].rolling(window=big).mean()
    big_average=big_average.iloc[-1]
    if small_average>big_average:
        print("Moving average is ideal")
    else:
        print("Moving average is not ideal")
        print(f"The moving average of {small} days is {small_average} \nThe moving average of {big} days is {big_average}")
    print("***************************************")
def rsi(company,lookback):
    data=get_dataframe(company)
    data["points_gain"]=data["Close"].diff().where(data["Close"].diff()>0,0)
    data["points_lost"]=-data["Close"].diff().where(data["Close"].diff()<0,0)
    avg_points_gained = data["points_gain"].rolling(window=lookback,min_periods=1).mean()
    avg_points_lost = data["points_lost"].rolling(window=lookback,min_periods=1).mean()
    rs=avg_points_gained/avg_points_lost
    rsi=100-(100/(1+rs.iloc[-1]))
    print(f"The rsi is {rsi}")
    if rsi<30:
        print("RSI indicates oversold. Buy Option")
    elif rsi>70:
        print("RSI indicates overbought. Sell Option")
    else:
        print("RSI is in middle")
    print("*********************************")
def bollinger_band(company,window,num_std):
    data=get_dataframe(company)
    data["rolling_mean"]=data["Close"].rolling(window=window).mean()
    data['upper_band'] = data['rolling_mean'] + (data['Close'].rolling(window=window).std() * num_std)
    data['lower_band'] = data['rolling_mean'] - (data['Close'].rolling(window=window).std() * num_std)
    # print(data[["Close","rolling_mean","upper_band","lower_band"]].tail(1))
    close,mean,upperBand,lowerBand=data[["Close","rolling_mean","upper_band","lower_band"]]
    if close<lowerBand:
        print("Close is lower than Lower Band")
    if close>upperBand:
        print("Close is upper than Upper Band")
    elif close>lowerBand and close<upperBand:
        print("Close is between lower and upper")
    print("***********************************")
def macd(company,small=12,large=26,signal_window=9):
    data=get_dataframe(company)
    small_ema=data["Close"].ewm(span=small).mean()
    large_ema=data["Close"].ewm(span=large).mean()
    data["MACD"]=small_ema-large_ema
    data["Signal"]=data["MACD"].ewm(span=signal_window,adjust=False).mean()
    data["MACDhistogram"]=data["MACD"]-data["Signal"]
    print(data[["Close","MACD","Signal","MACDhistogram"]].tail(1))
    #data=data[["Close","MACD","Signal","MACDhistogram"]].apply(pd.to_numeric,errors="coerce")
    macd=data["MACD"].iloc[-1]
    signal=data["Signal"].iloc[-1]
    # print(macd)
    if macd>signal: 
        print(f"MACD is agreeing")
    elif macd<signal:
        print(f"MACD does not confirm")
    else:
        print(f"MACD is unsure")
    print("***********************************")
if __name__ == "__main__":
    company="RELIANCE"
    get_stats(company)
    # get_changes_in_weeks(company)
    moving_average(company,30,60)
    rsi(company,14)
    bollinger_band(company,20,2)
    macd(company,12,25)
    print(".............................................",end="........")