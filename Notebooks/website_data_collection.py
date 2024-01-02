from bs4 import BeautifulSoup
import requests
def website_information(url):
    headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    try:
        response=requests.get(url,headers=headers)
        response.raise_for_status()
        soup= BeautifulSoup(response.text,"html.parser")
        pTags=soup.find_all("p")
        pTexts=[p.text for p in pTags]
        # return pTexts
        # with open("stockData.html","w",encoding="utf-8") as f:
        #     f.write(soup.prettify().encode("utf-8").decode("utf-8"))
        # with open("p_tags_context.txt","w",encoding="utf-8") as f:
        #     for p in pTexts:
        #         f.write(p+"\n")
        return pTexts
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error : {e}")
        return "No info"
    except requests.exceptions.RequestException as e:
        print(f"Request Exception : {e}")
        return "No info"
    except Exception as e:
        print(f"Uneqxpected error : {e}")
        return "No info"
if __name__=="__main__":
    url="https://www.moneycontrol.com/news/business/markets/short-call-of-beckoning-bector-and-healing-wockhardt-roar-in-hdfc-bank-fan-club-and-copper-craze-11742251.html"
    information=website_information(url)
    print(information)