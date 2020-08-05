## script to get latest data
import datetime
import shutil

import get_antutu
import get_geekbench
import get_gsmarena
import get_passmark

## move to data folder and rename with date
time_now = datetime.datetime.now()
today_date = f"{time_now.year}_{str(time_now.month).zfill(2)}_{str(time_now.day).zfill(2)}"

shutil.move("data_antutu.csv", f"./data/data_antutu_{today_date}.csv")
shutil.move("data_geekbench.csv", f"./data/data_geekbench_{today_date}.csv")
shutil.move("data_gsmarena.csv", f"./data/data_gsmarena_{today_date}.csv")
shutil.move("data_passmark.csv", f"./data/data_passmark_{today_date}.csv")
