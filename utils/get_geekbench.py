import requests
from bs4 import BeautifulSoup

import pandas as pd

res = requests.get("https://browser.geekbench.com/mobile-benchmarks")

soup = BeautifulSoup(res.text, 'html.parser')

list_raw = soup.find_all("tr")

list_names = []
list_geekbench = []

for i, item in enumerate(list_raw):
    if i == 0:
        continue
    elif item.find(class_="score").text == "Score":
        break

    list_names.append(item.find(class_="name").contents[2].strip("\n"))
    list_geekbench.append(int(item.find(class_="score").text.strip("\n")))

df = pd.DataFrame([], columns=["name","geekbench"])
df.name = list_names
df.geekbench = list_geekbench

df.to_csv("data_geekbench.csv", index=False)
