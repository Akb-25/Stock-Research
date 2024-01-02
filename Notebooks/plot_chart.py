import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot,iplot

def plot_company_chart(company):
    df=pd.read_csv(f"Data/DataFrame/{company}.csv")
    df["Date"]=pd.to_datetime(df["Date"])
    fig=go.Figure(data=[go.Candlestick(x=df["Date"],
    open=df["Open"],
    high=df["High"],
    low=df["Low"],
    close=df["Close"])])

    fig.update_layout(title='Stock Price Chart',
                  xaxis_title='Date',
                  yaxis_title='Stock Price',
                  xaxis_rangeslider_visible=True)

    # iplot(fig,filename="stock_chart.html")
    fig.write_html(f"{company}_chart.html")

if __name__ =="__main__":
    company="RELIANCE"
    plot_company_chart(company)