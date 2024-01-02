import yfinance as yf
import sqlite3 
import matplotlib.pyplot as plt
import pandas as pd
import datetime

today=datetime.date.today()
con=sqlite3.connect("Data/DB/data.sqlite3")
def get_company_data(symbol,start_date="1947-01-01",end_date=today):
    symbol+=".NS"
    data=yf.download(symbol,start_date,end_date)
    return data
def save_data_to_db(data,table_name):
    data.to_csv(f"Data/DataFrame/{table_name}.csv",encoding="utf-8")
    data.to_sql(table_name,con,if_exists="replace")
if __name__ == "__main__":
    symbol="RELIANCE"
    start_date="1947-02-02"
    company_data=get_company_data(symbol,start_date,end_date=today)
    table_name=symbol
    save_data_to_db(company_data,table_name)