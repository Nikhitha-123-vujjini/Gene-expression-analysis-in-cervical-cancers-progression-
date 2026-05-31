#!/usr/bin/env python3

import pandas as pd

def main():
    dunns_results = pd.read_csv("results/dunns_results.csv")

    significant = dunns_results[dunns_results["p_value"] <= 0.05]

    ranked = significant.groupby("probe")["p_value"].min().reset_index()
    ranked = ranked.sort_values("p_value")
    ranked["rank"] = range(1, len(ranked) + 1)

    top10 = ranked.head(10)
    top10.to_csv("results/significant_results.csv", index=False)
    print(top10.to_string())
    print("Saved to results/significant_results.csv")

if __name__ == "__main__":
    main()

