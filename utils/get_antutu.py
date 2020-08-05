import requests
from bs4 import BeautifulSoup

import pandas as pd

res = requests.get("https://www.antutu.com/en/ranking/rank1.html")

soup = BeautifulSoup(res.text, 'html.parser')

list_raw = soup.findAll(class_ = "list-unstyled newrank-b")

list_names = []
list_cpu = []
list_gpu = []
list_mem = []
list_ux = []
list_total = []

for item in list_raw:
    list_names.append(list(item.find(class_="bfirst").children)[1].strip())
    data = [_.text for _ in list(item.findAll("li"))][1:]
    data = list(map(int, data))
    list_cpu.append(data[0])
    list_gpu.append(data[1])
    list_mem.append(data[2])
    list_ux.append(data[3])
    list_total.append(data[4])

df = pd.DataFrame([], columns=["name","cpu","gpu","mem","ux","total"])
df.name = list_names
df.cpu = list_cpu
df.gpu = list_gpu
df.mem = list_mem
df.ux = list_ux
df.total = list_total

df.to_csv("data_antutu.csv", index=False)