#!/usr/bin/env python3

import pandas as pd
from scipy import stats

def main():
    try:
        analysed_data = pd.read_csv("results/analysed_df.csv")
    except FilenotFoundError:
        print("Error: analysed_df.csv not found. Make sure you ran feature_selection.py first.")
        return
    probes = []
    for col in analysed_data:
        if col != "sample_id" and col != "group":
            probes.append(col)

    for probe in probes:
        groups = []
        for group in analysed_data["group"].unique():
            value = analysed_data[analysed_data["group"] == group][probe]
            groups.append(value)

        statistic, p_value = stats.kruskal(*groups)
        print(probe + " - H=" + str(statistic) + " , p=" + str(p_value))


if __name__ == "__main__":
    main()
