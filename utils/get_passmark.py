import requests
from bs4 import BeautifulSoup

import pandas as pd

res = requests.get("https://www.androidbenchmark.net/passmark_chart.html")

soup = BeautifulSoup(res.text, 'html.parser')

list_raw = soup.find_all("li", id=lambda tag: tag is not None)

list_names = []
list_passmark = []
list_samples = []
list_cpu_mark = []

for i, item in enumerate(list_raw):
    list_names.append(item.find(class_="prdname").text)
    passmark = item.find(class_="count").text
    passmark = int(passmark.replace(",", ""))
    list_passmark.append(passmark)

    data = item.find(class_="more_details").attrs["onclick"]
    data = data.strip(");").split(", ")
    list_samples.append(int(data[2]))
    list_cpu_mark.append(int(data[-1].strip("'")))

df = pd.DataFrame([], columns=["name","passmark","samples","cpu_mark"])
df.name = list_names
df.passmark = list_passmark
df.samples = list_samples
df.cpu_mark = list_cpu_mark

df.to_csv("data_passmark.csv", index=False)