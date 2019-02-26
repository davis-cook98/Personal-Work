import requests
from bs4 import BeautifulSoup
import pandas as pd

url = requests.get("https://www.pro-football-reference.com/boxscores/game-scores.htm")
soup = BeautifulSoup(url.text, "html.parser")

table = soup.find("table", {"class": "sortable stats_table"})

# print(table)
