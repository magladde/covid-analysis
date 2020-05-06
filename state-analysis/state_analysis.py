import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def isolate_nc():
    df = pd.read_csv("/data/covid-19-data/us-states.csv")
    df = df[df["state"] == "North Carolina"]
    print(df)

def graph_states():
    df = pd.read_csv("D:\\covid-19-analysis\\covid-19-data\\us-states.csv")
    df = df.set_index("date")
    df = df["2020-04-25":"2020-05-01"]
    fig = df.groupby(["state"])['deaths'].plot(legend=True)
    #plt.savefig("figure")
    #plt.clf()
    df_diff = pd.DataFrame(columns=["state", "death_diff"])
    for state in df.groupby(["state"])["deaths"]:
        df_diff = df_diff.append({"state": state[0], "death_diff":(state[1]["2020-05-01"] - state[1]["2020-04-25"])}, ignore_index=True)
    df_pop = pd.read_csv("D:\\covid-19-analysis\\covid-19-data\\state-pop.csv")
    df_pop["pop"] = df_pop["pop"].astype(int)
    df_diff = pd.concat([df_pop.set_index("state"), df_diff.set_index("state")], axis=1, ignore_index=False)
    df_diff["perc_new_deaths"] = df_diff["death_diff"]/df_diff["pop"]
    df_diff = df_diff.sort_values(by=["perc_new_deaths"], ascending=False)
    states = df_diff.head(15)
    print('wait')

graph_states()