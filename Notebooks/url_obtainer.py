import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from website_data_collection import website_information
import time

def get_url(company):
    search_query=str(company)+" stock wikipedia"
    driver=webdriver.Chrome()
    driver.get("https://www.google.com/search?q="+search_query)
    
    search_results=driver.find_elements(by=By.CSS_SELECTOR,value=".tF2Cxc")
    search_results=search_results[0]
    urls=[]
    try:
        link=search_results.find_element(by=By.XPATH,value=".//a[contains(@href,'http')]")
        url=link.get_attribute("href")
        print(url)
        return url
        # data=website_information(url)
        # return data
    except Exception as e:
        print(f"Unable to find Wikipedia url ",e)
    driver.quit()

if __name__ == "__main__":
    company="SUZLON"
    get_url(company)