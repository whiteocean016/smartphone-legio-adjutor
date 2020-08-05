import pandas as pd
from fuzzywuzzy import fuzz, process

df_antutu = pd.read_csv("data_antutu.csv")
df_geekbench = pd.read_csv("data_geekbench.csv")
df_gsmarena = pd.read_csv("data_gsmarena.csv")
df_passmark = pd.read_csv("data_passmark.csv")


# add Apple to all iStuff products names (because it's missing)
mask_apple = df_geekbench.name.str.startswith("iPhone") | df_geekbench.name.str.startswith("iPad") | df_geekbench.name.str.startswith("iPod")
df_geekbench.loc[mask_apple, "name"] = df_geekbench.name[mask_apple].apply(lambda x: "Apple " + x)

df_geekbench = df_geekbench.sort_values(by="name")
df_gsmarena = df_gsmarena.sort_values(by="name")
df_passmark = df_passmark.sort_values(by="name")
df_antutu = df_antutu.sort_values(by="name")


df_merged = pd.merge(df_gsmarena, df_geekbench, "outer", on="name")

df_merged["meta_score"] = (df_merged.basemark_os_ii * df_merged.basemark_x * df_merged.geekbench)**(1/3)

df_merged.sort_values("meta_score", ascending=False).head(10)

df_merged[df_merged.name.str.find("Xiaomi Mi")]

# https://stackoverflow.com/a/56315491

def fuzzy_merge(df_1, df_2, key1, key2, threshold=90, limit=2):
    """
    :param df_1: the left table to join
    :param df_2: the right table to join
    :param key1: key column of the left table
    :param key2: key column of the right table
    :param threshold: how close the matches should be to return a match, based on Levenshtein distance
    :param limit: the amount of matches that will get returned, these are sorted high to low
    :return: dataframe with boths keys and matches
    """
    s = df_2[key2].tolist()

    m = df_1[key1].apply(lambda x: process.extract(x, s, limit=limit, scorer=fuzz.partial_ratio))    
    df_1['matches'] = m


    # TODO if only 1 match and its 100% then ok
    # if more than 1 match check if any 100 %
    # if more than 1 match is 100% then do ratio match and take best one
    
    m2 = df_1['matches'].apply(lambda x: [(i[0],i[1]) for i in x if i[1] >= threshold])
    df_1['matches'] = m2

    return df_1

a = fuzzy_merge(df_passmark, df_geekbench, "name", "name", threshold=95, limit=2)

a.sort_values("matches").tail(60)[["name","matches"]]

df_geekbench[df_geekbench.name.str.lower().str.find("redmi note")!=-1]
df_passmark[df_passmark.name.str.lower().str.find("redmi note")!=-1]