#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    analysed_data = pd.read_csv("results/analysed_df.csv")

    probes = []
    for col in analysed_data:
        if col != "sample_id" and col != "group":
            probes.append(col)

    group_order = ["Normal", "CIN1", "CIN2", "CIN3", "Cancer"]

    for probe in probes:
        plt.figure()
        sns.boxplot(data=analysed_data, x="group", y=probe, order=group_order)
        plt.title("Expression of " + probe + " across disease stages")
        plt.xlabel("Disease Stage")
        plt.ylabel("Expression Level")
        plt.savefig("figures/" + probe + "_boxplot.png")
        plt.close()
        print("Saved boxplot for " + probe)


if __name__ == "__main__":
    main()
