#!/usr/bin/env python3

import pandas as pd
from scipy import stats

def main():
    analysed_data = pd.read_csv("results/analysed_df.csv")
    print(analysed_data.shape)

    probes = []
    for col in analysed_data:
        if col != "sample_id" and col != "group":
            probes.append(col)
    not_normal_count = 0
    normal_count = 0

    for probe in probes:
        for group in analysed_data["group"].unique():
            value = analysed_data[analysed_data["group"] == group][probe]
            statistic, p_value = stats.shapiro(value)
            print(probe + " - " + group + ":" + " W -",  str(statistic) + "," + str(p_value))
            if p_value > 0.05:
                normal_count += 1
            else:
                not_normal_count += 1

    print("Normal Distributions: " + str(normal_count))
    print("Not Normal Distributions: " + str(not_normal_count))
    

if __name__ == "__main__":
    main()
