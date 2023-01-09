# Trying to scrape from yahoo finance
# Modules To Install:
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://sg.finance.yahoo.com/quote/AAPL/financials?p=AAPL"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
page = requests.get(url, headers=headers)
page_content = page.content
soup = BeautifulSoup(page_content, "html.parser")
tabl = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})

income_statement = {}

for t in tabl:
    rows = t.find_all("div", {"class" : "D(tbr) fi-row Bgc($hoverBgColor):h"})
    for row in rows:
        income_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1]