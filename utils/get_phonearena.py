import requests
from bs4 import BeautifulSoup

import pandas as pd

res = requests.get("https://www.phonearena.com/phones/benchmarks")

soup = BeautifulSoup(res.text, 'html.parser')

#TODO loads of data; trickier to get at