import requests
from bs4 import BeautifulSoup
import pandas as pd

# Websites have identical structure so abstraction
# was used.
def scraper(url, filename):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    allCols = []

    rows = soup.find_all("tr")

    for row in rows:
        cols = row.find_all('td')
        cols=[x.text.strip() for x in cols]
        #print (cols)
        allCols.append(cols)

    del allCols[0]

    df = pd.DataFrame(allCols)
    # Cleans all of the data
    df.columns = df.iloc[0]
    df = df[1:]
    df = df.set_index("NO.")
    #print(df.head())
    df.to_csv(filename)

    print("Done writing " + filename)

scraper("http://www.espn.com/nfl/superbowl/history/winners", "winners.csv")
scraper("http://www.espn.com/nfl/superbowl/history/mvps", "mvp.csv")
