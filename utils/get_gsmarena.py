import requests
from bs4 import BeautifulSoup

import pandas as pd

res = requests.get("https://www.gsmarena.com/benchmark-test.php3")

soup = BeautifulSoup(res.text, 'html.parser')

list_raw = soup.findAll("tr")

list_names = []
list_basemark_os_ii = []
list_basemark_x = []

for i, item in enumerate(list_raw):
    if i == 0:
        continue

    list_names.append(item.find("a").text)
    data = item.findAll("b")
    data = [_.text for _ in data]
    data = list(map(lambda x: int(x) if x != "" else "nan", data))
    list_basemark_os_ii.append(data[0])
    list_basemark_x.append(data[1])

df = pd.DataFrame([], columns=["name","basemark_os_ii","basemark_x"])
df.name = list_names
df.basemark_os_ii = list_basemark_os_ii
df.basemark_x = list_basemark_x

df.to_csv("data_gsmarena.csv", index=False)