# Trying to scrape from yahoo finance
# Modules To Install:
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import pandas as pd

tickers = ["AAPL", "AMZN", "META", "GOOG", "3988.HK"]
income_statement_dict = {}
balance_sheet_dict = {}
cashflow_st_dict = {}

for ticker in tickers:
    url = f"https://sg.finance.yahoo.com/quote/{ticker}/financials?p={ticker}"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content, "html.parser")
    tabl = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})

    income_statement = {}
    table_title = {}

    for t in tabl:
        heading = t.find_all("div", {"class" : "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]

        rows = t.find_all("div", {"class" : "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            try:
                print(row.get_text(separator="|").split("|"))
                income_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]
            except:
                print("This row " + row.get_text() + " has no value")
    
    temp = pd.DataFrame(income_statement).T
    temp.columns = table_title["Breakdown"]
    income_statement_dict[ticker] = temp

for ticker in tickers:
    for col in income_statement_dict[ticker].columns:
        income_statement_dict[ticker][col] = income_statement_dict[ticker][col].str.replace(',|-', '')
        income_statement_dict[ticker][col] = pd.to_numeric(income_statement_dict[ticker][col], errors = 'coerce')