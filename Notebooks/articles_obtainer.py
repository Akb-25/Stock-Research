from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# chromedriver_path=r"C:\Users\25bak\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
def get_article_urls(company):
    # chromedriver_path=r"C:\Users\25bak\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    search_query=str(company)+" share latest news"
    driver=webdriver.Chrome()

    driver.get("https://www.google.com/search")

    search_box=driver.find_element("name","q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    try:
        news_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/search?q=') and contains(@href, 'tbm=nws')]"))

    
        )
        news_tab.click()
    except Exception as e:
        print(f"Error while waiting for News tab: {e}")

    time.sleep(3)

    search_results=driver.find_elements(by=By.CSS_SELECTOR,value=".SoaBEf")
    urls=[]
    for i,result in enumerate(search_results[:10],start=1):
        try:
            link=result.find_element(by=By.XPATH,value=".//a[contains(@href,'http')]")
            url=link.get_attribute("href")
            urls.append(url)
        except Exception as e:
            print(f"Unable to retrieve URL ",e)

    driver.quit()
    return urls

if __name__ == "__main__":
    company="INFY"
    urlList=get_article_urls(company=company)
    print("Urls are obtained")
    print(urlList)
    print("--------------------------------")
    for url in urlList:
        print(url)