#!/usr/bin/env python3

import pandas as pd
import scikit_posthocs as sp

def main():
    analysed_data = pd.read_csv("results/analysed_df.csv")

    probes = []
    for col in analysed_data:
        if col != "sample_id" and col != "group":
            probes.append(col)

    all_results = []

    for probe in probes:
        print("Probe: " + probe)
        result = sp.posthoc_dunn(analysed_data, val_col=probe, group_col="group", p_adjust="bonferroni")
        print(result)
        
        for group1 in result.index:
           for group2 in result.columns:
               if group1 < group2:
                   all_results.append({
                       "probe": probe,
                       "group1": group1,
                       "group2": group2,
                       "p_value": result.loc[group1, group2]
                   })

    results_df = pd.DataFrame(all_results)
    results_df.to_csv("results/dunns_results.csv", index=False)
    print("Saved to results/dunns_results.csv")


if __name__ == "__main__":
    main()
