from Notebooks.stock_data_collection import get_company_data
from Notebooks.stock_data_collection import save_data_to_db
from Notebooks.plot_chart import plot_company_chart
from Notebooks.articles_obtainer import get_article_urls
from Notebooks.website_data_collection import website_information
from Notebooks.stats_from_data import rsi,macd,moving_average,get_changes_in_weeks,bollinger_band
import pandas as pd

company=str(input("Enter the company symbol : "))
data=get_company_data(symbol=company)
print("*********Company data imported***********")
save_data_to_db(data,company)
print("*********Company data saved**************")
plot_company_chart(company=company)
print("*********Company data plotted************")
urls=get_article_urls(company=company)
print("******Company data url's retreived*******")
information=pd.DataFrame({"url":urls})
websiteData=[]
for url in urls:
    data=website_information(url)
    websiteData.append(data)
print("*****Company data url's content saved****")
website_content=pd.DataFrame({"Data":websiteData})
information=pd.concat([information,website_content],axis=1)
information.to_csv("article_urls_information.csv")
print("Company data url and information combined")
rsi(company,14)
moving_average(company,30,60)
bollinger_band(company,20,2)
macd(company,12,25)
print("*********Successfully Completed**********")