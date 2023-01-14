# Trying to scrape from yahoo finance
# Modules To Install:
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

tickers = ["AAPL", "AMZN", "META", "GOOG", "3988.HK"]
key_statistics = {}

for ticker in tickers:
    url = f"https://sg.finance.yahoo.com/quote/{ticker}/financials?p={ticker}"

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")

    tabl = soup.find_all("table", {"class" : "W(100%) Bdcl(c)"})
    temp_stats = {}

    for t in tabl:
        rows = t.find_all("tr")
        for row in rows:
            try:
                print(row.get_text(separator="|").split("|"))
                temp_stats[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[-1]
            except:
                print("This row " + row.get_text() + " has no value")

    key_statistics[ticker] = temp_stats